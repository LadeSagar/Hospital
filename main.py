from flask import Flask, jsonify,render_template,request

from packages.utils import DaibeticPred_class    # call util file

app = Flask(__name__)

@app.route('/')
def home():
    print("well come**************")
    return render_template("shw.html")

@app.route("/Testing",methods= ['POST','GET'])
def showoutput():
    if request.method == "GET":
    
        Glucose       =  eval(request.args.get('Glucose'))
        BloodPressure = eval(request.args.get('BloodPressure'))
        SkinThickness = eval(request.args.get('SkinThickness'))
        Insulin       = eval(request.args.get('Insulin'))
        BMI           = eval(request.args.get('BMI'))
        DiabetesPedigreeFunction = eval(request.args.get('DiabetesPedigreeFunction'))
        Age           = eval(request.args.get('Age'))  
        
        
                
        obj = DaibeticPred_class(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
                
        Result = obj.predict_output()
        
        if Result == 0:
            A = "Petian is diabetic"
        else:
            A = "Petian is Not diabetic"
            
        return render_template("shw.html",Result = A)
    
    elif request.method == "POST":
        ## Ok - it's working with POST method also
        # Glucose       =  eval(request.form.get('Glucose'))
        # BloodPressure = eval(request.form.get('BloodPressure'))
        # SkinThickness = eval(request.form.get('SkinThickness'))
        # Insulin       = eval(request.form.get('Insulin'))
        # BMI           = eval(request.form.get('BMI'))   
        # DiabetesPedigreeFunction = eval(request.form.get('DiabetesPedigreeFunction'))
        # Age           = eval(request.form.get('Age'))
        
        ### or 
        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = float(request.form['Age'])

        obj = DaibeticPred_class(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)

        Result = obj.predict_output()
        
        #Tip : *** no need to again check Result value bcaz it's already handled in utils.py file - it return actual string.
        # if Result[0] == 0:     
        #     A = "Petian is diabetic"
        # else:
        #     A = "Petian is Not diabetic"
        # print("Result is **********",Result)
            
        # return render_template("shw.html",Result = A)
        return render_template("shw.html",Result = Result)

app.run(debug=True)