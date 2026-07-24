# question 1
def getOnlyEven(arr):
    result=[]
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
            result.append(arr[i])
    print(result)
getOnlyEven([1,2,3,6,4,8])
getOnlyEven([0,1,2,3,4])    
# question 2
def reverseCompare(num):
    reversed_num = int(str(num)[::-1])
    if num > reversed_num:
       print("ok")
    else:
       print("Not ok")
reverseCompare(72)
reverseCompare(23)
# question3
def recursion(num):
    if num==0:
        return 1
    else:
        return num*recursion(num-1)
print(recursion(5))
print(recursion(6))
print(recursion(0))
#question 4
def checkMeera(arr):
    for n in arr:
        if n * 2 in arr:
            print("I am NOT a Meera array")
            return
    print("I am a Meera array")

checkMeera([10, 4, 0, 5])
checkMeera([7,4,9])
checkMeera([1,-6,4,-3])
#question 5

def isDual(arr):
    for x in arr:
        if arr.count(x) != 2:
            return 0
    return 1
first = isDual([2,6,4,6,7,4,2,7])
second = isDual([5,8,7,7,8])
print(first)
print(second)
#question 6
def Clock(sec):
    hr = (sec // 3600) % 24
    min = (sec % 3600) // 60
    secs = sec % 60
    return f"{hr:02}:{min:02}:{secs:02}"
print(Clock(61201))   
print(Clock(87000)) 
print(Clock(5025))
