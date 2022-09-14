import pyperclip, string, random, os, sys
from colorama import Fore, Style

#########  EDIT ME ##########
PLAIN_TEXT_PASSWORD = True  # Display the generated password in plain text
ONLY_USER           = False # Only generate user
USER_LEN            = 10    # Username Lenght
PASS_LEN            = 20    # Password Lenght
#############################

USER_CHARS = string.ascii_letters + string.digits
PASS_CHARS = string.ascii_letters + string.digits + string.punctuation

# Check args. For some weird ass python scope reason doesnt work inside a function or inside main
if len(sys.argv) > 1:
    if sys.argv[1] == "--help":
        print(f"Usage:\n\t{sys.argv[0]} --hidden\n\t{sys.argv[0]} [user_len] [pass_len]")
        exit(1)
    elif sys.argv[1] == "--hidden":
        PLAIN_TEXT_PASSWORD = False
    else:
        USER_LEN = int(sys.argv[1])

        if len(sys.argv) > 2:
            PASS_LEN = int(sys.argv[2])
        else:
            ONLY_USER = True        # If we only have args for user, ignore password. Just personal preference

def success_text(text1, text2):
    print(f"{Style.RESET_ALL} {Style.BRIGHT}[{Fore.GREEN}+{Style.RESET_ALL}{Style.BRIGHT}] {Fore.GREEN}{text1}{Style.RESET_ALL}{Style.BRIGHT}{text2}{Style.RESET_ALL}")

def info_text(text):
    print(f"{Style.RESET_ALL} {Style.BRIGHT}[{Fore.BLUE}i{Style.RESET_ALL}{Style.BRIGHT}] {Fore.BLUE}{text}{Style.RESET_ALL}")

def info_input(text):
    try:
        input(f"{Style.RESET_ALL} {Style.BRIGHT}[{Fore.BLUE}i{Style.RESET_ALL}{Style.BRIGHT}] {Fore.BLUE}{text}{Style.RESET_ALL}")
    except KeyboardInterrupt:
        if ONLY_USER:
            error_text("Ctrl+C detected. Exiting...")
        else:
            error_text("Ctrl+C detected. Clearing clipboard and exiting...")
            pyperclip.copy("") 
        exit(1)

def error_text(text):
    print(f"\n{Style.RESET_ALL} {Style.BRIGHT}[{Fore.RED}!{Style.RESET_ALL}{Style.BRIGHT}] {Fore.RED}{text}{Style.RESET_ALL}\n")
    exit(1)


# Checking that variabes are ok
def checkTypes():
    if type(PLAIN_TEXT_PASSWORD) is not bool:
        errorText("The variable PLAIN_TEXT_PASSWORD is not a bool.")
    if type(ONLY_USER) is not bool:
        errorText("The variable ONLY_USER is not a bool.")
    if type(USER_LEN) is not int:
        errorText("The variable USER_LEN is not a bool.")
    if type(PASS_LEN) is not int:
        errorText("The variable PASS_LEN is not a bool.")

def main():
    checkTypes()
    print()

    # Username
    username = "".join(random.choice(USER_CHARS) for i in range(USER_LEN))
    success_text(f"Username generated with {USER_LEN} characters: ", username)
    pyperclip.copy(username)

    # If we only care about the username
    if ONLY_USER:
        info_text("Username copied to clipboard. User only mode, exiting...")
        exit(0)

    info_input("Username copied to clipboard. Press any key to generate the password...")

    # Password
    password = "".join(random.choice(PASS_CHARS) for i in range(PASS_LEN))
    if PLAIN_TEXT_PASSWORD:
        success_text(f"Username generated with {PASS_LEN} characters: ", password)
    else:
        success_text(f"Username generated with {PASS_LEN} characters: ", "*" * PASS_LEN)

    # Copy to clipboard using pyperclip
    pyperclip.copy(password)
    info_input("Password copied to clipboard. Press any key to empty the clipboard and exit the program...")
    pyperclip.copy("")
    exit(0)

main()
