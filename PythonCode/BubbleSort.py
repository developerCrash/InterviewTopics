
def my_sort(my_list):
    for i in range(len(my_list)-1):
        for j in range(0, len(my_list) - i - 1):
            if my_list[j+1] > my_list[j]:
                tmp = my_list[j+1]
                my_list[j+1] = my_list[j]
                my_list[j] = tmp
            
    print(my_list)
    

my_list = [1,2,3,4,5]
my_sort(my_list)
