print("")
print("Welcome to the internet safety quiz")
print("")
print("This quiz will dertermine whether you know how stay safe on the internet and know how to protect yourslef from any risks.")
 
print("You will be asked 7 questions for each question you will get a list of different answers")
 
print("You will recieve 3 lives whenever a question will be ansered wrong you will lose a live each time")
 
print("If you answered 3 questions wrong you will fail the quiz and have to restart.")

print("Whenever you are ready answer the first question")
print("")

Lives="3"

print("What is a malware?")

print("1 A program that installs and runs a computer without the user's knowledge")
print("")
print("2 Hardware that controls a computer without the user's knowledge")
print("")
print("3 Faulty software")
print("")

answer = input("Answer:")
if answer == "1":
    print("incorrect answer")
    Lives =-1
elif answer == "2":
    print("Incorrect answer")
    Lives =-1
elif answer =="3":
    print("")
    print("CORRECT ASNWER!!")
    print("")

print("What is a virus?")
print("1 A program that makes the user feel unwell")
print("")
print("2 A program which replicates itself and spreads to other computer via attachments")
print("")
print("3 A program that stops a computer from working")
print("")

answer = input("Answer:")
print("")
if answer == "1":
    print("incorrect answer")
    Lives =-1
elif answer =="2":
    print("CORRECT ANSWER!!")
elif answer == "3":
    print("incorrect answer")
    Lives =-1
print("")

print("What is a spyware?")
print("1 A program which replicates itself and spreads to other computers via attachments")
print("")
print("2 Hardware that controls a computer without the user's knowledge")
print("")
print("3 A program which monitors computer activity in an attempt to steal passwords or financial information")
print("")

answer = input("Answer:")
print("")
if answer =="1":
    print("incorrect answer")
    Lives =-1
elif answer =="2":
    print("incorrect answer")
    Lives =-1
elif answer =="3":
    print("CORRECT ANSWER")
print("")

print("What should be used to remove malware from a computer?")
print("1 Anti-virus software")
print("")
print("2 A firewall")
print("")
print("3 a filter")
print("")

answer = input("Answer:")
print("")
if answer =="1":
    print("CORRECT ANSWER!!")
elif answer == "2":
    print("incorrect answer")
    Lives =-1
elif answer =="3":
     print("incorrect answer")
     Lives =-1
print("")

print("What is phishing?")
print("1 Sending a program which replicates itself and spreads to other computers via attachments")
print("")
print("2 Sending an email designed to trick the recipient into giving away personal information")
print("")
print("3 Controlling a computer without the user's knowledge")
print("")

answer = input("Answer:")
print("")
if answer == "1":
    print("incorrect answer")
    Lives =-1
elif answer =="2":
    print("CORRECT ANSWER!!")
elif answer == "3":
    print("incorrect answer")
    lives =-1
print("")

print("What is a troll?")
print("1 A person who leaves distasteful messages on someone's social media account")
print("")
print("2 Someone who sends a virus")
print("")
print("3 someone who spies on a computer")
print("")

answer = input("Answer:")
print("")

if answer == "1":
    print("CORRECT ANSWER!!")
elif answer == "2":
    print("incorrect answer")
    Lives =-1
elif answer == "3":
    print("incorrect answer")
    Lives =-1
print("")

print("LAST AND FINAL QUESTION!!!")
print("")

print("What is used to prevent unauthorised communications from a computer?")
print("1 Anti-virus software")
print("")
print("2 A filter")
print("")
print("3 A firewall")
print("")

answer = input("Answer:")
print("")

if answer == "1":
    print("incorrect answer")
    Lives =-1
elif answer == "2":
    print("incorrect answer")
    Lives =-1
elif answer == "3":
     print("CORRECT ASNWER!!")
print("")

print("CONGRATULATIONS YOU HAVE PASSED THE QUIZ!!!!")
