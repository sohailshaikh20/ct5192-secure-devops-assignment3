import newrelic.agent
try:
    newrelic.agent.initialize(
        config_file='newrelic.ini',
        environment=None,
        log_file='stderr',
        log_level='INFO'
    )
except ImportError:
    print("New Relic import failed - monitoring disabled")

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    print("Home page accessed")
    return jsonify({"message": "Welcome to Secure DevOps App"})

@app.route('/api/health')
def health():
    print("Health check endpoint called")
    return jsonify({"status": "healthy"})

@app.route('/api/data')
def data():
    print("Data endpoint called - returning sample data")
    return jsonify({"items": ["item1", "item2", "item3"]})

if __name__ == '__main__':
    try:
        wsgi_application = newrelic.agent.WSGIApplicationWrapper(app)
        app.run(host='0.0.0.0', port=4000)
    except ImportError:
        app.run(host='0.0.0.0', port=4000)
