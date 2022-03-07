from pip import main
import redis
from redisgraph import Node, Edge, Graph, Path

nodes = {
    'user:1': {
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
        'dest_node': 'country:1',
        'properties': {
            'purpose': 'pleasure'
        }
    }
]

# connect to redis client
client = redis.Redis(host='localhost', port=6379)
redis_graph = Graph('social', client)

def find_node(id:str):
    query = """MATCH (n) WHERE n.id='{}' RETURN n""".format(id)
    result = redis_graph.query(query)
    result.pretty_print()
    return result

for node_key in nodes.keys():
    node = nodes[node_key]
    graph_node = Node(label=node['label'], properties=node['properties'])
    redis_graph.add_node(graph_node)
    uncommitted_nodes[node_key] = graph_node

for relationship in relationships:
    src_node = uncommitted_nodes[relationship['src_node']]
    dest_node = uncommitted_nodes[relationship['dest_node']]
    edge = Edge(src_node, relationship['type'], dest_node, properties=relationship['properties'])
    redis_graph.add_edge(edge)

redis_graph.commit()

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
# redis_graph.delete()