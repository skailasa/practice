"""
Check if string of parentheses is valid mathematically e.g.
"(){}[]" is true, but "[{]}" returns false
"""


def is_valid(s: str) -> bool:
    right = ['}', ']', ')']
    complete = ['{}', '[]', '()']

    stack = ''

    for ch in s:
        stack += ch
        if stack in right:
            return False

        else:
            if stack[-2:] in complete:
                stack = stack[:-2]

    if stack:
        return False
    return True
