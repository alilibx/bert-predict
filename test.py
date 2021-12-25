from flask import jsonify
import clean_corpus as cc
from bert import QA


print(cc.getCleanCorpusEnglish())


model = QA("model")

doc = cc.getCleanCorpusEnglish()
question = "how to get a driving license?"

result = model.predict(doc,question)
print(jsonify({"result":result}))