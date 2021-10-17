from datetime import datetime
import locale
import random
import string
import colorama
from colorama import Fore, Back, Style
colorama.init()
locale.setlocale(locale.LC_ALL, "")


print("\n\t\t\t\t\t ____                 ____               ")
print("\t\t\t\t\t|  _ \ ___ _ __   ___|  _ \ __ _ ___ ___ ")
print("\t\t\t\t\t| |_) / _ \ '_ \ / _ \ |_) / _` / __/ __|")
print("\t\t\t\t\t|  __/  __/ |_) |  __/  __/ (_| \\__ \\__ \\")
print("\t\t\t\t\t|_|   \___| .__/ \___|_|   \__,_|___/___/")
print("\t\t\t\t\t          |_|                            ")
print("\t\t\t\t\t\t\tVersion 2.0")
print("\t\t\t\t\t\tAuthor: github.com/PepeLab\n" )
print("\t\t\t\t\t-----------------------------------------\n")


#==========================VARIABLES===========================#
UP = string.ascii_uppercase
LOW = string.ascii_lowercase
NUMBERS = string.digits  
SPECIAL = string.punctuation

chars = ""
chars_len = False
password = ""
password_list = []

day = datetime.now()
#==========================VARIABLES===========================#


#===========================PROGRAM============================#
while True:
    length = int(input("\t\t\t\t\t[+] Password Length » "))
    use_low = input("\t\t\t\t\t[+] Use lowercase letters? » ")
    use_up = input("\t\t\t\t\t[+] Use uppercase letters? » ")
    use_num = input("\t\t\t\t\t[+] Use numbers? » ")
    use_spec = input("\t\t\t\t\t[+] Use special characters? » ")
    number_of_pass = int(input("\t\t\t\t\t[+] Number of passwords » "))
    print("")
    
    if use_low == "y":
        chars += LOW
        chars_len = True
    
    if use_up == "y":
        chars += UP
        chars_len = True
    
    if use_num == "y":
        chars += NUMBERS
        chars_len = True
    
    if use_spec == "y":
        chars += SPECIAL
        chars_len = True
    
    #==========================GENERATION==========================#
    if chars_len == True:
        for i in range(number_of_pass):
            for i in range(length):
                password += random.choice(chars)
                number_of_pass -= 1
                
            if length <= 6:
                print(Fore.RED + "\t\t\t\t\t" + password + Style.RESET_ALL)
            elif length <= 9:
                print(Fore.YELLOW + "\t\t\t\t\t" + password + Style.RESET_ALL )
            else:
                print(Fore.GREEN + "\t\t\t\t\t" + password + Style.RESET_ALL )
                
            password_list.append(password)
            password = ""
            
        #Saving file with password   
        pass_save = input("\n\t\t\t\t\t[+] Save? » ")
        if pass_save == "y":
            with open("passwords.txt", "a") as file:
                file.write("\n================ " + day.strftime("%d %B %Y / %I:%M") + " ================\n")
                for item in password_list:
                    file.write("%s\n" % item)
            file.close()
        
        chars = ""
        password_list.clear()
        chars_len = False
        print("\n\t\t\t\t\t-----------------------------------------\n")
    else:
        print("\t\t\t\t\t¯\(°_o)/¯ OOPS!")
        print("\n\t\t\t\t\t-----------------------------------------\n")

    #==========================GENERATION==========================#
    
#===========================PROGRAM============================#