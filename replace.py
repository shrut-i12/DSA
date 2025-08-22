text="i love apples"
words =text.split()
for i in range(len(words)):
    if words[i]=="apples":
     words[i]="orange"

     new_text=" ".join(words)
     print("before replace:",text)
     print(" after replace:",new_text)        

