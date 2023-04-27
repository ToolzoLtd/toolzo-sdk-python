METHOD_TYPE = "Cards.Rebill"


def get_payload():
    payload = {
        "OrderId": "10000069",
        "Amount": 150,
        "Currency": "USD",
        "BindingId": 106837,
    }

    return payload, METHOD_TYPE
