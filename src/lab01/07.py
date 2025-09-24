a=str(input())
count1=0
count2=0
result=''
for number,letter in enumerate(a):
    if letter.isupper():
        result+=letter
        index1=number
        break
for letter1 in range(len(a)-1):
    count2+=1
    if a[letter1] in '0123456789' and a[letter1+1] not in '0123456789':
        result+=a[letter1+1]
        break

step=count2-number
count3=number+step

while count3 < len(a):
    result+=a[count3]
    if a[count3]=='.':
        break
    count3+=step
print(result)
