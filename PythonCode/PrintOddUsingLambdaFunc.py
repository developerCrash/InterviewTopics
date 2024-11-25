numbers = [1, 2, 3, 4, 5,6,7,8,9]
odd_nums = list(map(lambda x: x**2, numbers))

print(odd_nums)


list(filter(lambda x: x%2 == 1, numbers))
