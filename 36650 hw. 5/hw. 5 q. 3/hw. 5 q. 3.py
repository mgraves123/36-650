#https://java2blog.com/add-character-to-string-in-python/
#https://careerkarma.com/blog/python-remove-character-from-string/

def edits_away(input, output):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if input == output: return True
    for char in range(len(input)):
        for letter in range(len(letters)-1):
            #replacing character 
            if (input[:char] + letters[letter] + input[(char+1):]) == output: return True
            #adding character
            elif (input[:char+1] + letters[letter] + input[char+1:]) == output: return True
    for i in range(len(input)): 
        #removing character
        if (input[:i] + input[i+1:]) == output: return True
    return False

print(edits_away('mall', 'maall'))
print(edits_away('mall', 'mal'))
print(edits_away('mall', 'malt'))
print(edits_away('mall', 'malts'))
print(edits_away('mall', 'malls'))