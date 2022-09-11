spam = [1]
def list_things(list):
    output = ''
    if len(list) > 1:
        first = spam[:-1]
        last = spam[-1]
        for word in first:
            output += str(word)
            output += ', '
        output += 'and ' + str(last)
        return output
    else:
        for word in list:
            return ''.join(str(word))
    
print(list_things(spam))