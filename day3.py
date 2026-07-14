book={"title":"Atomic habits","author":"james clear","pages":320}
print(book["author"])
book["year"]=2018
book["pages"]=321
del book["author"]
print(book)
students=["Riya","Aman","Zoya","Kabir"]
for index,key in enumerate(students,start=1):
    print(f"{index}:{key}")

marks={"Riya":85,"Aman":12,"Zoya":78}
for key,value in marks.items():
    if value>40:
        value="pass"
    else :
        value="fail"
    print(f"{key}:{value}")
sentense="the cat sat on the mat"
words=sentense.split()
print(words)
counts={}
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
print(counts)