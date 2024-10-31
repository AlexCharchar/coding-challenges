def isValid(s):

    pairs = {")":"(", "]":"[", "}":"{"}
    open_bracket = [] 
    
    for i in s:
        
        if i in pairs.values():  # Check if it's an open bracket; if so, append it to the stack.
            open_bracket.append(i)
            
        # Check if it's a closing bracket and matches the last item in the stack. 
        # Since we're using a stack (last-in, first-out), add and remove operations happen at the end of the list.
        elif i in pairs.keys() and len(open_bracket) > 0 and pairs[i] == open_bracket[-1]:  
            open_bracket.pop()
        else:
            return False  # If there's a closing bracket before an open bracket in the stack, it's invalid; return False.
    
    # If the stack is empty, all brackets are matched; otherwise, an open bracket lacks a corresponding close.
    if len(open_bracket) == 0:
        return True
    else:
        return False
