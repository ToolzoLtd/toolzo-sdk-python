from .. import get_order_id

METHOD_TYPE = "BankTransferChina.Payout"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "Currency": "USD",
        "BankCode": "mockBank",
        "RecipientAccount": "4564984561151",
        "ClientInfo": {
            "FirstName": "Ivan",
            "LastName": "Ivanov"
        }
    }
    return payload, METHOD_TYPE
