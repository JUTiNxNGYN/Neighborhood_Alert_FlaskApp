from flask import Flask

app = Flask(__name__)

users = {
    '1':{
    'username': 'jnguyen',
    'email': 'jnguyen@ct.com'
    },
    '2': {
    'username': 'dnguyen',
    'email': 'dnguyen@yahoo.com'
    }
}

posts = {
    '1' = {
        'body': 'FLASK WEEK LETS GO!!!',
        'user_id': '1'
    },
    '2' = {
        'body': 'Whiteboard was killer',
        'user_id': '2'
    },
    '3' = {
        'body': 'SERVERS!!!',
        'user_id': '3'
    }
}