def Large(arr,j):
    lar = arr[0]
    for j in range(1,j):
        if lar < arr[j]:
            lar = arr[j]
    
    return lar


# from array import *
arr = []
n = int(input("Enter the length of the array :"))

for i in range(n):
    x=int(input("Enter element for an array :"))
    arr.append(x)


print(arr)

ans = Large(arr,n)
print("largest element in Array is :",ans)
