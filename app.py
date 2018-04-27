import os

from flask import Flask,jsonify, request, render_template,Response #import main Flask class and request object
from svmNewArticle import evaluate_bias
app = Flask(__name__) #create the Flask app
port = int(os.environ.get('PORT', 5000))
@app.route('/', methods=['GET'])
def hello():
    print("works")


@app.route('/retrieveInfo', methods=['POST'])
def json_example():
    req_data = request.get_json()
    # # print(req_data['headline'])
    # # print(req_data['text'])
    # # print(req_data['author'])
    # # print(req_data['source'])
    articleHeadline = req_data['headline']
    articleBody = req_data['text'].encode('ascii', 'ignore')
    articleBody = articleBody.replace("\n", "").replace("\t", "")
    fullText = articleHeadline + articleBody
    biasScore = str(evaluate_bias(fullText)[0])
    print(biasScore)
    return biasScore

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port) #run app in debug mode on port 33507
