from .. import get_order_id

METHOD_TYPE = "Sepa.Payout"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "Currency": "USD",
        "ClientInfo": {
            "FirstName": "John",
            "LastName": "Doe",
            "PhoneNumber": "+79123456789",
            "Email": "johnd@gmail.com",
            "Country": "AT",
            "City": "Copenhagen",
            "Zip": "12345",
            "Address": "123, Park Lane",
            "Birth": "1990-01-01T00:00:00"
        },
        "Account": {
            "Iban": "DE89370400440532013000",
            "Country": "AT"
        }
    }
    return payload, METHOD_TYPE
