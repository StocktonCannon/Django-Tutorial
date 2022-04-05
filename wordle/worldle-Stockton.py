# a_file = open("sample.txt", "r")
# list_of_lists = []
# for line in a_file:
# stripped_line = line. strip()
# line_list = stripped_line. split()
# list_of_lists. append(line_list)
# a_file.
# print(list_of_lists)

firstCharacter = input("enter first character -> ")
secondCharacter = input("enter second character -> ")
thirdCharacter = input("enter third character -> ")
fourthCharacter = input("enter fourth character -> ")
fifthCharacter = input("enter fifth character-> ")
unusedCharacters = input("enter a string of unused letters -> ")
unorderedLetters = input("enter a string of letters that must be used ->")


wordFile = open("wordle/words.txt", "r")
setOfWords = []
for line in wordFile:
    stripped_line = line.strip()
    setOfWords.append(stripped_line)
wordFile.close()

setofWordsWithSetLetters = []
for word in setOfWords:
    if (word[0] == firstCharacter or firstCharacter == "") and (word[1] == secondCharacter or secondCharacter == "") and (word[2] == thirdCharacter or thirdCharacter == "") and (word[3] == fourthCharacter or fourthCharacter == "") and (word[4] == fifthCharacter or fifthCharacter == ""):
        setofWordsWithSetLetters.append(word)


listToRemove = []
for word in range(len(setofWordsWithSetLetters)):
    possible = True
    for letter in setofWordsWithSetLetters[word]:
        for unusedCharacter in unusedCharacters:
            if (unusedCharacter == letter):
                possible = False
    if (not possible):
        listToRemove.append(setofWordsWithSetLetters[word])
for i in listToRemove:
    setofWordsWithSetLetters.remove(i)
# print(setofWordsWithSetLetters)

listToRemove = []
for wordIndex in range(len(setofWordsWithSetLetters)):
    possible = True
    for unorderedLetter in unorderedLetters:
        if (not (unorderedLetter in setofWordsWithSetLetters[wordIndex])):
            possible = False
    if (not possible):
        listToRemove.append(setofWordsWithSetLetters[wordIndex])
for i in listToRemove:
    setofWordsWithSetLetters.remove(i)
print(setofWordsWithSetLetters)







# for word in setOfWords:
#     for i in range(5):
#         if word[0] == firstCharacter and word[1] == secondCharacter and word[2] = :
#             print(word)