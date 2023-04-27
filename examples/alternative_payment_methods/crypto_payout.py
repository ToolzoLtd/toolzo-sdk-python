from .. import get_order_id


METHOD_TYPE = "Crypto.Payout"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "Currency": "USD",
        "Address": "mqgsvC1CsPCW2NMaXAdFZFdqKhGH5kgAtC",
    }
    return payload, METHOD_TYPE
