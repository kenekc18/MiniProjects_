print("Lets play a game")
variable = ["Rock","Paper","Scissor"]
print(variable)
while True:
       u1 = input("User1 pick a variable:")
       u2 = input("User2 pick a variable:")

       if u1 == u2:
              print("It's a tie")
       elif u1 == "Rock" and u2 == "Paper":
              print("Congratulations user2 you won")
       elif u1 == "Paper" and u2 == "Rock":
              print("Congratulations user1 you won")
       elif u1 == "Scissors" and u2 == "Paper":
              print("Congratulations user1 you won")
       elif u2 == "Scissors" and u1 == "Paper":
              print("Congratulations user2 you won")
       elif u2 == "Rock" and u1 == "Scissors":
              print("Congratulations user2 you won")
       elif u2 == "Scissors" and u1 == "Rock":
              print("Congratulations user1 you won")

      

