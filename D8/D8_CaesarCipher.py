import string

l = list(string.printable)
letters = []
for i in range(len(l)-5):
    letters.append(l[i])

c = 1


def cipher(ch):
    if ch == 1 or ch == 2:
        text = input("Type your message below: \n")
        shift = int(input("Enter shift value: "))
        ind = 0
        new = ""
        if ch == 2:
            shift *= -1
        for i in text:
            if i in letters:
                ind = letters.index(i)
                ind += shift
                if ind >= len(letters):
                    ind = ind % len(letters)
                new += letters[ind]
            else:
                new += i
        if ch == 1:
            print(f"Encoded Text is: {new}")
        else:
            print(f"Decoded Text is: {new}")
    else:
        print("Invalid Input!")


while c == 1:
    ch = int(input("Type 1 to encode and 2 to decode: "))
    cipher(ch)
    contd = input(
        "Do you want to continue? Press 1 to continue or any key to exit: ")
    if contd == "1":
        c = 1
    else:
        print("Program Ended!")
        c = 0
