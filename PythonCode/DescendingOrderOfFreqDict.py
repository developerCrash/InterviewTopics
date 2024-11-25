my_list = [23,44,55,36,75,11,19,23,23,23,23,36,36,75]
count_dict = {}
freq_list = []



for i in my_list:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1


for key in count_dict:
    freq_list.append(count_dict[key])


def my_sort(my_list):
    for i in range(len(my_list)):
        for j in range(0, len(my_list) - i - 1):
            if my_list[j+1] > my_list[j]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


freq_list = my_sort(freq_list)
track_list = []


## Without Using Lambda Functions
for i in freq_list:
    for key, value in count_dict.items():
        if value == i and key not in track_list:
            print(f"{key} : {value}")
            track_list.append(key)


### Using Lambda Functions
#repeted_ele = sorted([elem for elem, freq in count_dict.items() if freq > 0], key=lambda x: count_dict[x], reverse=True)


''' 
rep_ele = [elem for elem, freq in count_dict.items() if freq > 0]

for ele in repeted_ele:
    print(f"{ele}: {count_dict[ele]}")


#key=lambda x: count_dict[x],


'''


