from MasterIndex import *

#shoppingLst is currently has placeholder values for testing. It should normally be empty when initialized.
shoppingLst = ["Buns", "Milk", "Apples", "Pork Chops"]

def fitness(item):
    return categoryOrderDict[itemCategoryDict[item]]

while True:

    #add the user's inputted shopping list item to shoppingLst
    addItem = input("Please enter your shopping list items here (when finished, enter DONE): ")
    
    if addItem != "DONE":
        shoppingLst.append(addItem)
    else:
        print("Your shopping list contains: ")
        shoppingLst.sort(key=fitness)
        for items in shoppingLst:
            print(items)
        break 
        


'''# NOT DONE: function that sorts items in shoppingLst so that items are optimized based on store layout
def storeSort(shoppingLst):

   #convert shoppingLst into a dictionary using lstToDctConvert()
    lstToDctConvert(shoppingLst)

    #just checking that the dict converter actually works (it does)
    print(shoppingLst)

    #iterate through the new shopping list dictionary, and check if each key is the same (or exists) compared to the masterIndexDict
    for key in shoppingLst:
        match = True
        if not key in masterIndexDct:
            match = False
    return '''
