from flask import Flask, request, render_template
from model import HousePricePredictor

app = Flask(__name__)
predict_module = HousePricePredictor()

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictor', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        area = request.form['area']
        bed = request.form['bedrooms']
        bath = request.form['bathrooms']
        predicted_price = predict_module.generate_price(area,bed,bath)
        return render_template('index.html', area=area,bed=bed,bath=bath, predicted_price=predicted_price)
if __name__ == '__main__':
    app.run(debug=True)