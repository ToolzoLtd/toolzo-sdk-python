from . import get_order_id


METHOD_TYPE = "CardsLatam.Payment"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "ReturnUrl": "https://yandex.ru",
        "Description": "DEBIT",
        "Currency": "USD",
        "RebillFlag": True,
        "CardInfo": {
            "CardNumber": "4111111111111111",
            "CardHolder": "CARD HOLDER",
            "ExpirationYear": "2024",
            "ExpirationMonth": "12",
            "Cvv": "736",
        },
        "ClientInfo": {
            "PhoneNumber": "+75991435892",
            "FirstName": "John",
            "LastName": "Doe",
            "Email": "doejohn@gmail.com",
            "TaxId": "50284414727",
            "Zip": "38082365"
        },
    }

    return payload, METHOD_TYPE
