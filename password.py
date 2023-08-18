import random
import string_utils

def main():
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

    digits_in = int(input("Enter the number of digits you want : "))
    symbols_in = int(input("Enter the number of symbols you want : "))
    locase_in = int(input("Enter the number of lowercase alphabets you want : "))
    upcase_in = int(input("Enter the number of uppercase you want : "))

    def create():
        password = ""

        for digits in range(digits_in):
            gen_digits = str(random.choice(DIGITS))
            password += gen_digits

        for symbols in range(symbols_in):
            gen_symbols = str(random.choice(SYMBOLS))
            password += gen_symbols

        for ucase in range(upcase_in):
            gen_ucase = random.choice(UPCASE_CHARACTERS)
            password += gen_ucase

        for locase in range(locase_in):
            gen_locase = random.choice(LOCASE_CHARACTERS)
            password += gen_locase

        generated_password = string_utils.shuffle(password)
        print(generated_password)

    create()
    
if __name__ == "__main__":
    main()