def no_lowercase(t):
    for i in t:
        if "a"<=i<="z":
            return False
    return True

def no_uppercase(t):
    for i in t:
        if "A"<=i<="Z":
            return False
    return True

def no_number(t):
    for i in t:
        if "0"<=i<="9":
            return False
    return True

def no_symbol(t):
    for i in t:
        if (not "A"<=i<="Z") and (not "a"<=i<="z") and (not "0"<=i<="9"):
            return False
    return True

def character_repetition(t):
    for i in range(3,len(t)):
        if (t[i]==t[i-1]==t[i-2]==t[i-3]):
            return True
    return False

def check4Sequence(sequence,t):
    for i in range(len(sequence)-3):
        generateSequence=sequence[i:i+4]
        if (generateSequence in t) or (generateSequence[::-1] in t):
            return True
    return False

def number_sequence(t):
    return check4Sequence("01234567890",t)

def letter_sequence(t):
    return check4Sequence("ABCDEFGHIJKLMNOPQRSTUVWXYZ",t.upper())

def keyboard_pattern(t):
    return \
    check4Sequence("!@#$%^&*()_+",t.upper()) or\
    check4Sequence("QWERTYUIOP",t.upper()) or\
    check4Sequence("ASDFGHJKL",t.upper()) or\
    check4Sequence("ZXCVBNM",t.upper())

passw=input().strip()
errors=[]
if len(passw)<8:
    errors.append("Less than 8 characters")

if no_lowercase(passw):
    errors.append("No lowercase letters")

if no_uppercase(passw):
    errors.append("No uppercase letters")

if no_number(passw):
    errors.append("No numbers")

if no_symbol(passw):
    errors.append("No symbols")

if character_repetition(passw):
    errors.append("Character repetition")

if number_sequence(passw):
    errors.append("Number sequence")

if letter_sequence(passw):
    errors.append("Letter sequence")

if keyboard_pattern(passw):
    errors.append("Keyboard pattern")

if len(errors)==0:
    print("OK")
else:
    for i in errors:
        print(i)