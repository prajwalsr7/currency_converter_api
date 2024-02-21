from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your ExchangeRate-API key
API_KEY = 'b7fe7a81a40ea03edf667c4e'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

@app.route('/convert', methods=['GET'])
def convert_currency():
    try:
        from_currency = request.args.get('from')
        to_currency = request.args.get('to')
        amount = float(request.args.get('amount', 1))
        
        if not from_currency or not to_currency:
            return jsonify({'error': 'Please provide both "from" and "to" currencies.'}), 400
        
        if from_currency.upper() == to_currency.upper():
            return jsonify({'error': 'Cannot convert the same currency.'}), 400

        response = requests.get(BASE_URL + from_currency.upper())
        data = response.json()
        rates = data.get('conversion_rates')

        if not rates:
            return jsonify({'error': 'Failed to fetch exchange rates.'}), 500

        if to_currency.upper() not in rates:
            return jsonify({'error': 'Currency not supported.'}), 400

        converted_amount = amount * rates[to_currency.upper()]
        
        return jsonify({
            'from': from_currency.upper(),
            'to': to_currency.upper(),
            'amount': amount,
            'converted_amount': converted_amount
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

