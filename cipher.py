choice = input("Encode or Decode (no capitals)")

if choice == "encode":
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))
    encoded = ""
    for char in message:
        asciiChar = ord(char)
        shiftedChar = asciiChar + shift
        finalChar = chr(shiftedChar)
        encoded += finalChar

    print(encoded)

elif choice == "decode":
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))
    uncoded = ""
    for char in message:
        asciiChar = ord(char)
        shiftedChar = asciiChar - shift
        finalChar = chr(shiftedChar)
        uncoded += finalChar

    print(uncoded)