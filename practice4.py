def group_by_length(words):
    count={}
    for i in words:
        length=len(i)
        if length in count:
            count[length].append(i)
        else:
            count[length]=[i]
    return count
print(group_by_length(["cat","dog","bird","ox"]))

