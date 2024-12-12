import csv
username = ""
password = ""
balance = 0

with open("atm_data.csv", "r") as file:
    reader = csv.DictReader(file)
    data = [line for line in reader]

def auth():
    global username, password, balance
    user_acc = str(input("Type account name: ")).strip().lower()
    user_pass = str(input("Type account pincode: ")).strip().lower()
    for item in data:
        if user_acc == item["username"] and user_pass == item["password"]:
            username = user_acc
            password = user_pass
            balance = float(item["balance"])
            print("Current Balance: ",balance)
            return True
    print("Authentication Failed.")
    return False

def update_balance():
    for item in data:
        if username == item["username"]:
            item["balance"] = str(balance)
    with open("atm_data.csv", "w", newline="") as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


authorisation = auth()

if authorisation:
    user_action = str(input("Would you like to 'withdraw' or 'deposit' money?: ")).lower().strip()
    try:
        user_amount = float(input(f"Type the amount to {user_action}: "))
    except ValueError:
        print("Invalid amount.")
        exit()
    if user_action == "withdraw":
        if user_amount > balance:
            print("Insufficient Funds.")
        else:
            balance -= user_amount
            print(f"Withdraw completed. Current balance is {balance}.")
            update_balance()
    elif user_action == "deposit":
        balance += user_amount
        print(f"Deposit completed. Current balance is {balance}.")
        update_balance()
    else:
        print("Invalid Action")