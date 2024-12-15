name = input("Hi I am compbot. What's your name?")
print("Hello" , name)
game = input("Do you wnat to play a game?")
if game == "Yes":
    print("Yay!Let's start!")
else:
    print("Oh man!Well guess what? I don't care! Your playing it anyway cause I'm bored 👿!" )
chocolate = "Cadbury"
newchocolate = input("I'm going to read your mind. Name any chocolate")
if newchocolate == chocolate:
    print("Yes! I'm officially a mind reader😀 Wow! Looks like I have a superpower 😜")
else:
    print("Oh! I was for sure I could read your mind. Great1 I lost😔")
print("Here's another game just for fun 😜")
import random
computer = random.randint(1,3)
user = int(input("Enter your choice:\n1 = rock\n2 = paper\n3 = scissors\n"))
if computer == user:
    print("It's a tie game.")
elif computer == 1 and user == 3:
    print("Computer wins!")
elif computer == 2 and user ==1:
    print("Computer wins again!")
else:
    print("You win!")
newgame = input("How about another game?")
if newgame == "Yes" :
    print("Yay!Let's start!")
else:
    print("I don't care! Let's play it anyway 😒")

print("Th game is where I give you a lyric and you have to guess the song")
song = (input("The first bit of the song is, 'For now the day bleeds, into night fall'"))
if song == "Someone you loved" :
    print("Yay!You got it right!")
elif song == "Idk" or "I don't know" :
    print("Oh! The song was someone you loved! It's okay! Better luck in the next round!")
else: 
    print("Eh! That is wrong! Sorry!")
nextsong = input("The first bit of the song is, 'Say you can't sleep, baby I know, that's that me espresso!'")
if nextsong == "Espresso" :
    print("Yess! You did good this time 🙌😜🥰😊")
elif nextsong == "I don't know" or "Idk" :
    print("Oh!That is wrong! That's okay! I guess you tried 😊 The song was espresso!")
else:
    print("EH! Sorry!That was wrong! It was espresso! I am glad that you even attempted 😊")

print("There is one more game you might be good at! Let's play tic, tac, toe!! But this time it is a different type of tic tac toe! You'll see!")
import random
computer = random.randint(1,3)
user = int(input("Enter your choice:\n 1 = tic \n 2 = tac \n 3 = toe \n"))
if computer == user:
    print("It's a tie game.")
elif computer == 1  and user == 3:
    print("Computer wins!")
elif computer == 2 and user == 1:
    print("Computer wins again!")
else:
    print("You win!")

print("Let's try your luck again if you lost!")
import random
computer = random.randint(1,3)
user = int(input("Enter your choice:\n 1 = tic \n 2 = tac \n 3 = toe \n"))
if computer == user:
    print("It's a tie game.")
elif computer == 1  and user == 3:
    print("Computer wins!")
elif computer == 2 and user == 1:
    print("Computer wins again!")
else:
    print("You win!")

print("Let's try it one more time to test your luck again!")
import random
computer = random.randint(1,3)
user = int(input("Enter your choice:\n 1 = tic \n 2 = tac \n 3 = toe \n"))
if computer == user:
    print("It's a tie game.")
elif computer == 1  and user == 3:
    print("Computer wins!")
elif computer == 2 and user == 1:
    print("Computer wins again!")
else:
    print("You win!")

win_or_lose = int(input("Tell me how many rounds you won!"))
if win_or_lose == "1":
    print("oh! 1 out of 3 is still good! Be happy you even won one! Hooray 😜🥰")
elif win_or_lose == "2":
    print("Woah! YOu have some good luck there! 2/3! Sheesh!! You are one lucky person 😜🥰😝")
elif win_or_lose == "3":
    print("OMG 😱 I can't believe that your are that lucky! 3/3! That is something we don't see everyday1 Well done! Proud of you 👏🩷😜")
else:
    print("I am so sorry 😔 I hate that you lost! It's okay! Better luck next time! Don't be sad! Just remember: practice makes perfect 😜🥰 ")

bye = input("Did you have fun today?")
if bye == "Yes" or "YESS" :
    print("Yay! I am glad that you had fun! I have to deal with some other important business now! So,Goddbye! See you next time 😜👋🥰🩷🩷🩷🩷🩷")
else: 
    print("Oh! I am sorry! I hope that I can do nbetter next time! I have to deal with some other importnat business now! So, Goddbye! See you next time 🥰😜🩷🩷🩷🩷🩷")





