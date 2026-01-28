# Question 2: Shopping Cart (Lists - Searching and Removal)
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
print("number of apples: ", cart.count("apple"))
print("Position of milk is ", cart.index("milk"))
cart.remove("apple")
print("removed item using pop: ", cart.pop())
print("Is banana in the cart? ", "banana" in cart)
print("Final cart: ", cart)
