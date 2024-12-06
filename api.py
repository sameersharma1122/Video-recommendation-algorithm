from flask import Flask, request, jsonify
from preprocess import preprocess_data
from recommendation import content_based_recommendations

app = Flask(__name__)

@app.route('/feed', methods=['GET'])
def get_feed():
    username = request.args.get('username')
    category_id = request.args.get('category_id')
    mood = request.args.get('mood')

    # Replace with actual logic
    recommendations = [{"post_id": "123", "title": "Sample Video"}]
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(port=5000)

