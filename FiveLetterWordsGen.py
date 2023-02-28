Words = open("AllTheWords.txt", "r")

AllChoices = []
Target = ""

for x in Words:
    Target = x

    if(len(Target) == 6):
        AllChoices.append(Target)
        
Words.close()
print(AllChoices)

FiveLetter = open("FiveLetterWords.txt", "x")
FiveLetter = open("FiveLetterWords.txt", "a")

FiveLetter.writelines(AllChoices)
FiveLetter.close()





