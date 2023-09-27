from flask import Flask,render_template,url_for,redirect,request
from joblib import load 
import numpy as np

model=load('.\Model\Covid_tested_model.pkl')

app=Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/affected')
def affected():
    return render_template('a.html')

@app.route('/not_affected')
def not_affected():
    return render_template('na.html')


@app.route('/predict_page',methods=['GET','POST'])
def predict_page():
    if request.method == 'GET':
        return render_template('predict.html')
    else:
        cough=request.form ['Cough']
        Fever=request.form['Fever']
        sore_throat=request.form['sore_throat']
        shortness_breath=request.form['shortness_breath']
        Headache=request.form['Headache']
        above_60=request.form['above_60']
        sex=request.form['sex']
        contact=request.form['contact']
        
        x=["1",cough,sore_throat,shortness_breath,Headache,above_60,sex,contact]
        y=[]
        
        for i in x:
            if i.lower() in ['no','abroad visit','female']:
                y.append(0)
            elif i.lower() in ['yes','contact with confirmed','male',"1"]:
                y.append(1)
            else:
                y.append(2)
                
        d=np.array(y,ndmin=2)
        
        pred=model.predict(d)
        
        
        if pred[0] == 0:
            c='not_affected'
        else:
            c='affected'
        
        
        return redirect(url_for(c))
            
        
@app.route('/about_us',methods=['GET'])
def about_us():
    return render_template('about.html')


if __name__=='__main__':
    app.run(debug=True,port=7000)

