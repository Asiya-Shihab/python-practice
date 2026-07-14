coordinates=(10,20)
x,y=coordinates
print(f"x={x},y={y}")
def has_duplicates(l):
    return len(l)==len(set(l))
team_a=["Riya","Aman","Zoya"]
team_b=["Zoya","kabir","Aman"]
team_a=set(team_a)
team_b=set(team_b)
print(team_a.intersection(team_b))
print(team_a.difference(team_b))
print(team_a.union(team_b))
def swapped(a,b):
    return(b,a)
print(swapped(1,2))
team_b.remove("dijd")