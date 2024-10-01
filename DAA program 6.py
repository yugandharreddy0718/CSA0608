def sort_and_find_max(input_list):
    sorted_list=sorted(input_list)
    max_element=sorted_list[-1]
    return max_element
numbers=[5,2,8,1,9]
max_num=sort_and_find_max(numbers)
print("maximum element in the list:",max_num)
