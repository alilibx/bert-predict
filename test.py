from flask import jsonify
from bert import QA


model = QA("model")
with open('textraw.txt') as file: 
    data = file.read()
question = "how to get a driving license?"

result = model.predict(data,question)
print(jsonify({"result":result}))