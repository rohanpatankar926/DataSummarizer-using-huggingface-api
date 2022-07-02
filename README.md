### DataSummarizer-using-huggingface-api
This is my nlp project where i have used huggingface tranformers text summarizer api to get the text summaries as an output.The main motive to build this application is to understand how the transformer actually works and how we can used state of the art model apis to get or list out the summary of the text data.

<br>
<br>

### Run app in localhost
1. First clone my repo using git clone command<br>
2. Unzip and open folder in vscode<br>
3. Now visit to https://huggingface.co/ and make an account first<br>
4. After login go to here https://huggingface.co/facebook/bart-large-cnn and on right side click on deploy and you will get an option called `Accelerated Inference` click on that.<br>
5. You will get an api key copy these variable for example: headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"} with api key and replace with my code.<br>
6. Thats it now fire up terminal and type `python app.py` 
7.Enjoy in localhost i.e http://127.0.0.1 
##### Note: Remember to change the host name from 0.0.0.0 to 127.0.0.1 in app.run() section.
<br>
If you face any problem in this contact me https://rohanpatankar.netlify.app/
<br>
Thankyou
