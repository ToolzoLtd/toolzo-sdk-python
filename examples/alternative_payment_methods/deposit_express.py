from .. import get_order_id

METHOD_TYPE = "DepositExpress.Payment"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "Currency": "USD",
        "Bank": "mockBank",
        "ClientInfo": {
            "FirstName": "Ivan",
            "LastName": "Ivanov",
            "Birth": "1990-03-01T00:00:00Z",
            "Email": "ivanov@gmail.com",
            "TaxId": "50284414727",
            "PhoneNumber": "75991435892",
            "Zip": "38082365"
        }
    }
    return payload, METHOD_TYPE
