from stack import Stack
def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False
def is_paren_balanced(paren_string):
    index = 0
    is_balanced = True
    s = Stack()
    if paren_string == '':
        is_balanced = False
        return False
    elif paren_string[-1] in '([{':
        is_balanced = False
        return False
    else:
        while index < len(paren_string) and is_balanced == True:
            if paren_string[index] in '([{':
                s.push(paren_string[index])
            else:
                if s.is_empty():
                    is_balanced = False
                    return False
                elif is_match(s.pop(), paren_string[index]):
                    is_balanced = True
                else:
                    is_balanced == False
                    return False
            index += 1
        if s.is_empty() and is_balanced == True:
            return True
print(is_paren_balanced('[]'))
print(is_paren_balanced('([{}])'))
print(is_paren_balanced('(([)'))
print(is_paren_balanced('())'))
print(is_paren_balanced('))'))
print(is_paren_balanced('(('))
print(is_paren_balanced(''))
