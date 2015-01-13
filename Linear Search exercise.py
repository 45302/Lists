#Alexander Allan
#13/01/2015
#Linear Search

#Function(s).
def LinearSearch(Search_List,Search_Item):
    SearchedValue = 0
    Found = False
    while not Found and SearchedValue < len(Search_List):
        if Search_Item == Search_List[SearchedValue]:
            Found = True
            print("Found.")
        else:
            SearchedValue = SearchedValue + 1
    return Found

#Information needed.
Search_List = ["A","B","C","D","E","F"]

#Main Program.
Search_Item = input("Enter the item you are looking for: ")
Found = LinearSearch(Search_List,Search_Item)
if Found == False:
    print("Not found.")
