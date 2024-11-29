# In app.py
from flask import Flask
from flask_cors import CORS  # Enable cross-origin requests
from api.routes import api  # Import the correct 'api' variable, not 'api_routes'

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests
app.register_blueprint(api)  # Register blueprint 'api'

if __name__ == '__main__':
    app.run(debug=True)
