from . import get_order_id

METHOD_TYPE = "Cards.Refund"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "ParentOrderId": "10000018",
        "Currency": "USD",
        "Description": "TEST"
    }
    return payload, METHOD_TYPE
