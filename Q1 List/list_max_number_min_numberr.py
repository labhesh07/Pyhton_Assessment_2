num = int(input("Enter number of elements :"))
list= []
for i in range(0 , num):
    element=int(input(f"Enter {i+1}" " Element : "))
    list.append(element)

print("Maximum element in List is : ", end="")
print(max(list))

print("Minimum element in List is : ", end="")
print(min(list))