#Audrey Ringle (revised list)
#1/18/24
#Grocery List

#Initiation
print("Welcome to your personal Grocery list")
Grocery = []

#Functions
def menu():
    for i in range(55):
        print("Please choose an option: Type in a number between 1-8")
        print("1. Add an item to the Grocery list \n2. View the current Grocery list \n3. Mark an item as complete \n4. Sort list in alphabetical order \n5. Remove an item from the Grocery list \n6. Clear entire list \n7. See how many items are on your list \n8. Quit the program")
        option=int(input("Option: "))
        if option ==1:
          newitem = input("What would you like to add?: ") 
          Grocery.append(newitem)
        
        if option==2:
            print(Grocery)
        if option == 3:
            print("Please insert a number of the item on the list, not the name of the item. Note: Item one on your list is considered 0, item 2 is considered 1, and so on.")
            completeitem = int(input("What item would you like to mark as complete?:"))
            Grocery[completeitem] = Grocery[completeitem] + " X"
        if option == 4:
            Grocery.sort()
            print("All sorted in alphabetical order! Go check your list in option 2 to view these changes.")
        if option == 5:
           print("Please insert a number of the item on the list, not the name of the item. Note: Item one on your list is considered 0, item 2 is considered 1, and so on.")
           removeitem = int(input("What would you like to remove?: "))
           Grocery.pop(removeitem)
        if option == 6:
            response=(input("Are you sure you want to delete your whole list?  Yes or No?:    "))
            if response == "Yes":
                Grocery.clear()
            if response == "No":
                print("Nothing has been cleared.")
        if option == 7:
            No_of_items = len(Grocery)
            print(No_of_items)

        if option ==8:
           print("Come back soon!")
           break
           
#Main
menu()