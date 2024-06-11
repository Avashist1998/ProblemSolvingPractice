#LC 227.

def calculate(s: str) -> int:
    operation = {
        "+": lambda x,y: x+y, 
        "-": lambda x,y: x-y,
        "*": lambda x,y: x*y, 
        "/": lambda x,y: x/y, 
    }

    processed = []
    buffer = 0
    for i, ch in enumerate(s):
        if ch in operation:
            if s[buffer:i+1] != "":
                processed.append(s[buffer:i])
            processed.append(ch)
            buffer = i+1

    processed.append(s[buffer:])
    for operator in [("*", "/"),("-","+")]:
        i = 0
        stack = []
        while i < len(processed):
            if processed[i] in operator:
                prev = stack.pop(-1)
                i += 1
                new = operation[processed[i-1]](int(prev), int(processed[i]))
                stack.append(new)
            else:
                stack.append(processed[i])
            i += 1

        processed = stack
    return int(processed[0])
