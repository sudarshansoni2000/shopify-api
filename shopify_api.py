import shopify
import requests


API_KEY = "94f2c673f4425a21cf0abb482d39ca9a"
API_SECRET = 'b05c0b253dfe2f0108cbc7c6939b4fbc'

access_token='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'
class ShopifyAPI:
    def __init__(self, access_token):
        self.base_url = 'https://StoreTest/admin/api/2024-01'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

    def create_product(self, title, price, sku):
        endpoint = '/products.json'
        data = {
            "product": {
                "title": title,
                "variants": [
                    {
                        "price": price,
                        "sku": sku
                    }
                ]
            }
        }
        response = requests.post(f'{self.base_url}{endpoint}', headers=self.headers, json=data)
        return response.json()