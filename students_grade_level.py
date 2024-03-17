# Write a program that asks the user how many credits they have taken. If they have taken 23 or less, print that the student is a freshman. If they have taken between 24 and 53, print that they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.
credits = int(input("How many credits have you taken? : "))

if credits <= 23:
        print("You are a freshman.")
elif credits <= 53:
        print("You are a sophomore.")
elif credits <= 83:
        print("You are a junior.")
else:
        print("You are a senior.")

