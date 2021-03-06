from flask import Flask,request,jsonify
from flask_cors import CORS
import clean_corpus as cc

from bert import QA
#import clean_corpus as cc

app = Flask(__name__)
CORS(app)

model = QA("model")

@app.route("/predict",methods=['POST'])
def predict():
    #doc = request.json["document"]
    doc = cc.getCleanCorpusEnglish()
    print("Corpus Has been loaded........!")
    q = request.json["question"]
  
    try:
        out = model.predict(doc,q)
        return jsonify({"result":out})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9000)