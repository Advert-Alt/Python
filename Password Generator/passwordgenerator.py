import string
import secrets

def generate_password(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits
    
    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)

    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

print("=====================================PASSWORD LIST===========================================")

password_list = [generate_password(length=24, symbols=True, uppercase=True) for _ in range(10)]

for _, i in enumerate(range(10)):
    print(i + 1, ":", password_list[i])

print("======================================YOUR CHOICE=============================================")

print("Which password do you want to use? (1-10)")
choice = int(input())

if 1 <= choice <= 10:
    print("You have chosen password number", choice)
    pass_choice = password_list[choice - 1]
    add_information = input("Saved for account: ")

    with open("passwords.txt", "a") as file:
        file.write(f"{add_information} : {pass_choice}\n")
        
        print("Password saved:", pass_choice)
else:
        print("Invalid choice. Please choose a number between 1 and 10.")
print("===========================================END=================================================")
