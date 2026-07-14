
def find_average(nums):
    sum=0;
    for number in nums:
        sum+=number
    return sum/len(nums)
def remove_duplicate(nums):
    newnum=set(nums)
    return list(newnum)

numbers=[5,3,8,1,9,2,2]
maximum=0
for number in numbers:
    if number>maximum:
        maximum=number
print(maximum)
print(find_average(numbers))

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(remove_duplicate(numbers))
students=["Riya","Aman","Zoya","Kabir"]
i=0;
for student in students:
    print(f"{i}:{student}")
    i+=1


