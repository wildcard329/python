word = "Test word."

def changeHiddenWord(hiddenWord, word, letter):
    newHiddenWord = ""
    for i in range(0, len(hiddenWord)):
        if word[i].lower() == letter.lower():
            newHiddenWord += word[i]
        else:
            newHiddenWord += hiddenWord[i]
    return newHiddenWord

def hideWord(word):
    hiddenWord = ""
    for c in word:
        if c.isalpha():
            hiddenWord += '-'
        else:
            hiddenWord += c
    return hiddenWord

def startGame(word):
    hiddenWord = hideWord(word)

    print(hiddenWord)
    while hiddenWord != word:
        letter = input("Enter letter")
        hiddenWord = changeHiddenWord(hiddenWord, word, letter)
        print(hiddenWord)


startGame(word)
