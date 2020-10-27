user1=input("Player 1 name=")
user2= input("Player 2 name=")

while True:
    user1Choice=input("Enter user1 choice").lower()
    user2Choice=input("Enter user2 choice").lower()
    print(user1Choice)
    print(user2Choice)
    if (user1Choice=='rock' and user2Choice=='scissor'):
         print("User1 win")
    elif (user1Choice=='scissor' and user2Choice=='rock'):
         print("User2 win")
    elif (user1Choice=='scissor' and user2Choice=='paper'):
         print("User1 win")
    elif (user1Choice=='paper' and user2Choice=='scissor'):
         print("User2 win")
    elif (user1Choice=='paper' and user2Choice=='rock'):
         print("User1 win")
    elif (user1Choice=='rock' and user2Choice=='paper'):
         print("User2 win")
    elif (user1Choice==user2Choice):
         print("It's a tie")
    else:
         print("wrong choice")

          repeat=input("Do you want to continue").lower()
          if(repeat=="yes"):
                pass
          else(repeat =="no"):	
                raise SystemExit
else:
      raise SystemExit 