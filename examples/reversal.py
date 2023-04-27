from . import get_order_id

METHOD_TYPE = "Cards.Reversal"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "ParentOrderId": "10000067",
        "Currency": "USD",
        "Description": "TEST"
    }
    return payload, METHOD_TYPE
