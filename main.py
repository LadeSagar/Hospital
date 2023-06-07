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
    
app.run()