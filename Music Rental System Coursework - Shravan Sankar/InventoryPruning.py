import matplotlib.pyplot as plt

## compares the rental text file to music text file to check which music records have been rented so it can be distinguished between non rentals.
def checkRentalDist():
    with open("Rental.txt", "r") as rental_file:
        rental_file.readline()
        rental_lines = rental_file.readlines()
    
    with open("Music_Info.txt", "r") as music_file:
        music_file.readline()
        music_lines = music_file.readlines()

    ## takes all the music records from Music_Info.txt and compares the records in Rental.txt.
    rental_count = {line.strip().split("|")[0]: 0 for line in music_lines}

    for line in rental_lines:
        record_id = line.strip().split("|")[0]
        if record_id in rental_count:
            rental_count[record_id] += 1
    
    val = input("Would you like to see the distribution of the music records rented? [y/n]: ").strip().lower()
    if val == 'y':
        print("\nRental Distribution:")
        for record_id, count in rental_count.items():
            print(f"RecordID: {record_id}, NumofTimes Rented: {count}")
    elif val == 'n':
        return
    else:
        print("Please enter 'y' for yes or 'n' for no.")
        checkRentalDist()
        
    ## converts both records and rental values into an array so that it can be graphed.
    record_ids = list(rental_count.keys())
    rental_values = list(rental_count.values())

    ## plots the graph of the distribution of music records with some added style to ensure that it is easy to interpret.
    plt.figure(figsize=(18, 7))  
    plt.bar(record_ids, rental_values, color='skyblue')
    plt.xlabel("Record IDs", fontsize=10)
    plt.ylabel("Number of Rentals")
    plt.ylim(0, 10)
    plt.title("Distribution of Music Records")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


    ## executes removeRentals() to identify the records with the least rentals.
    remove_option = input("\nWould you like to assess whether music records with fewer rentals should be removed? [y/n]: ")
    if remove_option.lower() == 'y':
        removeRentals(rental_count)
    else: 
        return

## function being executed.
def removeRentals(rental_count):
    low_rental_records = [record_id for record_id, count in rental_count.items() if count < 3]

    ## displays the music records with fewer rentals so that the manager can remove if necessary.
    if low_rental_records:
        print("\nRecords to be removed due to low rentals:")
        for record_id in low_rental_records:
            print(f"RecordID: {record_id}")