# Caesar Cipher Shift Encoder 🔐

A Python project where you'll build a secret message encoder using the **Caesar Cipher** — one of the oldest encryption techniques in history!

---

## What Is a Caesar Cipher?

A Caesar Cipher works by **shifting** every letter in a message by a fixed number of positions in the alphabet. For example, with a shift of 3:

```
A → D
B → E
C → F
...
Z → C  (wraps back around!)
```

So the message `HELLO` becomes `KHOOR` with a shift of 3.

---

## Your Goal

Write a Python program that:
1. Asks the user for a message and a shift number
2. **Loops through every character** in the message
3. Shifts each letter by the given amount
4. Leaves spaces, numbers, and punctuation unchanged
5. Prints the encoded message

---

## Python Tools You'll Need

Before you start coding, read up on these three built-in Python functions — they're the key to making your cipher work!

### `ord()`
Converts a character to its **ASCII number** (its position in the computer's character table).

📖 [Read the W3Schools docs on ord()](https://www.w3schools.com/python/ref_func_ord.asp)

```python
ord('A')  # returns 65
ord('a')  # returns 97
```

### `chr()`
Does the opposite — converts an **ASCII number** back into a character.

📖 [Read the W3Schools docs on chr()](https://www.w3schools.com/python/ref_func_chr.asp)

```python
chr(65)  # returns 'A'
chr(97)  # returns 'a'
```

### `isalpha()`
Checks whether a character is a **letter** (and not a space, number, or symbol). Returns `True` or `False`.

📖 [Read the W3Schools docs on isalpha()](https://www.w3schools.com/python/ref_string_isalpha.asp)

```python
'A'.isalpha()  # returns True
'3'.isalpha()  # returns False
' '.isalpha()  # returns False
```

---

## Step-by-Step Hints

### Step 1 — Get input from the user
```python
message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))
```

### Step 2 — Create a variable to hold your encoded message
```python
encoded = ""
```

### Step 3 — Loop through each character in the message
Use a `for` loop to go through the message one character at a time:
```python
for char in message:
    # your encoding logic goes here
```

### Step 4 — Check if the character is a letter
Inside your loop, use `.isalpha()` to decide what to do:
- If it **is** a letter → shift it
- If it **isn't** a letter → leave it alone and add it as-is

### Step 5 — Shift the letter
This is the tricky part! Here's the idea:
1. Use `ord()` to get the character's ASCII number
2. Add the shift value
3. Use `chr()` to convert the number back to a character

> **Watch out for wrapping!** After `Z` (ASCII 90) you need to wrap back around to `A` (ASCII 65). The `%` (modulo) operator can help with this.
>
> **Hint:** Uppercase letters run from 65–90, and lowercase letters run from 97–122. You'll want to handle both cases!

### Step 6 — Print the result
```python
print("Encoded message:", encoded)
```

---

## Challenge Extensions

Once your basic encoder works, try adding these features (hint some of them we will be doing later in the project):

- **Decoder** — Add an option to decode a message (hint: shift in the opposite direction)
- **Brute Force** — Print all 26 possible shifts so you can crack a cipher without knowing the key
- **File I/O** — Read a message from a `.txt` file and write the encoded version to a new file

---

## Example Output

```
Enter your message: Hello, World!
Enter the shift number: 3
Encoded message: Khoor, Zruog!
```

---

## Tips for Success

- Test with a shift of **0** — the message should not change
- Test with a shift of **26** — the message should also not change (full wrap)
- Make sure **spaces and punctuation stay in place**
- Try encoding a message with one program and decoding it with another!

Good luck, and keep your messages secret! 🕵️
