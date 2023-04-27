import asyncio
import base64
import json
import uuid

from .examples import (
    payment,
    payment_latam,
    payout,
    payment_link_,
    rebill,
    refund,
    reversal,
    state,
)
from .examples.alternative_payment_methods import (
    bank_transfer_eu_payment,
    boleto,
    lottery,
    pix,
    sepa,
    deposit_express,
    pic_payment,
    bank_transfer_china_payment,
    bank_transfer_china_payout,
    crypto_payment,
    crypto_payout,
)
from .examples import (
    API_KEY, API_VERSION, API_URL, SECRET, REQUEST_TYPE_REQUEST,
)
from .transport import send_request


async def amain():
    is_async = False

    payload, method_type = payment.get_payload()
    # payload, method_type = payment_latam.get_payload()
    # payload, method_type = payout.get_payload()
    # payload, method_type = payment_link_.get_payload()
    # payload, method_type = rebill.get_payload()
    # payload, method_type = refund.get_payload()
    # payload, method_type = reversal.get_payload()

    # payload, method_type = state.get_payload()

    # payload, method_type = bank_transfer_eu_payment.get_payload()
    # payload, method_type = boleto.get_payload()
    # payload, method_type = lottery.get_payload()
    # payload, method_type = pix.get_payload()
    # payload, method_type = sepa.get_payload()
    # payload, method_type = deposit_express.get_payload()
    # payload, method_type = pic_payment.get_payload()
    # payload, method_type = bank_transfer_china_payment.get_payload()
    # payload, method_type = bank_transfer_china_payout.get_payload()
    # payload, method_type = crypto_payment.get_payload()
    # payload, method_type = crypto_payout.get_payload()

    response = await send_request(
        method_type, payload,
        api_url=API_URL,
        api_key=API_KEY,
        secret_key=SECRET,
        api_version=API_VERSION,
        request_type=REQUEST_TYPE_REQUEST,
        correlation_id=str(uuid.uuid4()),
        is_async=is_async,
    )
    print(response)


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(amain())


if __name__ == "__main__":
    main()
