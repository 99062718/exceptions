number = input("Please enter a number here! (seriously)")
try:
    number = float(number)
except ValueError:
    print("WHY DIDNT YOU ENTER A NUMBER")
else:
    print("Good job!")
finally:
    exit()