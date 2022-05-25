def syntax_check(expression):
    """Checks wheter the expression using brackets is balanced or not.
    
    Args:
        expression: A String with opening and closing brackets to be checked

    Returns:
        A Boolean that is True if the expression is balanced and False otherwise
    """

    # Initiating an empty list as the stack
    stack = []
 
    # Checking each character in the expression
    for char in expression:
        
        if char in ['(']:
 
            # Push the character into the stack
            stack.append(char)

        else:
 
            # IF the character is not opening a bracket, it must be closing.
            # So the stack cannot be empty at this point,
            # if it is, we are closing something that hasn't been opened.
            if stack == []:
                return False
            
            # Checking the last bracket that was opened and removing it from the stack
            current_char = stack.pop()

            # Checking if the expression has any different characters, if so,
            # it is not what we are checking
            if current_char == '(':
                if char != ")":
                    return False
 
    # Check Empty Stack
    if stack != []:
        return False
    else:
        return True
 
 
# Driver Code
if __name__ == "__main__":

    # Example expressions
    expression1 = "()(()())"
    expression2 = "()))))"
    expression3 = ")("
 
    # Function call
    # To check the other examples, change expression1 into any other.
    if syntax_check(expression1) == True:
        print("Balanced")
    else:
        print("Not Balanced")