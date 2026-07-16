basket1 = {"apple", "banana", "cherry", "mango", "orange", "grape", "kiwi", "pear", "peach", "plum"}
basket2 = {"apple", "banana", "kiwi", "pear", "peach", "plum", "watermelon", "papaya", "pineapple", "coconut", "fig"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("strawberry")
print("Basket 1 after adding strawberry:", basket1)

#Find fruits common to both baskets
common_fruits = basket1.intersection(basket2)
print("Fruits in both baskets:", common_fruits)

union=basket1.union(basket2)
print("All fruits in baskets:", union)

diff=basket1.difference(basket2)
print("difference in basket:", diff)

sym=basket1.symmetric_difference(basket2)
print("symmetric difference in basket:", sym)