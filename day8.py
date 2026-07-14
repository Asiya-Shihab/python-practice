with open("journal.txt","w") as f:
    f.write("this is first line\n")
    f.write("this is second line\n")
    f.write("this is third line\n")
with open("journal.txt","r") as f:
        content=f.read()
        print(content)
def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return ("cannot divide by zero")
print(safe_divide(2,0))
try:
    with open("data.txt","r") as f:
       content=f.read()
       print(content)
except FileNotFoundError:
        print("file not exist.")

def safe_int(value):
 try:
    new=int(value)
    return new
 except ValueError:
    return None
print( safe_int("7"))
print(safe_int("hello"))

def read_score(filename):
    with open (filename) as f:
        for line in f:
            content=line.strip()
            try:
                name,score=content.split(",")
                score=int(score)
                print(f"{name}:{score}")
            except ValueError:
                print(f"error in {line}")
with open("score.txt","w") as f:
   f.write("Riya,85\n")
   f.write("aman,92\n")
   f.write("bad line here\n")
   f.write("zoya,notnumber\n")
read_score("score.txt")

print(int("85\n"))