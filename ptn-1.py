# print
print("task1")
print("Hello World!")

# if: elif else is/is not
print("task2")
c = "100"
d = "101"
if(c is d):
    print("c and d have the same identity")
elif(c is not d):
    print("c and d have different identities")
else:
    print("default")

# for: break continue pass
print("task 3")
sentence = "I like python!"
letter_num_before_python = 0
for letter in sentence:
    if(letter == "p"):
        break
    if(letter == " "):
        continue
    if(letter == "i"):
        pass
        print("Current letter is " + letter)
    letter_num_before_python = letter_num_before_python + 1
print("The number of letters before python is ", letter_num_before_python)