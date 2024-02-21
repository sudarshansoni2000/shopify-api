# import shopify
access_token='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'
from shopify_api import ShopifyAPI

from fastapi import FastAPI, HTTPException

app = FastAPI()
shopify_api = ShopifyAPI(access_token)


@app.post("/products/")
def create_product(title: str, price: float, sku: str):
    try:
        response = shopify_api.create_product("Gold Necklace",200000, 50)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# shop_url = "https://94f2c673f4425a21cf0abb482d39ca9a:b05c0b253dfe2f0108cbc7c6939b4fbc@StoreTest.myshopify.com/admin"
# shopify.ShopifyResource.set_site(shop_url)
#
# shopify.Session.setup(api_key=API_KEY, secret=API_SECRET)
# # Now, let's try to retrieve some data from the Shopify API
# try:
#     # Let's get the list of products from the Shopify store
#     products = shopify.Product.find()
#     print("Session is connected!")
# except Exception as e:
#     print("Failed to connect to the Shopify store:", e)
#
# path = "Sumangali-Jewellery-Collection-o1.jpg"
#
# new_product = shopify.Product()
# new_product.title = "Jewellery pictures test "
# new_product.body_html = "<b>24 caret gold necklace</b>"
#
# ###########this part is so far good. but the bottom part is not working####
#
# variant = shopify.Variant() # this does not work {'price':9.99 , 'requires_shipping':False}
# variant.price= 9.99
# variant.requires_shipping = False
# new_product.variants =[variant] # this does not work
# new_product.save()
# # new_product.variant_2() # This does not work
# image = shopify.Image()
# with open(path, "rb") as f:
#     filename = path.split("/")[-1:][0]
#     encoded = f.read()
#     image.attach_image(encoded, filename=filename)
# new_product.images = [image] # Here's the change
# new_product.save()
