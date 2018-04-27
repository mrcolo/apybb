
from flask import Flask,jsonify, request, render_template,Response #import main Flask class and request object
from svmNewArticle import evaluate_bias
app = Flask(__name__) #create the Flask app

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
    app.run(debug=True, port=os.environ["PORT"]) #run app in debug mode on port 5000
