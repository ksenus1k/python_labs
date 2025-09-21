n=int(input())
online=0
offline=0
for i in range(n):
    line=input()
    if 'True' in line:
        online+=1 
    else:
        offline+=1 
print(online,offline)
