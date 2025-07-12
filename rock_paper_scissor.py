import random

class Game:     # CLASS

    def __init__(self):     
        self.dict = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}
        self.U, self.C = 0,0              ## USER & COMPUTER SCORE


    def scoreboard(self):       ## SCOREBOARD
        print(f'''
|========= SCOREBOARD =========|
|            ||                |
|     YOU    ||   COMPUTER     |
|------------------------------|              
|     {self.U}      ||      {self.C}         | 
|------------------------------|
''')


    def winner(self, user, ai):     ## DETERMINING WINNER
        print(f"\nYou chose: {self.dict[user]} 👤")
        print(f"Computer chose: {self.dict[ai]} 🖥️")        
        if user == ai:
            print("Draw. No gain from both sides. ⚖️\n")

        elif (user == 1 and ai == 3) or (user == 2 and ai == 1) or (user == 3 and ai == 2):
            print("GREAT!! You Win. Keep it up. 👤✅\n")
            self.U += 1

        else:
            print("Computer Win. Hard Luck. Good Luck next time. 🖥️✅\n")
            self.C += 1



obj = Game()        ## OBJECT

round = 1           ## INITIATING ROUND

## GAME STARTS
print('''                           
====    ROCK    ====🪨
====    PAPER   ====📃
====   SCISSOR  ====✂️
====     CUT    ====    

        Let's Play  🚀
      
    (+1 point for each win)
''')

while True:
    try:
        c = int(input(f'''
Press 1 for "Rock"      🪨  

Press 2 for "Paper"     📃

Press 3 for "Scissor"   ✂️
                      
ROUND {round} :
---------------------------
                      
Enter your choice here 👉:     '''))              ## INPUT
        
        if c not in obj.dict.keys():
            print("Given input not in the game. Try again!! ❌\n")
            continue

        else:
            x = random.randint(1,3)
            obj.winner(c, x)
            print(f"TILL ROUND {round} :")
            obj.scoreboard()
            r = int(input('''
Do you want to continue:
(Press 1 for Yes & 2 for No) 👉:   '''))
            
            print("=" * 40, "\n")
            
            if r == 1:
                round += 1                  ## IF YES, NEXT ROUND STARTS
            
            elif r == 2:
                if obj.U > obj.C:
                    print("Looks like you won. GREAT!!🏆")
                elif obj.U < obj.C:
                    print("Looks like computer won. Better LUCK next time.🫡")
                
                print("Thanks for playing. Have a good day. 😊\n")         ## ELSE, GAME EXITS
                break
                
            else:
                print("Invalid. Exiting the game. ❌")
                break

    except:
        print("Given input not in the game. Try again!! ❌\n")             ## INVALID INPUT