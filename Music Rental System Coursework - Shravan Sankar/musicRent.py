import subscriptionManager as sm
from datetime import date
import musicReturn as mcr

## passed parameter of subscription txt file and used to check if the customer id is valid with a subscription type else print error.
def checkSubscription(subscriptions_file="Subscription_Info.txt"):
    subscriptions = sm.load_subscriptions()
    customer_id = input("Please enter your customer ID for renting a music record: ").strip().lower()
    with open(subscriptions_file, "r") as file:
        file.readline()  # Skip header line
        for line in file:
            sub = line.strip().split(",")
            ## checking and verifying the length of each element in the line and customer id is checked against the first element which allows to display sub type as well.
            if len(sub) > 1 and sub[0] == customer_id and sm.check_subscription(customer_id, subscriptions):
                print(f"Customer ID found. Subscription type: {sub[1]}")
                updateRental(customer_id, sub[1])
                return
        print("Customer ID not found, please try again.")
        return False


## used to create the initial transaction log by appending and deleting elements in the text files
def updateRental(customer_id, subscription_type):
    # Initialize limit and validate subscription type
    if subscription_type == "Basic":
        limit = 2
    elif subscription_type == "Premium":
        limit = 7
    else:
        print("Invalid subscription type.")
        return

    # Check if the limit is properly set
    if limit == 0:
        print("Invalid subscription type.")
        return

    # Open music and rental files
    with open("Music_Info.txt", "r") as music_file:
        music_lines = music_file.readlines()

    with open("Rental.txt", "r") as rental_file:
        rental_lines = rental_file.readlines()

    # Calculate the number of records already rented by the customer
    rented_count = sum(1 for line in rental_lines if line.strip().split("|")[-1] == customer_id)

    while rented_count >= limit:
        value = mcr.returnMusic()
        if value == True:
            rented_count -= 1
            break
        else:
            print(f"Rental limit reached. You can rent up to {limit} music records with your subscription.")
            return  

    # Allow customer to rent music records until their rental limit is reached
    while rented_count < limit:
        rental = input(f"What music record would you like to rent? (Remaining Rentals: {limit - rented_count}): ").strip()

        # Find and rent the music record
        music_record_found = False
        for i, line in enumerate(music_lines):
            music_record = line.strip().split("|")
            if rental == music_record[0]:
                music_record_found = True
                if music_record[-1] == "Available":
                    music_record[-1] = "Unavailable"
                    current_date = date.today()
                    music_record[-2] = current_date.strftime("%Y-%m-%d")

                    music_lines[i] = "|".join(music_record) + "\n"
                    rented_count += 1

                    with open("Rental.txt", "a") as rental_file:
                        rental_file.write(f"{rental}|{current_date.strftime('%Y-%m-%d')}|         |{customer_id}\n")

                    with open("Music_Info.txt", "w") as music_file:
                        music_file.writelines(music_lines)

                    print("Music record rented successfully.")
                    break
                else:
                    print("Music is already rented.")
                    break

        if not music_record_found:
            print("Music record not found, please try again.")

        if rented_count < limit:
            more_rentals = input(f"Would you like to rent another record? (You can still rent {limit - rented_count} more) [y/n]: ").strip().lower()
            if more_rentals != 'y':
                break

    if rented_count == limit:
        print("You have reached your rental limit.")
