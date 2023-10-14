sent = (input("enter sentence: ")).lower()
encrypted = []
ress = []

for i in sent:
    for ch in i:
        if ch != " ":
            ch = "*"
            encrypted += [ch]
            print("*", end="")
        
    if i == " ":
        encrypted += [i]
        print(" ", end="")
g = 0
while g < 3:
    letter = input("\nenter letter: ")

    for j in sent:
        for ch1 in j:
            if ch1 == letter:
                
                ress += [letter]
                print(letter, end="")
                
            elif ch1!= letter and ch1 != " ":
                ch1 = "*"
                ress += [ch1]
                print("*", end="")
        if j == " ":
            ress += [j]
            print(" ", end="")
    g += 1

#guessig the whole sentence
print("\nNow try to guese the sentence: ")
sentence = input()
if sentence == sent:
    print("You win!!!")
else: 
    print("You lose :(")
        
