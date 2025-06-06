from fastapi import FastAPI, Request, Header, HTTPException
from webhook_handler import handle_shopify_order
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post("/webhook/orders/create")
async def webhook_orders_create(
    request: Request,
    x_shopify_hmac_sha256: str = Header(None)
):
    raw_body = await request.body()
    json_data = await request.json()
    print(json_data)

    if not handle_shopify_order(raw_body, x_shopify_hmac_sha256, json_data):
        raise HTTPException(status_code=401, detail="Invalid HMAC")
    
    return {"status": "received"}
