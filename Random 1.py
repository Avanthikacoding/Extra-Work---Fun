name = input("Hi I am compbot. What's your name?")
print("Hello" , name)
answer = "Yes"
newanswer = input("Do you wanna play a game?")
if newanswer == answer:
      print("Welcome back to my game")
else:
      print("Well your playing it anyway😡")
num1 = int(input("Input the first number"))
num2 = int(input("Input the second number"))
addition = num1 + num2
multiplication = num1 * num2
division = num1/num2
subtraction = num1 - num2
print("addition is" , addition)
print("multiplication is" , multiplication)
print("division is" , division)
print("subtraction is" , subtraction)
num1 = int(input("Input the first number"))
num2 = int(input("Input the second number"))
num3 = int(input("Input the last number"))
average = (num1 + num2 + num3) /3
print("Your average is" , average)
game = "Yes"
newgame = input("Do you wanna play another game? It's better than the last one.")
if newgame == game:
    print("Yay!Let's start!")
else:
    print("Oh man!Well guess what? I don't care! Your playing it anyway cause I'm bored!" )
chocolate = "Maltesers"
newchocolate = input("I'm going to read your mind. Name any chocolate")
if newchocolate == chocolate:
    print("Yes! I'm officially a mind reader😀")
else:
    print("Oh! I was for sure I could read your mind. Great1 I lost😔")
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
age  = int(input("Enter your age below: Depending on that we will give you a quote about something."))
if age <10:
       print("You are still in primary and still growing. Remember to keep trying when things go wrong and never give up!")
elif age ==10 or age <=20:
       print("You are a teenager and must be going through some mental and physical changes. Just so you know, this is a normal process and it will stop soon after you are an adult. Remember to study hard so that you  can pass your GCSE’s with flying colours!")
elif age ==21 or age <=40:
        print("You are currently in the process of growing older and now have a job. Congrats on that achievement! Make sure to keep pushing to achieve your goal!")
elif age == 41 or age <=60:
        print("Now you have entered the wonderful part of your life. Your children are all grown up and now you get to spend more time with family. Isn’t that the family spirit?")
elif age ==61 or age <=80:
    print("You are very lucky to have lived this long! Congrats on reaching the time where you spend more time for yourself and have retired from your job and started to take more rest.")
else:
    print("I am surprised you have made it this far!  You are very lucky to have lived this long. You must thank God and start to spend more and more time with family before your time comes to leave this world happily and peacefully")
newaverage = int(input("Now, tell me how long on average you spend on your phone everyday? Depending on this I will give you some advice on what to do with it."))
if newaverage  >=4:
     print("That’s good. Keep using the same amount of screentime and you will have healthy eyes😊")
elif  newaverage >=5:
     print("That’s okay but try and reduce it to make sure you don’t get glasses so soon.")
else:
     print("That is not good. You need to reduce your screen time and set time limits to the usage of each app and then make sure you get your eyes check soon before they get even worse! Thank you for being honest though😄")
response = "Yes"
newresponse = input("Did you have fun?")
if newresponse == response:
    print("Great! I'm glad you enjoyed it!😊 Bye!")
else:
    print("I'm sorry you didn't enjoy.😔 I hope I can cheer you up next time! Bye!")


