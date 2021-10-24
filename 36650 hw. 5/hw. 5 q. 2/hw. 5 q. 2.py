def punc_rm(str):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    new_str = ''
    for char in range(len(str)-1):
        if str[char] in punctuations:
            continue
        else:
            new_str = new_str + (str[char])
    return print(new_str)

punc_rm('Hello in 36-650, & other MSP courses.')