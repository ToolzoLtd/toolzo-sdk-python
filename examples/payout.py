from . import get_order_id

METHOD_TYPE = "Cards.Payout"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "Currency": "USD",
        "CardInfo": {
            "CardNumber": "4111111111111111",
            "CardHolder": "CARD HOLDER",
            "ExpirationYear": "2024",
            "ExpirationMonth": "12",
        }
    }

    return payload, METHOD_TYPE
