from .. import get_order_id

METHOD_TYPE = "BankTransferEu.Payment"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "Currency": "USD",
        "ReturnUrl": "https://yandex.ru"
    }
    return payload, METHOD_TYPE
