# Here is the initiation of the array where we are going to append the information in music_info.txt.
musicdb = []
with open("Music_Info.txt", "r") as f:
    f.readline()
    for line in f:
        s = line.strip()
        musicdb.append(list(s.split("|")))

# Outputting the array to check for the available rental music
##print(musicdb)

# Here is the intial menu page for the user where they can search for the music by artist, genre, medium and title which they would like to rent
def display_menu():
    print("Press (a) to search music records by Artist")
    print("Press (t) to search music records by Title")
    print("Press (m) to search music records by Medium")
    print("Press (g) to search music records by Genre")
    print("Press (q) to quit the program")

# Searching for the array musicdb by artist
def getArtist():
    while True:
        sArtist = input("\nWhich Artist are you looking for?: ").strip()
        
        if sArtist == "":
            print("Please enter an Artist name.")
            continue
        
        found = False
        for i in range(len(musicdb)): 
            if len(musicdb[i]) > 1 and musicdb[i][1].lower() == sArtist.lower():
                found = True
                print("[RecordID =", musicdb[i][0],
                    "|Artist =", musicdb[i][1],
                    "|Title =", musicdb[i][2],
                    "|Medium =", musicdb[i][3],
                    "|Genre =", musicdb[i][4],
                    "|Availability =", musicdb[i][6] + "]")

## loops until found else it will loop until customer enters an artist.        
        if found:
            break
        else:
            print("No records found for this artist. Please try again.\n")
            break 
            

# Searching for the array musicdb by genre
def getGenre():
    while True:
        sGenre = input("\nWhat Genre are you looking for?: ").strip()
        
        if sGenre == "":
            print("Please enter a Genre.")
            continue
        
        found = False
        for i in range(len(musicdb)): 
            if len(musicdb[i]) > 1 and musicdb[i][4].lower() == sGenre.lower():
                found = True
                print("[RecordID =", musicdb[i][0],
                    "|Artist =", musicdb[i][1],
                    "|Title =", musicdb[i][2],
                    "|Medium =", musicdb[i][3],
                    "|Genre =", musicdb[i][4],
                    "|Availability =", musicdb[i][6] + "]")

## loops until found else it will loop until customer enters a genre.        
        if found:
            break
        else:
            print("No records found for this genre. Please try again.\n")
            

# Searching for the array musicdb by medium
def getMedium():
    while True:
        sMedium = input("\nWhat Medium are you looking for?: ").strip()
        
        if sMedium == "":
            print("Please enter a Medium.")
            continue
        
        found = False
        for i in range(len(musicdb)): 
            if len(musicdb[i]) > 1 and musicdb[i][3].lower() == sMedium.lower():
                found = True
                print("[RecordID =", musicdb[i][0],
                    "|Artist =", musicdb[i][1],
                    "|Title =", musicdb[i][2],
                    "|Medium =", musicdb[i][3],
                    "|Genre =", musicdb[i][4],
                    "|Availability =", musicdb[i][6] + "]")

## loops until found else it will loop until customer enters a medium.        
        if found:
            break
        else:
            print("No records found for this Medium. Please try again.\n")
            

# Searching for the array musicdb by title
def getTitle():
    while True:
        sTitle = input("\nWhat Title are you looking for?: ").strip()
        
        if sTitle == "":
            print("Please enter a Title.")
            continue
        
        found = False
        for i in range(len(musicdb)): 
            if len(musicdb[i]) > 1 and musicdb[i][2].lower() == sTitle.lower():
                found = True
                print("[RecordID =", musicdb[i][0],
                    "|Artist =", musicdb[i][1],
                    "|Title =", musicdb[i][2],
                    "|Medium =", musicdb[i][3],
                    "|Genre =", musicdb[i][4],
                    "|Availability =", musicdb[i][6] + "]")

## loops until found else it will loop until customer enters a title.        
        if found:
            break
        else:
            print("No records found for this Title. Please try again.\n")
            

# Here is the function where each function is outputted which is determined by the customer's input
def SearchMusic():
    ## loading the menu to select how to search.
    display_menu()    
    option = input("\nPlease select an option displayed above: ").lower()
    if option == "a":
        getArtist()
        ## if user likes any of the records, they can continue to rent the searched music records.
        value = input("\nWould you like to rent any of these music records? [y/n]: ").lower()
        if value == 'y':
            return value
        elif value == 'n':
           ## loops back to search main menu to allow constant searching.
           print("Redirecting back to musicSearch...\n")
           SearchMusic()
        else:
            print("Invalid option, please try again.\n")
            SearchMusic() 
    elif option == "t":
        getTitle()
        value = input("\nWould you like to rent any of these music records? [y/n]: ").lower()
        if value == 'y':
            return value
        elif value == 'n':
           print("Redirecting back to musicSearch...\n")
           SearchMusic()
        else:
            print("Invalid option, please try again.\n")
            SearchMusic() 
    elif option == "m":
        getMedium()
        value = input("\nWould you like to rent any of these music records? [y/n]: ").lower()
        if value == 'y':
            return value
        elif value == 'n':
           print("Redirecting back to musicSearch...\n")
           SearchMusic()
        else:
            print("Invalid option, please try again.\n")
            SearchMusic() 
    elif option == "g":
        getGenre()
        value = input("\nWould you like to rent any of these music records? [y/n]: ").lower()
        if value == 'y':
            return value
        elif value == 'n':
           print("Redirecting back to musicSearch...\n")
           SearchMusic()
        else:
            print("Invalid option, please try again.\n")
            SearchMusic()         
    elif option == "q":
        ## back to main menu.
        print("You have exited Music Search.")
        return option
    else:
        print("Invalid option selected, please try again.\n")
        SearchMusic()