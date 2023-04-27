METHOD_TYPE = "PaymentLink.Add"


def get_payload():
    payload = {
        "PaymentName": "Payment_tratata",
        "Order ID": "link-135",
        "Website": "616-test.com",
        "Currency": "USD",
        "Amount": 150,
        "Description": "test",
        # "Days": "00",
        "Hours": "2",
        # "Minutes": "00",
        "Email": "tratata@gmail.com",
    }

    return payload, METHOD_TYPE
