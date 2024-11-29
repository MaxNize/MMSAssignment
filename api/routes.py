# In routes.py
from flask import Blueprint, request, jsonify

api = Blueprint('api', __name__)  # Blueprint is named 'api'

# POST route for greeting with a name
@api.route('/api/greet', methods=['POST'])
def greet_user():
    print("HI")
    data = request.get_json()
    print(data)
    return jsonify({'message': f'Hello, { data['name'] }!'})
