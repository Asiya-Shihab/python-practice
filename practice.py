def word_frequency_sorted(sentence):
    new=sentence.split()
    count={}
    for i in new:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return sorted(count.items(),key=lambda x:x[1], reverse=True)
print(word_frequency_sorted("the cat cat cat dog dog sat on the mat the cat ran"))

words=[("apple",5),("banana",1),("cherry",3)]
print(sorted(words))
print(sorted(words,key=lambda x:x[1]))
print(sorted(words,key=lambda x:x[1],reverse=True))