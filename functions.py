def greater_than(x, y):
    return x > y


a = 2
b = 3
result1 = greater_than(a, b)
output1 = "The statement " + str(a) + " is greater than " + str(b) + " is " + str(result1)


a = 10
b = 6
result2 = greater_than(a, b)
output2 = "The statement " + str(a) + " is greater than " + str(b) + " is " + str(result2)

results = [output1, output2]

for res in results:
    print(res)

