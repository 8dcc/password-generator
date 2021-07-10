import pyperclip, string, random, os, sys
from colorama import Fore, Style

########  EDIT ME #########
PlainTextPassword = True  # Display the generated password in plain text
UsernameLenght = 10       # Username Lenght
PasswordLenght = 20       # Password Lenght
###########################

if len(sys.argv) is 3:
    UsernameLenght = int(sys.argv[1])
    PasswordLenght = int(sys.argv[2])

UsernameCharacters = string.ascii_letters + string.digits
PasswordCharacters = string.ascii_letters + string.digits + string.punctuation

def SuccessText(text1, text2):
    print(f"{Style.RESET_ALL} {Style.BRIGHT}[{Fore.GREEN}+{Style.RESET_ALL}{Style.BRIGHT}] {Fore.GREEN}{text1}{Style.RESET_ALL}{Style.BRIGHT}{text2}{Style.RESET_ALL}")
def InfoText(text):
    print(f"{Style.RESET_ALL} {Style.BRIGHT}[{Fore.BLUE}i{Style.RESET_ALL}{Style.BRIGHT}] {Fore.BLUE}{text}{Style.RESET_ALL}")
def InfoInput(text):
    input(f"{Style.RESET_ALL} {Style.BRIGHT}[{Fore.BLUE}i{Style.RESET_ALL}{Style.BRIGHT}] {Fore.BLUE}{text}{Style.RESET_ALL}")
def errorText(text):
    print()
    print(f"{Style.RESET_ALL} {Style.BRIGHT}[{Fore.RED}!{Style.RESET_ALL}{Style.BRIGHT}] {Fore.RED}{text}{Style.RESET_ALL}")
    print()
    exit(1)

def checkTypes():
    if type(PlainTextPassword) is not bool:
        errorText("The variable PlainTextPassword is not a bool.")
    if type(UsernameLenght) is not int:
        errorText("The variable UsernameLenght is not a bool.")
    if type(PasswordLenght) is not int:
        errorText("The variable PasswordLenght is not a bool.")

def main():
    checkTypes()
    print()

    # Username
    Username = "".join(random.choice(UsernameCharacters) for i in range(UsernameLenght))
    SuccessText(f"Username generated with {UsernameLenght} characters: ", Username)
    pyperclip.copy(Username)
    InfoInput("Username copied to clipboard. Press any key to generate the password...")

    # Password
    Password = "".join(random.choice(PasswordCharacters) for i in range(PasswordLenght))
    if PlainTextPassword:
        SuccessText(f"Username generated with {PasswordLenght} characters: ", Password)
    else:
        SuccessText(f"Username generated with {PasswordLenght} characters: ", "*" * PasswordLenght)
    pyperclip.copy(Password)
    InfoInput("Password copied to clipboard. Press any key to empty the clipboard and exit the program...")
    pyperclip.copy("")
    exit(1)

main()
