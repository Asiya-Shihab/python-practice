count=10
while count>0:
    print(count)
    count-=1
for i in range(1,21):
    if i%3==0:
        continue
    print(i)
nums=[4,9,15,23,8,6]
for num in nums:
    if num>20:
        break
    print(num)
for i in range(1,6):
    for j in range(1,6):
        print(f"{i}*{j}={i*j}")

guesses=[2,9,4,7,1]

count=0
while count<len(guesses):
    if guesses[count]==7:
        print("found it")
        break
    count+=1