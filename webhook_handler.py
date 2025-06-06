import hmac
import hashlib
import base64
import os

def verify_hmac(data: bytes, hmac_header: str) -> bool:
    secret = os.getenv("SHOPIFY_WEBHOOK_SECRET").encode()
    digest = hmac.new(secret, data, hashlib.sha256).digest()
    computed_hmac = base64.b64encode(digest).decode()
    return hmac.compare_digest(computed_hmac, hmac_header)

def handle_shopify_order(raw_body, hmac_header, json_data):
    if not verify_hmac(raw_body, hmac_header):
        print("HMAC validation failed")
        return False

    print(f"✅ New order received: #{json_data['id']} | Customer: {json_data['customer']['first_name']}")
    return True
