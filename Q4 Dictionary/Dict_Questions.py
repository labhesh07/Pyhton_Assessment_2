#Create a dictioanry specifying name and age of your friend
friend_info={}
num = int(input("How many friends you want to add :"))
for i in range(num):
    name = input(f"Enter friend {i+1} name :")
    age = int(input(f"Enter age of {i+1} friend :"))
    score = float(input(f"Enter score of {i+1} friend :"))


    friend_info[name]={"age" :  age ,
                       "score" : score }

print(friend_info)

# Update score code
while True :
    option = int(input("Do you want to update score of any person. Enter 1 for Yes and 2 for No"))
    if option == 2 :
        exit
    elif option == 1 :
        Update_name = input("Enter name of student")
        if Update_name in friend_info :
            print("<-- Name Found -->")
            update_score = int(input("Enter the updated score"))
            friend_info[Update_name]["score"]=update_score
            print(friend_info)
        else :
            print("Name Not Found")
    else:
        print("Invalid Input ! Please Enter The Specified Input ")

