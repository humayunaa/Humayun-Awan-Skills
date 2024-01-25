vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def move_vow(string):
    str_vow = []
    for each in string:
        if each in vowels:
            string = string.replace(each, "")
            str_vow.append(each)
    return "{}{}".format("".join(str_vow), string)
            

print(move_vow("This is DCU!"))