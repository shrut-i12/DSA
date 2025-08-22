text=input("enter a string")
c_text =""
for char in text:
    if char.isalnum():
        c_text += char.lower()
if c_text == c_text[::-1]:
    print("it is a palindrome",text)
else:
    print("it is not a  palindrome",text)