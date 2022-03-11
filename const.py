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
            'id': 'user:13',
            'name': 'Mor Yesharim', 
            'age': 31, 
            'gender': 'female', 
            'status': 'married'
        }
    },
    'user:14': {
        'label': 'person',
        'properties': {
            'id': 'user:14',
            'name': 'John Doe', 
            'age': 34, 
            'gender': 'male', 
            'status': 'single'
        }
    },
    'country:1': {
        'label': 'country',
        'properties': {
            'id': 'country:1',
            'name': 'USA'
        }
    },
    'country:2': {
        'label': 'country',
        'properties': {
            'id': 'country:2',
            'name': 'Prague'
        }
    },
    'country:3': {
        'label': 'country',
        'properties': {
            'id': 'country:3',
            'name': 'Japan'
        }
    },
    'country:4': {
        'label': 'country',
        'properties': {
            'id': 'country:4',
            'name': 'Greece'
        }
    },
    'country:5': {
        'label': 'country',
        'properties': {
            'id': 'country:5',
            'name': 'Canada'
        }
    },
    'country:6': {
        'label': 'country',
        'properties': {
            'id': 'country:6',
            'name': 'China'
        }
    },
    'country:7': {
        'label': 'country',
        'properties': {
            'id': 'country:7',
            'name': 'Amsterdam'
        }
    },
    'country:8': {
        'label': 'country',
        'properties': {
            'id': 'country:8',
            'name': 'Andora'
        }
    },
    'country:9': {
        'label': 'country',
        'properties': {
            'id': 'country:9',
            'name': 'Kazakhstan'
        }
    },
    'country:10': {
        'label': 'country',
        'properties': {
            'id': 'country:10',
            'name': 'Russia'
        }
    },
    'country:11': {
        'label': 'country',
        'properties': {
            'id': 'country:11',
            'name': 'Germany'
        }
    },
    'country:12': {
        'label': 'country',
        'properties': {
            'id': 'country:12',
            'name': 'Italy'
        }
    },
    'country:13': {
        'label': 'country',
        'properties': {
            'id': 'country:13',
            'name': 'Thailand'
        }
    }
}

relationships = [
    {
        'type': 'visited',
        'src_node': 'user:1',
        'src_node_type': 'person',
        'dest_node': 'country:1',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'business'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:1',
        'src_node_type': 'person',
        'dest_node': 'country:4',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:1',
        'src_node_type': 'person',
        'dest_node': 'country:10',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'bsuiness'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:2',
        'src_node_type': 'person',
        'dest_node': 'country:8',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'business'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:3',
        'src_node_type': 'person',
        'dest_node': 'country:4',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:3',
        'src_node_type': 'person',
        'dest_node': 'country:5',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'business'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:3',
        'src_node_type': 'person',
        'dest_node': 'country:5',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:4',
        'src_node_type': 'person',
        'dest_node': 'country:13',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'business'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:4',
        'src_node_type': 'person',
        'dest_node': 'country:12',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:4',
        'src_node_type': 'person',
        'dest_node': 'country:7',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'bsuiness'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:4',
        'src_node_type': 'person',
        'dest_node': 'country:5',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'business'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:5',
        'src_node_type': 'person',
        'dest_node': 'country:1',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:6',
        'src_node_type': 'person',
        'dest_node': 'country:1',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'business'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:7',
        'src_node_type': 'person',
        'dest_node': 'country:1',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:8',
        'src_node_type': 'person',
        'dest_node': 'country:1',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:9',
        'src_node_type': 'person',
        'dest_node': 'country:1',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'business'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:9',
        'src_node_type': 'person',
        'dest_node': 'country:3',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:9',
        'src_node_type': 'person',
        'dest_node': 'country:6',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:9',
        'src_node_type': 'person',
        'dest_node': 'country:12',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'business'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:9',
        'src_node_type': 'person',
        'dest_node': 'country:13',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:10',
        'src_node_type': 'person',
        'dest_node': 'country:7',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:10',
        'src_node_type': 'person',
        'dest_node': 'country:11',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'business'
        }
    },
    {
        'type': 'visited',
        'src_node': 'user:11',
        'src_node_type': 'person',
        'dest_node': 'country:1',
        'dest_node_type': 'country',
        'properties': {
            'purpose': 'pleasure'
        }
    },
]