from flask import Flask, render_template, request, jsonify
from redis import Redis
from datetime import datetime

app = Flask(__name__)
redis = Redis(host="redis", db=0, socket_timeout=5, charset="utf-8", decode_responses=True)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Get the name from the request data
        name = request.json.get('name')

        # Generate the current date and time
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Store both name and date as a single entry in Redis
        entry = f"{name} - {date}"
        redis.rpush('names_dates', entry)

        return jsonify({'name': name, 'date': date}), 201

    if request.method == 'GET':
        # Retrieve the list of name-date entries from Redis
        return jsonify(redis.lrange('names_dates', 0, -1))

@app.route('/action')
def do():
    # Pass the list of name-date entries to the template
    templateData = {'entries': redis.lrange('names_dates', 0, -1)}
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
