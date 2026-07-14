def common_elements(list1,list2):
    return sorted(set(list1).intersection(set(list2)))
list1=[1,2,3,4,5,6,3,2,3,12]
list2=[1,2,3,4,5,6,7,8,9,10]
print(common_elements(list1,list2))