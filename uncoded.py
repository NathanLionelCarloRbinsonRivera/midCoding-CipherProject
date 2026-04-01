message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))
uncoded = ""

for char in message:
    asciiChar = ord(char)
    shiftedChar = asciiChar - shift
    finalChar = chr(shiftedChar)
    uncoded += finalChar

print(uncoded)