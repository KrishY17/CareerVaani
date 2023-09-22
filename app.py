from flask import Flask,redirect,url_for,render_template,request
import numpy as np
import model

app=Flask(__name__)

def calculate_score(responses):
    # Define the correct answers
    correct_answers=["c", "b", "c", "b", "a", "b", "b", "a", "c", "b", "a", "c" ,"b","a","c"  ,"c","b","b","c","a","b","c","a","c","a","a","a","a","a","a",   "c","b","b","c","b","d","a","a","b","a","a","a","a","a","a",  "c","c","c","c","a","a","b","a","a","a","a","a","a","a","c",  "b","b","b","c","a","c","c","a","a","a","a","a","a","a","a",   "a","a","b","c","a","d","b","a","a","a","a","a","a","a" ,"a",  "c","c","d","c","a","a","a","a","a","a","a","a","a","a","a"]
    easy=[1,2,3,4,16,17,18,19,31,32,33,34,46,47,48,49,61,62,63,64,76,77,78,79,91,92,93,94]
    med=[5,6,7,20,21,22,35,36,37,50,51,52,65,66,67,80,81,82,95,96,97]
    hard=[8,9,10,11,12,13,14,15,23,24,25,26,27,28,29,30,38,39,40,41,42,43,44,45,53,54,55,56,57,58,59,60,68,59,70,71,72,73,74,75,83,84,85,86,87,88,89,90,98,99,100,101,102,103,104,105]
    # Initialize score
    score = [0,0,0,0,0,0,0,0]
    
    # Loop through responses and check against correct answers
    for i in range(len(responses)):
        if (i+1) in easy:
           t=1
        elif (i+1) in med:
           t=2
        else:
           t=4
        if responses[i] == correct_answers[i]:
            if (i+1)<=15:
               score[0]+=t
            elif (i+1)<=30:
               score[1]+=t
            elif (i+1)<=45:
               score[2]+=t
            elif (i+1)<=60:
               score[3]+=t
            elif (i+1)<=75:
               score[4]+=t
            elif (i+1)<=90:
               score[5]+=t
            else:
               score[6]+=t
            score[7]+=t;
    
    return score

@app.route('/')
@app.route('/index.html')
def welcome():
  return render_template('index.html')


@app.route('/sign-up.html')
def signup():
  return render_template('sign-up.html') 

@app.route('/log-in.html')
def login():
  return render_template('log-in.html')

@app.route('/aptitude.html')
def aptitude():
  return render_template('aptitude.html')

@app.route('/predictswot', methods=['POST'])
def predict():
    responses = []
    for i in range(1, 106):
        question_key = f'q{i}'
        response = request.form.get(question_key)
        responses.append(response)
    
    score = calculate_score(responses)  # Calculate the score
    
    global swot_report
    # Use the score in your prediction logic
    swot_report = model.swot_analysis(score)
    
    return render_template('result.html', data=swot_report)

   

@app.route('/predictswot',methods=['GET'])
def result():
   return  render_template('result.html',data= swot_report)


if __name__=='__main__':
  app.run(debug=True)