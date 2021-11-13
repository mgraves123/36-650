#https://www.programiz.com/python-programming/methods/dictionary/pop

def delete_keys(keys, d):
    for i in range(len(keys)):
        d.pop(keys[i])
    return d

key = ['First', 'Second']
test_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'R'}

print(delete_keys(key, test_dict))
