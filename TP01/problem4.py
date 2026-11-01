print(int("7") + 3.5)
print(str(10) * 3)
print(bool(""), bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True) + float("2.5"))
print(round(2.5), round(3.5))
print(type(10 / 2))

print("Part B. turns a string into an int")
def safe_int(text):
    text = text.strip()  #cut strip bar
    if text.lstrip("-").isdigit():
        return int(text)   #return text into number
    try:
        return int(float(text))
    except ValueError:
        return "Not a number"

for sample in ["42", "-8", "3.90", "abc", ""]:
    print(repr(sample), "-> ", safe_int(sample))
# representation: is a built-in function that returns an unambiguous, official string representation of an object

       
print("\n\nPart C. Ask the user for two numbers with input(), convert them with safe_int() ") 
def safe_int(text):
    try:
        number = float(text.strip())
        return int(number)
    except ValueError:
        return None


num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

a = safe_int(num1)
b = safe_int(num2)

if a is None or b is None:
    print("Please enter valid numbers!")
else:
    total = a + b
    print("The sum is:", total)