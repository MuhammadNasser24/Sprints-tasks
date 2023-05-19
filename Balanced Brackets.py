def isbalanced(s): # S => string
    stack = []
    open_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    brackets_pairs = {'(':')', '[':']', '{':'}'}



    for bracket in s:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or brackets_pairs[stack.pop()] != bracket:
                return "No"
            
    return "Yes" if not stack else "No"

strings = [
    "{[()]}",
    "{[(])}",
    "{{[[(())]]}}"
]

for s in strings:
    print(isbalanced(s))



