
import requests
from flask import Flask,render_template
from flask import request
import os

WEB_DIR="webapp"
TEMP_DIR=os.path.join(WEB_DIR,"templates")

app = Flask(__name__,template_folder=TEMP_DIR)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/summarize",methods=["GET","POST"])
def Summarize():
    if request.method== "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}

        data=request.form["data"]

        maxL=int(request.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs":data,
            "parameters":{"min_length":minL,"max_length":maxL},
        })[0]
        
        return render_template("index.html",result=output["summary_text"])
    else:
        return render_template("index.html")

port=int(os.environ.get("PORT",5000))
if __name__=="__main__":                                     
    app.run(host="0.0.0.0",port=port,debug=False)