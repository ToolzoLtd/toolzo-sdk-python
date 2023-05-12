API_URL = "https://pay.toolzo.com"
API_VERSION = "1"
API_KEY = "your apikey" 
SECRET = "your secret key"
REQUEST_TYPE_REQUEST = "Request"


def get_order_id():
    import os
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, "order_id.txt"), "r+") as file:
        order_id = int(file.read())
        file.seek(0)
        file.write(str(order_id + 1))
    return str(order_id)
