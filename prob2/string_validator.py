def validate_brackets(str):
    ''' ensures that string s is valid
    
    valiation criteria:
        - the string only contains the followin characters 
            - '{', '(',']','[',')','}'
            - one of more digits
        - all open brackets (,),{,},(,) are followed by an 
          approriate closing bracket
         
        - open bracket must be closed in the correct order

    return True if the input string is valid, else false
    '''
    left_brackets = ['(','{','[']
    right_brackets = [')','}',']']
    stack = []
    # import pdb; pdb.set_trace()
    for char in str:
        if char in left_brackets:
            stack.append(char)
        elif char in right_brackets:
            if len(stack) < 1:
                return False
            if left_brackets.index(stack.pop()) != right_brackets.index(char):
                return False
        elif not char.isdigit():
            return False

    # we are done iterating over the string. 
    # The stack has to be empty if string contained matching brackets in
    # a correct order
    return len(stack) == 0 
    
    
