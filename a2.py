import array as arr
fruit_counts = arr.array('i', [10, 20, 30, 40, 50])
print("Fruit counts array:", fruit_counts)

fruit_counts.insert(2, 25)  # index,element
fruit_counts.append(60)
print("Fruit counts after adding items:", fruit_counts)

count_of_4 = fruit_counts.count(40)
print("Number of times 4 appears:", count_of_4)

fruit_counts.reverse()
print("Reversed fruit counts array:", fruit_counts  )