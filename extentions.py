import requests
import json
from config import KEYS


class CurrencyConvertor:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
            raise APIException(
                f"Не удалось перевести одинаковые валюты {base}")

        try:
            base_ticker = KEYS[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}")

        try:
            quote_ticker = KEYS[quote]
        except KeyError:
            raise APIException(
                f"Не удалось обработать валюту {quote}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(
                f"Не удалось обработать количество {amount}")

        r = requests.get(
            f"https://free-currency-converter.herokuapp.com/list/convert?source={base_ticker}&destination={quote_ticker}&price={amount}")

        return round(
            json.loads(r.content).get('converted_value'), 2)


class APIException(Exception):
    pass
