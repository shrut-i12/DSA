words = input("enter a  string ")
vowels ="aeiouAEIOU"
count_vowels=0
count_consonant=0

for i in words:
    if i.isalpha():
     if i in  vowels:
        count_vowels +=1
     else:
        count_consonant +=1
print("number of vowels:",count_vowels)
print("number of constantant",count_consonant)
