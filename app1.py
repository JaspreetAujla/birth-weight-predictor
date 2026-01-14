from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/' , methods=['GET'])
def home():
    return render_template('form1.html')

@app.route('/upload', methods=['POST'])
def get_data():
    
    file = request.files['file']
     
    print("This is what it contains:", request.files)
    print("file:", file)
    
    if file.filename.endswith('.pdf'):
           # path = "userfile/" + file.filename[folder_name + filename ,first you have to create a folder in flask app then run the code]
            path = file.filename
            file.save(path)
            return "We have recorded your file"
    else:
        return "Please upload only PDF files"
    
if __name__ == '__main__':
    app.run(debug = True)
    
