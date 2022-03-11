from pip import main
import redis
from redisgraph import Node, Edge, Graph, Path

'''
TODO:
    - get querying function working
    - add more data
    - abstract methods
    - add flask
'''

nodes = {
    'user:1': {
        'label': 'person',
        'properties': {
            'id': 'user:1',
            'name': 'Roi Lipman', 
            'age': 32, 
            'gender': 'male', 
            'status': 'married'
        }
    },
    'user:2': {
        'label': 'person',
        'properties': {
            'id': 'user:2',
            'name': 'Alon Fital', 
            'age': 32, 
            'gender': 'male', 
            'status': 'married'
        }
    },
    'user:3': {
        'label': 'person',
        'properties': {
            'id': 'user:3',
            'name': 'Ailon Velger', 
            'age': 32, 
            'gender': 'male', 
            'status': 'married'
        }
    },
    'user:4': {
        'label': 'person',
        'properties': {
            'id': 'user:4',
            'name': 'Ori Laslo', 
            'age': 32, 
            'gender': 'male', 
            'status': 'married'
        }
    },
    'user:5': {
        'label': 'person',
        'properties': {
            'id': 'user:5',
            'name': 'Boaz Arad', 
            'age': 31, 
            'gender': 'male', 
            'status': 'married'
        }
    },
    'user:6': {
        'label': 'person',
        'properties': {
            'id': 'user:6',
            'name': 'Omri Traub', 
            'age': 33, 
            'gender': 'male', 
            'status': 'single'
        }
    },
    'user:7': {
        'label': 'person',
        'properties': {
            'id': 'user:7',
            'name': 'Tal Doron', 
            'age': 32, 
            'gender': 'male', 
            'status': 'single'
        }
    },
    'user:8': {
        'label': 'person',
        'properties': {
            'id': 'user:8',
            'name': 'Lucy Yanfital', 
            'age': 30, 
            'gender': 'female', 
            'status': 'married'
        }
    },
    'user:9': {
        'label': 'person',
        'properties': {
            'id': 'user:9',
            'name': 'Jane Chernomorin', 
            'age': 31, 
            'gender': 'female', 
            'status': 'married'
        }
    },
    'user:10': {
        'label': 'person',
        'properties': {
            'id': 'user:10',
            'name': 'Shelly Laslo Rooz', 
            'age': 31, 
            'gender': 'female', 
            'status': 'married'
        }
    },
    'user:11': {
        'label': 'person',
        'properties': {
            'id': 'user:11',
            'name': 'Valerie Abigail Arad', 
            'age': 31, 
            'gender': 'female', 
            'status': 'married'
        }
    },
    'user:12': {
        'label': 'person',
        'properties': {
            'id': 'user:12',
            'name': 'Gal Derriere', 
            'age': 26, 
            'gender': 'male', 
            'status': 'single'
        }
    },
    'user:13': {
        'label': 'person',
        'properties': {
            'id': 'user:1',
            'name': 'Mor Yesharim', 
            'age': 31, 
            'gender': 'female', 
            'status': 'married'
        }
    },
    'user:14': {
        'label': 'person',
        'properties': {
            'id': 'user:1',
            'name': 'John Doe', 
            'age': 33, 
            'gender': 'male', 
            'status': 'single'
        }
    },
    'country:1': {
        'label': 'country',
        'properties': {
            'id': 'country:1',
            'name': 'Japan'
        }
    }
}

uncommitted_nodes = {}

relationships = [
    {
        'type': 'visited',
        'src_node': 'user:1',
        'src_node_type': 'person',
        'dest_node': 'country:1',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    }
]

############## GRAPH QUERIES ##############

# NOTE: will return a QueryResponse object.
def find_node_with_id(id:str):
    query = """MATCH (n) WHERE n.id='{}' RETURN n""".format(id)
    result = redis_graph.query(query)
    result.pretty_print()
    return result

############# GRAPH MUTATIONS #############
def add_sample_nodes():
    global nodes, uncommitted_nodes
    for node_key in nodes.keys():
        node = nodes[node_key]
        graph_node = Node(label=node['label'], properties=node['properties'])
        redis_graph.add_node(graph_node)
        uncommitted_nodes[node_key] = graph_node
    redis_graph.commit()

def add_sample_edges():
    global relationships
    for relationship in relationships:
        add_relationship_to_nodes(relationship, True)   
    redis_graph.commit() 

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
    # connect to redis client
    client = redis.Redis(host='localhost', port=6379)
    redis_graph = Graph('social', client)

    # load data into graph
    add_sample_nodes()
    add_sample_edges()

    query = """MATCH (p:person)-[v:visited {purpose:"pleasure"}]->(c:country)
            RETURN p.name, p.age, v.purpose, c.name"""

    result = redis_graph.query(query)

    # Print resultset
    result.pretty_print()

    # Use parameters
    params = {'purpose':"pleasure"}
    query = """MATCH (p:person)-[v:visited {purpose:$purpose}]->(c:country)
            RETURN p.name, p.age, v.purpose, c.name"""

    result = redis_graph.query(query, params)

    # Print resultset
    result.pretty_print()

    # Use query timeout to raise an exception if the query takes over 10 milliseconds
    result = redis_graph.query(query, params, timeout=10)

    # Iterate through resultset
    for record in result.result_set:
        person_name = record[0]
        person_age = record[1]
        visit_purpose = record[2]
        country_name = record[3]

    query = """MATCH p = (:person)-[:visited {purpose:"pleasure"}]->(:country) RETURN p"""

    result = redis_graph.query(query)

    # Iterate through resultset
    for record in result.result_set:
        path = record[0]
        print(path)


    # IF WANTED – DELETE GRAPH
    redis_graph.delete()