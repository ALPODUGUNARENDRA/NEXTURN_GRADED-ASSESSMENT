import json

def parse_json_data(json_data):
    try:
        data = json.loads(json_data)
        return data
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return None

def add_new_product(catalog, product):
    catalog.append(product)
    return catalog

def update_product_price(catalog, product_id, new_price):
    for product in catalog:
        if product["id"] == product_id:
            product["price"] = new_price
            return product
    return "Product not found"

def filter_products_by_availability(catalog):
    available_products = [product for product in catalog if product["available"]]
    return available_products

def filter_products_by_category(catalog, category_name):
    category_products = [product for product in catalog if product["category"] == category_name]
    return category_products

def main(action, catalog, **kwargs):
    actions = {
        "add_product": lambda: add_new_product(catalog, kwargs.get("product")),
        "update_price": lambda: update_product_price(catalog, kwargs.get("product_id"), kwargs.get("new_price")),
        "filter_available": lambda: filter_products_by_availability(catalog),
        "filter_category": lambda: filter_products_by_category(catalog, kwargs.get("category_name")),
    }
    
    if action in actions:
        result = actions[action]()
        print(f"Action '{action}' executed. Result: {result}")
        print("Updated Catalog:", catalog)
        return result
    else:
        print("Invalid action")
        return None

json_data = '''
[
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200, "available": true},
    {"id": 2, "name": "Table", "category": "Furniture", "price": 150, "available": false}
]
'''

catalog = parse_json_data(json_data)

new_product = {"id": 3, "name": "Chair", "category": "Furniture", "price": 75, "available": True}
catalog = main("add_product", catalog, product=new_product)

main("update_price", catalog, product_id=1, new_price=1300)

available_products = main("filter_available", catalog)

electronics_products = main("filter_category", catalog, category_name="Electronics")
