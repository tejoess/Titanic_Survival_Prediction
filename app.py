from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get form data
            pclass = int(request.form['pclass'])
            age = float(request.form['age'])
            sibsp = int(request.form['sibsp'])
            parch = int(request.form['parch'])
            fare = float(request.form['fare'])
            sex = int(request.form['sex'])
            embarked = request.form['embarked']
            chosen_model = request.form['modelname']
            # Feature engineering
            groupsize = sibsp + parch + 1
            individualfare = fare / groupsize

            if embarked == 'Q':
                embarkedQ = 1
                embarkedS = 0
            elif embarked == 'S':
                embarkedQ = 0
                embarkedS = 1
            else:
                embarkedQ = 0
                embarkedS = 0

            if chosen_model == 'XGB':
                model = joblib.load("models/xgb_model.pkl")
            if chosen_model == 'LogReg':
                model = joblib.load('models/LogReg_model.pkl')
            if chosen_model == 'RanFor':
                model = joblib.load('models/random_forest_model.pkl')
            features = [[pclass, age, sibsp, parch, fare, sex, embarkedQ, embarkedS, groupsize, individualfare]]
            prediction = model.predict(features)[0]
            result = "Passennger survived" if prediction == 1 else "Passenger did not survive"
            return render_template('index.html', prediction=result)
        except Exception as e:
            return render_template('index.html', prediction=f"Error: {str(e)}")

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
