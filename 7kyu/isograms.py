def is_isogram(string):
    #your code here
    tempArray = []
    for letter in string:
        if letter.lower() in tempArray:
            return False
        else:
            tempArray.append(letter.lower())
    
    return True