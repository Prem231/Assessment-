
print("Welcome to the internet safety quiz")
print("")
print("This quiz will dertermine whether you know how stay safe on the internet and know how to protect yourslef from any risks.")
 
print("You will be asked 7 questions for each question you will get a list of different answers")
 
print("You will recieve 3 lives whenever a question will be ansered wrong you will lose a live each time")
 
print("If you answered 3 questions wrong you will fail the quiz and have to restart.")

print("Whenever you are ready answer the first question")
print("")
Lives=3

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
    Lives -=1
elif answer == "2":
    print("Incorrect answer")
    Lives =-1
elif answer =="3":
    print("")
    print("CORRECT")
print("")
print("What is a virus?")
print("1 A program that makes the user feel unwell")
print("")
print("2 A program which replicates itself and spreads to other computer via attachments")
print("")
Print("3 A program that stops a computer from working")
print("")

answer = input("Answer:")
if answer == "1":
    print("in correct answer")
    Lives =-1
elif answer =="2":
    print("CORRECT")
elif answer == "3":
    print("incorrect answer")
    Lives =-1

