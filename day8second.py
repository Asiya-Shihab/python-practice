with open("numbers.txt","w") as f:
    f.write("1\n")
    f.write("2\n")
    f.write("3\n")
    f.write("4\n")
    f.write("5j\n")
def summation(textfile):
 with open ("numbers.txt","r") as f:
    sum=0
    for line in f:
        line=line.strip()
        try:
            num=int(line)
            sum+=num

        except ValueError:
            print(f"error in {line}")
    print(sum)
summation("numbers.txt")

def safe_list_get(lst,index):
    try:
        return lst[index]
    except IndexError:
        return "index out of range"

print(safe_list_get([2,3,4,5],3))

print(safe_list_get([2,3,4,5],4))

def append_log(filename,message):
    with open(filename,"a") as f:
        f.write(message+'\n')
    with open(filename,'r') as f:
        content=f.read()
        print(content)

append_log("new.txt","hello")
append_log("new.txt","world")
append_log("new.txt","asiya")
scores={"Riya":85}
try:
    num=int("hello")
    print(scores["Zoya"])
except KeyError:
    print("error")
except ValueError:
    print("value error")

def word_count_from_file(filename):
    count={}
    max_value=0
    max_word=''
    try:
        with open(filename,"r") as f:
            for line in f:
                words=line.split()
                for word in words:
                    if word in count:
                        count[word]+=1
                    else:
                        count[word]=1
        for name, value in count.items():
            if value > max_value:
                max_value = value
                max_word = name
        return max_word, max_value
    except FileNotFoundError:
        print("file not found")
        return None


with open("sample.txt","w") as f:
    f.write("the cat sat on the mat\n")
    f.write("the cat ran fast\n")
print(word_count_from_file("sample.txt"))
print(word_count_from_file("input.txt"))
