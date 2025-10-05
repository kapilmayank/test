print("Hello, World!")
for i in range(5):
    print("Hello, World!", i)
for num in range(10):
    if num == 5:
        break  # stop the loop
    if num % 2 == 0:
        continue  # skip even numbers
    print(num)
