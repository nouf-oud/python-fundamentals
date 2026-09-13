

product_name = input("Enter product name: ")
price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))
print(f"price data type: {type(price)}")
final_price = price - (price * (discount / 100))
print("final price for %s is: %.2f" % (product_name, final_price))
