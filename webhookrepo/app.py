from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB Atlas Connection
mongo_uri = "mongodb+srv://azhaguazhagu30:j2oW5hkGVUwR2tG7@cluster0.ipwnl5f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client.github_events
events_collection = db.events

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == 'push':
        author = data['pusher']['name']
        to_branch = data['ref'].split('/')[-1]
        timestamp = datetime.utcnow()
        events_collection.insert_one({
            'author': author,
            'action': 'push',
            'to_branch': to_branch,
            'timestamp': timestamp.isoformat()
        })

    elif event_type == 'pull_request':
        author = data['pull_request']['user']['login']
        from_branch = data['pull_request']['head']['ref']
        to_branch = data['pull_request']['base']['ref']
        timestamp = data['pull_request']['created_at']
        merged = data['pull_request'].get('merged', False)
        action_type = 'merge' if merged else 'pull_request'
        events_collection.insert_one({
            'author': author,
            'action': action_type,
            'from_branch': from_branch,
            'to_branch': to_branch,
            'timestamp': timestamp
        })

    return jsonify({'status': 'success'})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def events():
    latest_events = list(events_collection.find().sort('timestamp', -1).limit(10))
    for e in latest_events:
        e['_id'] = str(e['_id'])
    return jsonify(latest_events)

if __name__ == '__main__':
    app.run(debug=True)