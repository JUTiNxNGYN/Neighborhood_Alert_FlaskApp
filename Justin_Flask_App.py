from flask import Flask, request
from uuid import uuid4

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
    '1' :  {
        'body': 'FLASK WEEK PROJECT',
        'user_id': '1'
    },
    '2' : {
        'body': 'Whiteboard was killer',
        'user_id': '2'
    },
    '3' : {
        'body': 'SERVERS!!!',
        'user_id': '1'
    }
}

"""
Create - Post
Retrieve - Get
Update
Delete
"""

#user routes

# @app.route('/user', methods=['GET'])
# def user():
#     return { 'users': list(users.values())}

@app.get('/user')
def user():
    return { 'users': list(users.values())}, 200

@app.post('/user')
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return { 'message': f'{json_body["username"]} created'}, 201 #Good, created


# @app.post('/user', methods=["GET", "POST"])
# def user2():
#     return { 'users': list(users.values())}

@app.put('/user')
def update_user():
    return

@app.delete('/user')
def delete_user():
    pass

#post routes  

@app.get('/post')
def get_posts():
    return

@app.post('/post')
def create_post():
    return

@app.put('/post')
def update_post():
    return

@app.delete('/post')
def delete_post():
    return 


 