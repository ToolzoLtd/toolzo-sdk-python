from .. import get_order_id

METHOD_TYPE = "BankTransferChina.Payment"


def get_payload():
    payload = {
        "OrderId": get_order_id(),
        "Amount": 150,
        "Currency": "USD",
        "ReturnUrl": "https://uat.info.40eeq.xyz/bankpage?o1=379435&o2=1000130&o3=9c314f253c507739adc2efc405d8824f0f0d4944&b1=a568f32604bb85388c3db612a3963352a521b42b10a0cc84c06cd3249b5d8c7a&b2=3b26dbc4100c4ae323737884a529b319b8c07b356b233d96726822c75d3aa38c&b3=29da3831a2d3f8efec74af112fe8de4cc1ddabc71da409327d4592d7281c74af&b4=d488dfe499624ea647ec30b9f28b3d8013eaf100ea3637a80bdfbbc5fd6346e45b37b346d5a6dd9ce319e9bf03dd17fe&b5=e6f256fb6c49e5ac613abd62ef0661a04f3ef7813549a169fd2f3d8550371bcb&b6=9326db5e0825d52b99fab0b6d9a3d1eebc40dae6fd0250b3c5e1b860d888c32b&b7=3a9782354fcb999ec6b8a4296c1aea0dbee0bffd6841246f0bc03779640002f7&b8=d49704e69fc84bd43e101e69457a9c39404912507bcf9c339ba4cae56a9b8259&b9=6328ace2d94640d6d80bd3550601995e3563f7681afa0788e1e6faf00f8accda",
        "ClientInfo": {
            "FirstName": "Ivan",
            "LastName": "Ivanov",
            "Email": "ivanov@gmail.com",
            "PhoneNumber": "+79123456789",
            "Zip": "123456",
            "Country": "Russia",
            "City": "Moscow",
            "Address": "Mira street"
        }
    }
    return payload, METHOD_TYPE
