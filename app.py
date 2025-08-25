from flask import Flask, render_template, request

app = Flask(__name__)

# Home route - shows index.html
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route - handles form submission
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        symptoms = request.form['symptoms']  # get symptoms input
        # Dummy output for now, replace later with ML model
        result = f"Prediction based on symptoms: {symptoms}"
        return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
