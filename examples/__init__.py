API_URL = "https://apidomen/api/v1/"
API_VERSION = "1"
API_KEY = "47620c0e870b4a7e8f2f9f091293ad45"  # your API KEY
SECRET = "D85SKVd7wWdDHfJgrLDry+9/yka1dc9fdXV2YN+JWmVDQjraaF8ugt0ZJ4pZqUq9Dkcdvd/Ti0WFgGVV3UTdUw=="  # your SECRET (hmacKey)
REQUEST_TYPE_REQUEST = "Request"


def get_order_id():
    import os
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, "order_id.txt"), "r+") as file:
        order_id = int(file.read())
        file.seek(0)
        file.write(str(order_id + 1))
    return str(order_id)
