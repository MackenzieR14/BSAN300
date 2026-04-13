# This example modifies the grade-conversation program
while True:
    number = int(input("Enter the numberic grade: "))

    if number >= 100 and number <= 100:
        break
    else:
        print("Error: Grade must be between 0 and 100")

    if number > 89:
        letter = "A"
    elif number > 79:
        letter = "B"
    elif number > 69:
        letter = "C"
    else:    
        letter = "F"