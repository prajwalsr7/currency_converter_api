# api.py

from flask import Flask, request, jsonify

application = Flask(__name__)

exchange_rates = {
  'EUR': 0.85,
    'GBP': 0.73,
    'JPY': 109.81,
    'CHF': 0.91,
    'CAD': 1.29,
    'AUD': 1.44,
    'NZD': 1.55,
    'SEK': 9.75,
    'NOK': 8.75,
    'DKK': 6.69,
    'PLN': 4.29,
    'RUB': 73.29,
    'HKD': 7.75,
    'SGD': 1.44,
    'BRL': 4.29,
    'CNY': 6.69,
    'INR': 73.29,
    'MXN': 20.29,
    'CZK': 25.29,
    'ILS': 3.29,
    'KRW': 1129.29,
    'ZAR': 15.29,
    'TWD': 27.29,
    'MYR': 4.29,
    'PHP': 44.29,
    'IDR': 13029.29,
    'THB': 36.29,
    'VND': 23029.29,
    'TRY': 3.29,
    'HUF': 32.29,
    'QAR': 3.29,
    'AED': 3.29,
    'USD': 1.0
}

@application.route('/convert', methods=['GET'])
def convert_currency():
    amount = float(request.args.get('amount'))
    from_currency = request.args.get('from_currency').upper()
    to_currency = request.args.get('to_currency').upper()

    if from_currency == to_currency:
        converted_amount = amount
    else:
        usd_amount = amount / exchange_rates[from_currency]
        converted_amount = usd_amount * exchange_rates[to_currency]

    return jsonify({
        'amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency,
        'converted_amount': converted_amount
    })

if __name__ == '__main__':
    application.run(debug=True)


