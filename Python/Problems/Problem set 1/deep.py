
# Question: In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.


#Get input from user
answer= input("What is the Great Question of Life, the Universe and Everything, outputting: ")

#if the user inputs 42 or (case-insensitively) forty-two or forty two
if answer =="42":
    print("Yes")
elif answer.lower().strip() ==("forty-two"):
    print("Yes")
elif answer.upper().strip() == ("forty two"):
    print("Yes")

#Otherwise output No
else:
    print("No")