from platform import node

from pip import main

import redis
from redisgraph import Node, Edge, Graph, Path

from const import nodes, relationships

# connect to redis client
client = redis.Redis(host='localhost', port=6379)
redis_graph = Graph('social', client)

############## GRAPH QUERIES ##############

# NOTE: will return a QueryResponse object.
def find_node_with_id(id:str):
    query = """MATCH (n) WHERE n.id='{}' RETURN n""".format(id)
    result = redis_graph.query(query)
    result.pretty_print()
    return result

def find_people_who_visited_country(country, params):
    if (params != None):
        query = """MATCH (p:person)-[v:visited %s]->(c:country) WHERE c.name = '%s'
            RETURN p.name, p.age, v.purpose, c.name""" % (params, country)
        result = redis_graph.query(query, params, timeout=10)
    else:
        query = """MATCH (p:person)-[v:visited]->(c:country) WHERE c.name = '%s'
            RETURN p.name, p.age, v.purpose, c.name""" % country
        result = redis_graph.query(query, None, timeout=10)
    
    result.pretty_print()
    
    # Iterate through resultset
    for record in result.result_set:
        person_name = record[0]
        person_age = record[1]
        visit_purpose = record[2]
        country_name = record[3]

############# GRAPH MUTATIONS #############
def add_sample_nodes():
    global nodes
    for node_key in nodes.keys():
        node = nodes[node_key]
        create_record(node)
    redis_graph.commit()

def create_record(node):
    add_node_doc(node['properties'])
    add_node_to_graph(node)

def add_node_doc(properties):
    for key in properties.keys():
        client.hset(properties['id'], key, properties[key])

def add_node_to_graph(node):
    graph_node = Node(label=node['label'], properties=node['properties'])
    redis_graph.add_node(graph_node)

def add_sample_edges():
    global relationships
    for relationship in relationships:
        add_relationship_to_nodes(relationship, True)   

def add_relationship_to_nodes(relationship, relationship_has_property):
    src_node_type = relationship['src_node_type']
    src_node_id = relationship['src_node']
    dest_node_type = relationship['dest_node_type']
    dest_node_id = relationship['dest_node']
    type = relationship['type']
    query = None
    if (relationship_has_property):
        prop_key = list(relationship['properties'].keys())[0]
        prop_val = relationship['properties'][prop_key]
        query = """MATCH (src:%s {%s: '%s'}), (dest:%s {%s: '%s'}) CREATE (src)-[:%s {%s: '%s'}]->(dest)""" % (src_node_type, 'id', src_node_id, dest_node_type, 'id', dest_node_id, type, prop_key, prop_val)
    else:
        query = """MATCH (src:%s{%s: '%s'}), (dest:%s{%s: '%s'}) CREATE (src)-[:%s]->(dest)""" % (src_node_type, 'id', src_node_id, dest_node_type, 'id', dest_node_id, type)
    result = redis_graph.query(query)
    return result
    

# TODO: test this function
def add_nodes_with_relationship(src_node, dest_node, relationship_type, relationship_props):
    edge = Edge(src_node, relationship_type, dest_node, properties=relationship_props)
    redis_graph.add_edge(edge)

################# HELPERS ##################

if __name__ == "__main__":
    # delete nodes before loading
    client.flushall()

    add_sample_nodes()
    add_sample_edges()

    find_people_who_visited_country('USA', None)