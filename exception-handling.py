# 1. Try except
l1=[2,4,7,"Odisha","Chhattisgarh"]

for element in l1:
    try:
        print(element/2)
    except:
        print("element is not a number")

# 2. While Break
n=4
while n>0:
    print(n)
    n=n-1
    #print('message1')
    if n==2:
        break

print('message1')