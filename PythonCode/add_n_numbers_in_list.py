"""
Program to display max value among sum of K Numbers in a list
"""
"""
Logic is:
if list is [1,14,2,4,5,6] and k=2
then sum of group of 2 numbers is 15 16 6 9 11
max value is 16
if k is 3 
then sum of group of 3 numbers is 17 20 11 15
max value is 20
"""

my_list = [1,14,2,4,5,6]
k=3
sum_list = []
my_sum = 0 
max_sum = my_list[0]


for i in range(len(my_list)):
    for j in range(k):
        if (i + k) <= len(my_list):
            if (i+j) < len(my_list) :
                my_sum = my_sum + my_list[i+j]
    if my_sum != 0:
        sum_list.append(my_sum)
    if my_sum > max_sum:
        max_sum = my_sum
    my_sum = 0
        
        
print(sum_list)
print("Max of the sum list is " + str(max_sum))
