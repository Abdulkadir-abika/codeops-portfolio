#1 temprature label
temprature= int (input("Enter the temprature : "))
if temprature<15:
    print("Cold")
elif temprature>=15 and temprature <=28:
    print("Warm")
else:
    print("Hot")

#2 receipt loop

for i in range(1, 11):
    print("receipt #",i)

#3 even numbers

for i in range(1,20):
   if i%2==0:
       print(i)
#4 discount function
price=int(input("enter price:"))
def apply_discount(price,percent=0.10):
    after_discount=price-(price*percent)
    return(after_discount)
print(apply_discount(price,0.10))
#5 count down
number=5
while number>0:
    print(number)
    number-=1
print("lift off!") 