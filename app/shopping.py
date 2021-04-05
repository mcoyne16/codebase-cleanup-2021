import os
from datetime import datetime
from pandas import read_csv

def format_usd(my_price):
    """
    Formats a number as USD with $ and two decimals, and thousands separator
    Params my_price is a number (int or float) that we want to formation
    Examples: format_usd(10)
    """
    return f"${my_price:,.2f}"

def lookup_product(product_id, all_products):
    """
    Params :
        product_id (str)
        all_products (list of dict) each dict has "id", "name", "department", "aisle", and "price
    """
    matching_products = [p for p in all_products if str(p["id"]) == str(product_id)]
    if any(matching_products):
        return matching_products[0]
    else:
        return None

#Prevent all the app code from being imported
if __name__ == "__main__":

# READ INVENTORY OF PRODUCTS
    
    products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
    products_df = read_csv(products_filepath)
    products = products_df.to_dict("records")
    
    # CAPTURE PRODUCT SELECTIONS
    
    selected_products = []
    while True:
        selected_id = input("Please select a product identifier: ")
        if selected_id.upper() == "DONE":
            break
        else:
            matching_product = lookup_product(selected_id, products)
            if matching_product:
                selected_products.append(matching_product)
            else:  
                print("OOPS, Couldn't find that product. Please try again.")
    
    checkout_at = datetime.now()
    
    subtotal = sum([float(p["price"]) for p in selected_products])
    
    # PRINT RECEIPT
    
    tax_rate = 0.0875

    print("---------")
    print("CHECKOUT AT: " + str(checkout_at.strftime("%Y-%M-%d %H:%m:%S")))
    print("---------")
    
    receipt = ""
    for p in selected_products:
        receipt += "SELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]) + "\n"
    receipt += "---------\n"
    receipt += f"SUBTOTAL: {format_usd(subtotal)}\n"
    receipt += f"TAX: {format_usd(subtotal * tax_rate)}\n"
    receipt += f"TOTAL: {format_usd(subtotal * tax_rate + subtotal)}\n"
    receipt += "---------\n"
    receipt += "THANK YOU! PLEASE COME AGAIN SOON!\n"
    receipt += "---------\n"

    print(receipt)
    # WRITE RECEIPT TO FILE
    
    receipt_id = checkout_at.strftime('%Y-%M-%d-%H-%m-%S')
    receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")
    
    with open(receipt_filepath, "w") as receipt_file:
        receipt_file.write("------------------------------------------\n")
        receipt_file.write(receipt)