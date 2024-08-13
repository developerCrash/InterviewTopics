my_list = [11, 10,2,3,3,4,5,6,7]
largest = second_largest = float('-inf')

for i in my_list:
    if i > largest:
        second_largest = largest
        largest = i
    elif largest > i > second_largest:
        second_largest = i
        
print ("second largest is " + str(second_largest))
