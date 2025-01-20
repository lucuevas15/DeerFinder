##This application will allow users to find a list of 
##the 5 smallest deer species in the world

##Here is the file list for the deer species
deerSpeciesList =  ['Pudu, 7-13 inches,' , 'Pygmy Brocket, 15-20 inches,' , 'Indian Hog Deer, 14 inches,' , 'Chinese Water Deer, 18-22 inches,' , 'Truong Son Muntjac, 15 inches,' ,]

##Write the initial deer list to the file
with open('deerSpeciesList.txt', 'w') as tfile:
    tfile.write('\n'.join(deerSpeciesList))

##Open application prompt
prompt = ("******************************** \nDeer Finder v0.1 \n********************************" 
          "\nPlease Enter the your selection from the following menu: \n1. PRINT top 5 smallest deer breeds "
          "\n2. SEARCH smallest deer breeds \n3. Exit \nAll species information provided by Nature.org and Plazi.org")


##Convert all prompt elif statements to clear defined functions

##Function and statement for all deer printing
def Print_Deer_List():
    print("The top 5 smallest deer species in the world are: ")
    with open('deerSpeciesList.txt', 'r') as tfile:
        for line in tfile:
            print(f"- {line.strip()}")

##Function and statement to search for a deer
def Search_Deer_List():
    print("******************************** \nPLEASE ENTER THE DEER SPECIES NAME: ")
    searchDeer = input("").lower()  #Convert to lowercase to make search case-insensitive
    
    with open('deerSpeciesList.txt', 'r') as tfile:
        deerSpeciesList = [line.strip().lower() for line in tfile]  #Read and convert all names to lowercase
        
    # Search for partial match in the list
    matches = [species for species in deerSpeciesList if searchDeer in species]
    
    if matches:
        print(f"Found the following matches: ")
        for match in matches:
            print(f"- {match} is one of the 5 smallest deer species")
    else:
        print(f"No matches found for '{searchDeer}', try again.")


##Corrected while statement for loop      
while True:
    print(prompt)
    answer = input("select: ")

##Created If statements for user selections within prompt loop
    if answer == '1':
        Print_Deer_List()
    elif answer == '2':
        Search_Deer_List()  
 
##End application
    elif answer == '3':
        print("******************************** \nThank you for using the smallest deer species finder, good-bye!")
        break