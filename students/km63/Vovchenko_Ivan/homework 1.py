#exs1---------------------------
"""
Напишіть програму, яка отримує три числа і друкує їх суму. Кожне 
число користувач вводить у окремому рядку.
"""
print('Program that takes three numbers and prints their sum')
a=int(input('value#1:'))
b=int(input('value#2:'))
c=int(input('value#3:'))
print(a+b+c)
#-------------------------------
#exs2---------------------------
"""
Напишіть програму, яка отримує довжини двох катетів прямокутного 
трикутника та виводить його площу. Користувач вводить довжини 
катетів у окремих рядках.
"""
print('This program count sq')
h= int(input('Cathetus 1:')) #height
b= int(input('Cathetus 2:')) #base
print(0.5 * h * b)
#exs3---------------------------
"""
N студентів отримали K яблук і розподілити їх між собою порівну. 
Неподілені яблука залишились у кошику. Скільки яблук отримає кожен
студент? Скільки яблук залишиться в кошику?
"""
print('This program answer for 2 que. Just input N and K')
n=int(input( )) #students
k=int(input( )) #apples
print(k//n)
print(k%n)
#-------------------------------
#exs4---------------------------
"""
Нехай число N - кількість хвилин, відрахованих після півночі. 
Скільки годин і хвилин буде показувати цифровий годинник, 
якщо за відлік взяти 00:00?
"""
print('Digital clock')
n=int(input( ))
print((n//60)%24) #hour
print((n*60))     #minute 
#-------------------------------
#exs5---------------------------
"""
Напишіть програму, яка вітає користувача, друкуючи слово "Hello", 
ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”
"""
print('just input your name, dude')
a=input( )
print("Hello,"+a+"!")
#-------------------------------
#exs6---------------------------
"""
Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:
	The next number for the number 179 is 180.
	The previous number for the number 179 is 178.
"""
a=input( )
print("The_next_number_for_the_number"+a+"is"+str(int(a)+1)+".")
print("The_previous_number_for_the_number"+a+"is"+str(int(a)-1)+".")
#-------------------------------
#exs7---------------------------
"""
Школа вирішила сформувати три нові групи учнів та надати їм окремі 
класи. У кожному класі необхідно встановити столи для учнів, у 
розрахунку, що за одним столом може сидіти не більше двох учнів. 
Яку мінімальну кількість столів необхідно придбати?
"""
a=input( )
b=input( )
c=input( )
print(str((a//2+a%2)+(b//2+b%2)+(c//2+c%2)))
#-------------------------------
