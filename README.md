# Лабораторная работа №1

## Задание 1
```
name = input("Имя: ")
age = int(input("Возраст :"))
age1= age + 1
print(f"Привет, {name}! Через год тебе будет {age1}.") 
```
![Привет и возраст](./images/lab01/01.r.png)


## Задание 2
```
a=float(input("a: ").replace(',','.'))
b=float(input("b: ").replace(',','.'))
sum=a+b
avg=sum/2
print(f"sum={sum:.2f}; avg={avg:.2f}")
```
![Сумма и среднее](./images/lab01/02.r.png)


## Задание 3
```
price=float(input())
discount=float(input())
vat=float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:  {vat_amount:.2f} ₽")
print(f"Итого к оплате: {total:.2f} ₽")
```
![Чек: скидка и НДС](./images/lab01/03.r.png)


## Задание 4
```
m=int(input("Минуты: "))
hour=m//60
m1=m%60
print(f"{hour}:{m1}")
```
![Минуты → ЧЧ:ММ](./images/lab01/04.r.png)


## Задание 5
```
name=input("ФИО: ").strip()
part=name.split()
length=len(''.join(part))+2
ini=''.join([i[0].upper() for i in part])
print(f"Инициалы: {ini}")
print(f"Длина (символов): {length}")
```
![Инициалы и длина строки](./images/lab01/05.r.png)


## Задание 6
```
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
```
![Задания со звездочкой](./images/lab01/06.r.png)

# Лабораторная работа №2

## Задание 1
```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return ValueError
    return (min(nums), max(nums)) 
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums=list(set(nums))
    unique_nums.sort()
    return unique_nums
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat: list[list | tuple]) -> list:
    res=[]
    for x in mat:
        if not isinstance(x,(list,tuple)):
            raise TypeError(f"строка не строка строк матрицы")
        res.extend(x)
    return res
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![arrays](./images/lab02/1.png)

## Задание 2
```
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    row_length = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != row_length:
            return ValueError
    result = []
    for cl in range(len(mat[0])):
        new_row = []
        for row in range(len(mat)):
            new_row.append(mat[row][cl])
        result.append(new_row)
    return result
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    row_length = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != row_length:
            return ValueError
    result = []
    for row in mat:
        result.append(sum(row))
    return result
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    row_length = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != row_length:
            return ValueError
    result = []
    for col in range(len(mat[0])):
        col_sum = 0
        for row in range(len(mat)):
            col_sum += mat[row][col]
        result.append(col_sum)
    return result
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![matrix](./images/lab02/2.png)

## Задание 3
```
def format_record(rec:tuple[str,str,float])-> str:
    fio,group,gpa=rec
    part_fio=[part.strip() for part in fio.split() if part.strip()]
    ini=[]
    for part in part_fio[1:]:
        if part:
            ini.append(f"{part[0].upper()}.")
    res_fio=f"{part_fio[0]} {''.join(ini)}"
    res_gpa=f"{gpa:.2f}"
    return f"{res_fio}, гр. {group}, GPA {res_gpa}"
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6) ))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![tuples](./images/lab02/3.png)




