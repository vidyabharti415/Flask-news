from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

GNEWS_API_URL = "https://gnews.io/api/v4/search"
API_KEY = "0ed0732574c016bca148465a114cc4e8" 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/news', methods=['GET'])
def get_news():
    query = request.args.get('q') 
    if not query:
        return jsonify({"error": "Please provide a search query parameter 'q'"}), 400
    
    params = {
        'q': query,
        'apikey': API_KEY
    }
    
    response = requests.get(GNEWS_API_URL, params=params)
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch news articles"}), response.status_code
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

