from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "0883e6daf4424c098b2909af062f9dfe"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-11-30&sortBy=publishedAt&apiKey=0883e6daf4424c098b2909af062f9dfe"

@app.route('/')
def home():
    return "API is running successfully "

@app.route('/api/news', methods=['GET'])
def get_news():
    
    response = requests.get(url)
    
    if response.status_code == 200:
        news_data = response.json()
        total_articles = len(news_data['articles'])
        first_article = news_data['articles'][0]
        author = first_article['author']
        content = first_article['content']
        title = first_article['title']
        publishedAt = first_article['publishedAt']

        output_data = {"Total Article Count" : total_articles,
                        "Title": title,
                    "Author": author,
                    "Content": content,
                    "Published At": publishedAt
                    }
        return jsonify (output_data)
     
    else:
        return jsonify ("msg : INVALID API key!")  
    
if __name__ == '__main__':
     app.run(debug = True)