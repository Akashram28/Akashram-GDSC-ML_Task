s = str(input("Enter notation : "))
try:
    print(eval(s))
except Exception:
    print("Invalid Notation")