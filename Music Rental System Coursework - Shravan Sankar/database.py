## importing all cells into database
import musicSearch as ms
import musicRent as mr
import InventoryPruning as ip
import musicReturn as mcr
import datetime as dt

## assigning all text files into a variable
subscription = "Subscription_Info.txt"
music = "Music_Info.txt"
rental = "Rental.txt"
feedback = "Music_Feedback.txt"

## used to create a new customer id for new customers creating an account for the rental store.
def register():
        new_id = input("Enter a new customer ID (4 alphabetical letters): ").strip()
        if len(new_id) != 4 or not new_id.isalpha():
            print("Error: Customer ID must be exactly 4 alphabetical letters. Please try again.")
            register()
        else:
            ## ensures a loop to disallow invalid inputs.
            while True:
                subscription_type = input("Enter subscription type (Basic includes 3 months of 2 rentals or enjoy Premium which includes 3 months of 7 rentals): ").strip()
                if subscription_type not in ["Basic", "Premium"]:
                    print("Invalid subscription type. Please enter either 'Basic' or 'Premium'.")
                    continue
                else:
                    start_date = dt.date.today()
                    if subscription_type == "Basic":
                        ## generically set to 3 months but rental limit changes depending on subscription type.
                        end_date = start_date + dt.timedelta(days=90)
                    elif subscription_type == "Premium":
                        end_date = start_date + dt.timedelta(days=90)
                    with open(subscription, "a") as sub:
                        sub.write(f"{new_id},{subscription_type},{start_date.strftime('%Y-%m-%d')},{end_date.strftime('%Y-%m-%d')}\n")
                    
                    print(f"New Customer ID: '{new_id}' has successfully registered with a '{subscription_type}' subscription.")
                    print(f"Your subscription will expire on {end_date.strftime('%Y-%m-%d')}.")
                    ## allows new customer ids to view their account after registration.
                    return new_id, subscription_type
                    


## guarantees that customers will be able to view their account before making a decision in the rental system.
def viewData(subscription_file="Subscription_Info.txt", customer_id=None):
    if customer_id is None:
        customer_id = input("Please enter your customer ID: ").strip().lower()
        
        with open(subscription_file, "r") as file:
            found = False
            for line in file:
                data = line.strip().split(",")
                if data[0] == customer_id:
                    print(f"Here are your details:\n"
                          f"\nCustomer ID: {data[0]}\n"
                          f"Subscription Type: {data[1]}\n"
                          f"Start Date: {data[2]}\n"
                          f"End Date: {data[3]}")
                    found = True
                    break
            if not found:
                print("Customer ID not found. Redirecting to registration...")
                new_id = register()
                viewData(subscription_file, customer_id=new_id)


## the main function of the program where customer can choose what they want to do.
def mainMenu():
    ## ensures that customer always returns to main menu after breaking from any function.
    while True:
            print("___________________________")
            print("\n---*Search* Music Records---\n---*Rent* Music Records---\n---*Return* Music Records---\n---*Statistics*---\n---*Exit*---\n")
            print("___________________________\n")
            opt = input("Please choose an option: ").strip().lower()

            if opt in ["search", "rent", "return", "statistics", "exit"]:
                return opt
            else:
                print("Invalid option. Please choose from the available options.")


                    ###___main menu___###

## viewing their data before they can choose a decision.
viewData()

## the main program of the rental system where most decisions caused by customer will determine the output.
def main():
    while True:
        value = mainMenu()
        if value == 'search':
            result = ms.SearchMusic()
            if result == 'y':
                mr.checkSubscription()
        elif value == 'rent':
            mr.checkSubscription()
        elif value == 'return':
            mcr.returnMusic()
        elif value == 'statistics':
            ip.checkRentalDist()
        elif value == 'exit':
            print("You have exited the program, goodbye.")
            break
        else:
            print("Invalid option, please try again\n")



### running the music store management rental system program ###

main()