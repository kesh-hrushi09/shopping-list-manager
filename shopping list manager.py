print(f"--- Shopping List---" )
print(f"1. Add an item" )
print(f"2. Remove an item" )
print(f"3. View the list" )
print(f"4. Count items" )
print(f"5. Quit" )

user = int(input("enter an action: "))
lists = []

while user != 5:
    if user == 1:
        shopping = input("enter an ingredient: ")
        if shopping in lists:
            print("item alreadys exists")
        lists.append(shopping)
    elif user == 2:
        item = input("enter an item to remove:")
        if item in lists:
            lists.remove(item)
        else:
            print("item is not in the list")
    elif user == 3:
        print(lists)
    elif user == 4:
        c = len(lists)
        print(c)
    else:
        print("invalid choice")
        break
    
    user = int(input("enter an action"))