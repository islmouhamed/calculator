from flask import Flask, request, jsonify, render_template

# Create the app object
app = Flask(__name__)


# importing function for calculations
from calculator import calculator

# Define calculator
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = calculator(a,b,operation)

    return render_template('index.html', prediction_text=str(result))


if __name__ == "__main__":
    app.run(debug=True)