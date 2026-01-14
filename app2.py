from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

#define  our endpoint
@app.route("/predict", methods = ['POST'])
def get_prediction():
    
    #get data from user
    baby_data = request.get_json()
    
    #convert into dataframe
    baby_df = pd.DataFrame([baby_data])
    

    
    #load ML trained model
    with open("model/model.pkl", 'rb') as obj:
        model = pickle.load(obj)
        
    #make prediction on user data
    prediction = model.predict(baby_df)
    prediction = round(float(prediction[0]), 2)
   
                       
    #return response in a json format
    response = {"Prediction":prediction}
        
    return jsonify(response)

if __name__ == '__main__':
 app.run(debug=True)
        
        
