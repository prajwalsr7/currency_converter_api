
# Currency Converter API

This is a simple API for currency conversion. It allows users to convert between different currencies using the latest exchange rates.

## Features

- Convert currency from one currency to another.
- Supports various currencies including EUR - Euro
GBP - British Pound Sterling
JPY - Japanese Yen
CHF - Swiss Franc
CAD - Canadian Dollar
AUD - Australian Dollar
NZD - New Zealand Dollar
SEK - Swedish Krona
NOK - Norwegian Krone
DKK - Danish Krone
PLN - Polish Zloty
RUB - Russian Ruble
HKD - Hong Kong Dollar
SGD - Singapore Dollar
BRL - Brazilian Real
CNY - Chinese Yuan
INR - Indian Rupee
MXN - Mexican Peso
CZK - Czech Koruna
ILS - Israeli New Shekel
KRW - South Korean Won
ZAR - South African Rand
TWD - New Taiwan Dollar
MYR - Malaysian Ringgit
PHP - Philippine Peso
IDR - Indonesian Rupiah
THB - Thai Baht
VND - Vietnamese Dong
TRY - Turkish Lira
HUF - Hungarian Forint
QAR - Qatari Riyal
AED - United Arab Emirates Dirham
USD - United States Dollar

## Usage

### Convert Currency

Send a POST request to the `/convert` endpoint with the following parameters:

- `amount`: The amount to convert.
- `from_currency`: The currency to convert from.
- `to_currency`: The currency to convert to.

Example Request:
