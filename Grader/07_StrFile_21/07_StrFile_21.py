while True:
    data=input()
    if (data=="end"):
        break
    ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet=ALPHABET.lower()
    for i in data:
        if "A"<=i<="Z":
            print(ALPHABET[(ALPHABET.find(i)+13)%26],end="")
        elif "a"<=i<="z":
            print(alphabet[(alphabet.find(i)+13)%26],end="")
        else:
            print(i,end="")
    print()