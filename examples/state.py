METHOD_TYPE = "GetOrderState"


def get_payload():
    payload = {
        "OrderId": "10000069",
    }
    return payload, METHOD_TYPE