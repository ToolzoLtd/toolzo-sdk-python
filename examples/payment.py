from . import get_order_id


METHOD_TYPE = "Cards.Payment"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "ReturnUrl": "https://yandex.ru",
        "Description": "DEBIT",
        "Currency": "USD",
        "RebillFlag": True,
        "CardInfo": {
            "CardNumber": "4111111111111111",
            "CardHolder": "CARD HOLDER",
            "ExpirationYear": "2024",
            "ExpirationMonth": "12",
            "Cvv": "736"
        }
    }
    return payload, METHOD_TYPE

