from flask import Flask, jsonify, render_template, request
import pandas as pd
import pickle
import requests

app = Flask(__name__)

API_KEY = "0883e6daf4424c098b2909af062f9dfe"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-11-30&sortBy=publishedAt&apiKey=0883e6daf4424c098b2909af062f9dfe"

@app.route('/')
def home():
    return "API is running successfully "

def get_cleaned_data(form_data):
    gestation =float (form_data['gestation'])
    parity = int(form_data['parity'])
    age = float(form_data['age'])
    height = float(form_data['height'])
    weight = float(form_data['weight'])
    smoke = float(form_data['smoke'])
    
    cleaned_data = {
        'gestation': gestation,
        'parity': parity,
        'age': age,
        'height': height,
        'weight': weight,
        'smoke': smoke
    }

    return cleaned_data

@app.route('/', methods=['GET'])
#def home():
    #return render_template("index.html")

#define  our endpoint
#@app.route("/predict", methods = ['POST'])
def get_prediction():
    
    #get data from user
    baby_data_form = request.form
    
    baby_data_cleaned = get_cleaned_data(baby_data_form)
    
    #convert into dataframe
    baby_df = pd.DataFrame([baby_data_cleaned])
    
    
    #load ML trained model
    with open("model.pkl", 'rb') as obj:
        model = pickle.load(obj)
        
    #make prediction on user data
    prediction = model.predict(baby_df)
    prediction = round(float(prediction[0]), 2)
   
                       
    #return response in a json format
    response = {"Prediction":prediction}
        
    return render_template("index.html", prediction=prediction)


####### app3.py ###########

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