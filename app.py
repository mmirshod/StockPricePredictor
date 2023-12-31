from flask import Flask, render_template, request, flash
import utils

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='Gold')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            Open = float(request.form['Open'])
            High = float(request.form['High'])
            Low = float(request.form['Low'])
            Volume = int(request.form['Volume'])

            prediction = utils.preprocess(Open, High, Low, Volume)

            return render_template('prediction.html', prediction=prediction, title='Gold')
        except ValueError or OverflowError:
            flash('Please enter valid numbers!')


if __name__ == '__main__':
    app.run(debug=True)
