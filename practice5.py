students={"riya":85,"aman":45,"zoya":92,"kabir":38}
bestname=""
bestscore=0
failedstudents=[]
for i,j in students.items():
    if j>bestscore:
        bestscore=j
        bestname=i
    if j<40:
        failedstudents.append(i)

print(bestname,bestscore)
print(failedstudents)
