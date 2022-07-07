
from flask import Flask, render_template,request
from requests import get
from transcript_api import get_text
import summarize 
app=Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('1.html') 

@app.route('/submit',methods=['GET','POST'])
def submit():
    str1=""
    if request.method=='POST':
        string = request.form['fname']
        (text1,punct_text,ans_string1,ans_string2)=get_text(string)      
    return render_template('1.html',resultText1=ans_string2,resultText2=ans_string1,Text=punct_text,simple=text1)



if__name__="__main__"
app.run(debug=True)

