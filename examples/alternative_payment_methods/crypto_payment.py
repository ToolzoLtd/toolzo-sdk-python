from .. import get_order_id

METHOD_TYPE = "Crypto.Payment"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "Currency": "USD",
        "ReturnUrl": "http://yandex.ru",
        "Description": "This is description",
        "ClientInfo": {
            "Email": "johndoe@gmail.com"
        }
    }
    return payload, METHOD_TYPE
