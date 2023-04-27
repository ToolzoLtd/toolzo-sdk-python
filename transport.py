import base64
import hmac
import json

from hashlib import sha1
from typing import Optional, Awaitable, Union


def decode_response(response_dict) -> "dict":
    text = response_dict.get("text")
    if not text:
        return response_dict
    data = json.loads(text)
    payload = data.get("Payload", {})
    data["Payload"] = json.loads(base64.b64decode(payload).decode())
    response_dict["text"] = data
    return response_dict


async def send_request(
        method_type: "str",
        payload: "dict",
        *,
        api_key: "str",
        encrypted_key: "Optional[str]" = None,
        authentication_tag: "Optional[str]" = None,
        request_type: "Optional[str]" = "Request",
        correlation_id: "Optional[str]" = None,
        ttl: "Optional[str]" = None,
        api_version: "str",
        secret_key: "str",
        api_url: "str",
        is_async: "bool" = True,
) -> "Union[dict, Awaitable[dict]]":

    main_message = {
        "Type": request_type,
        "CorrelationId": correlation_id,
        "Payload": {
            "Type": method_type,
            "ApiVersion": api_version,
            "Payload": payload,
        }
    }

    # Form main_message in JSON format as string;
    main_message = json.dumps(main_message, separators=(',', ':')).encode()
    # main_message in Base64;
    payload_base64 = base64.b64encode(main_message).decode()
    # Convert hmacKey from Base64 string to byte array;
    key_decoded = base64.b64decode(secret_key)
    # Generate a signature using the HMAC algorithm based
    # on the main_message and the secret;
    request_encoded = hmac.new(key_decoded, main_message, sha1)
    # Signature into a Base64 string;
    signature = base64.b64encode(request_encoded.digest()).decode()

    httpMessage = {
        "ApiKey": api_key,
        "Payload": payload_base64,
        "Signature": signature,
    }
    httpMessage_final = json.dumps(httpMessage)

    url = api_url
    headers = {
        'Content-Type': 'application/json'
    }

    if is_async:
        async def do() -> "dict":
            import aiohttp
            async with aiohttp.request("POST", url=url, headers=headers,
                                       data=httpMessage_final) as response:
                response_dict = {"text": await response.read(),
                                 "status_code": response.status}
                return decode_response(response_dict)
        return await do()
    else:
        def do() -> "dict":
            import requests
            response = requests.request("POST", url=url, headers=headers,
                                        data=httpMessage_final)
            response_dict = {"text": response.text,
                             "status_code": response.status_code}
            return decode_response(response_dict)
        return do()

