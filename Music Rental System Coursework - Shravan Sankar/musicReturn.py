import feedbackManager as fm
import datetime as dt

# Ensures that the date added to the text files are the correct dates
# Disallows dates such as 30th Feb and 31st Nov, etc.
def is_valid_date(date_str, date_format="%Y-%m-%d"):
    dt.datetime.strptime(date_str, date_format)

# Takes in 3 parameters of all the text files required to return the music record.
def returnMusic(subscriptions_file="Subscription_Info.txt", music_file="Music_Info.txt", rental_file="Rental.txt"):
    customer_id = input("Please enter your customer ID for returning your music record: ")
    music_record = input("Please enter the music record ID you would like to return: ")

    # Reads the rental.txt and verifies that the music record has been rented and the customer ID is valid.
    with open(rental_file, "r") as rent_file:
        rent_lines = rent_file.readlines()

    rental_valid = False
    for i, line in enumerate(rent_lines):
        fields = line.strip().split("|")
        if len(fields) < 4:
            print(f"Error: Invalid rental data format: {line}")
            return

        record_id, rental_date, return_date, rental_customer_id = fields[0], fields[1], fields[2], fields[3]
        if record_id == music_record and rental_customer_id == customer_id:
            if return_date and return_date.strip():  # Check if return_date is not empty or just spaces
                if dt.datetime.strptime(return_date.strip(), "%Y-%m-%d").date() < dt.date.today():
                    print("Music record cannot be returned as it is past the due date and has already been returned.")
                    return

            # Update the return date to today's date
            rent_lines[i] = f"{record_id}|{rental_date}|{dt.date.today().strftime('%Y-%m-%d')}|{rental_customer_id}\n"
            rental_valid = True
            break

    if not rental_valid:
        print("Customer ID does not belong to this music record, please try again.")
        return

    with open(rental_file, "w") as rent_file:
        rent_file.writelines(rent_lines)

    # Verifies that the customer ID is also part of the subscription.
    with open(subscriptions_file, "r") as sub_file:
        sub_file.readline()
        valid_customer = False
        for line in sub_file:
            fields = line.strip().split(",")
            if len(fields) < 4:
                print(f"Invalid subscription data format: {line}")
                return

            sub_customer_id, sub_end_date = fields[0], fields[3]
            if sub_customer_id == customer_id:
                if dt.date.today() > dt.datetime.strptime(sub_end_date, "%Y-%m-%d").date():
                    print("Music Record has already been returned as your subscription has expired. Please renew your subscription.")
                    return
                valid_customer = True
                break

        if not valid_customer:
            print("Invalid customer ID, please try again.")
            return

    with open(music_file, "r") as music:
        music_lines = music.readlines()

    # Ensuring that the music record has been rented first before it can be returned.
    record_found = False
    for i, line in enumerate(music_lines):
        record = line.strip().split("|")
        if music_record == record[0]:
            record_found = True
            if record[-1] != "Unavailable":
                print("Error: This music record is not currently rented out.")
                return

            record[-1] = "Available"
            record[5] = "N/A"
            music_lines[i] = "|".join(record) + "\n"
            break

    if not record_found:
        print("Music record not found.")
        return

    with open(music_file, "w") as music:
        music.writelines(music_lines)

    print("Music record has been successfully returned.")
    collectFeedback(customer_id, music_record)
    return True

# Passes the two variables from returnMusic() and collects the feedback.
def collectFeedback(customer_id, music_record):
    while True:
        feedback_list = fm.load_feedback()
        star_rating = input("Please enter a star rating from 1 to 5 of the music record(s) you have rented previously: ").strip()
        if star_rating.isdigit() and 1 <= int(star_rating) <= 5:
            star_rating = int(star_rating)
            comments = input("Please enter optional comments about your experience (press Enter to skip): ").strip()
            fm.add_feedback(f"{music_record}", f"{star_rating}", f"{comments}", "Music_Feedback.txt")
            print("Thank you for your feedback!")
            break
        else:
            print("Please enter a star rating with the range 1-5.")
