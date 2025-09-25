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




