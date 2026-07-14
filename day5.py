def reverse_string(s):
    return s[::-1]
def is_palindrome(s):
    s=s.lower()
    return s==s[::-1]
print(is_palindrome('madam'))
def count_vowels(s):
    s=s.lower()
    count=0
    for i in s:
        if i in "aeiou":
            count+=1
    return count
print(count_vowels('madam'))
sentence="  python is Fun  "
sentence=sentence.lower().strip()
print(sentence.split())
new=sentence.split()
newn=[]
for i in new:
    i=i[0].upper()+i[1:]
    newn.append(i)
print(" ".join(newn))