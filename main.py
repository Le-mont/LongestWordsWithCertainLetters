with open('words.txt',"r") as file:
    words = file.read()
ListOfWords = words.split()
print(len(ListOfWords))
chars = ["b","l","s","h","e","i","o"]
TestWord = ""

for x in ListOfWords:
    if len(TestWord) <  len(x):
        has_all = all([ch in chars for ch in x])
        if has_all == True:
            TestWord = x
            print(x)