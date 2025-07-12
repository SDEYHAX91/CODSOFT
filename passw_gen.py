## PASSWORD GENERATOR
import string as st
import random as r

class passw_gen:         ## CLASS

    def __init__(self):
        pass

    def create(self, n):    ## METHOD TO GENERATE PASSWORD
        if n < 4:
            print("Password length must be at least 4 to include all character types.")
            return

        ## AT LEAST PASSWORD MUST HAVE LETTERS, DIGITS AND SPECIAL CHARACTERS
        
        passw = [r.choice(st.ascii_lowercase), r.choice(st.ascii_uppercase),
                 r.choice(st.digits), r.choice(st.punctuation)]

        ## FILL THE REST WITH RANDOM COMBINATION OF LETTERS, DIGITS & OTHERS

        all_chars = st.ascii_letters + st.digits + st.punctuation
        passw += r.choices(all_chars, k = n - 4)

        r.shuffle(passw)        ## SHUFFLE

        ## JOIN
        final_pass = ''.join(passw)
        print(f"\nHere is your Generated Password: {final_pass}     \n")      ## OUTPUT


if __name__ == '__main__':      ## MAIN
    
    obj = passw_gen()       ## OBJECT

    try:
        length = int(input("\nEnter length of the required password: "))        ## INPUT LENGTH
        obj.create(length)

    except ValueError:
        print("\nPlease enter a valid integer.\n")



