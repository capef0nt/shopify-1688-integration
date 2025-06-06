import os
import shopify
from dotenv import load_dotenv

load_dotenv()

SHOP_URL = os.getenv("SHOP_URL")
API_VERSION = os.getenv("API_VERSION")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

def activate_shopify_session():
    session = shopify.Session(SHOP_URL, API_VERSION, ACCESS_TOKEN)
    shopify.ShopifyResource.activate_session(session)
    return session

def clear_shopify_session():
    shopify.ShopifyResource.clear_session()
