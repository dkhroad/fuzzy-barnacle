class StringValidator(object):
    '''validate a string with brackes and numbers'''

    def validate_brackets(self,s):
        ''' ensures that string s is valid
        :type s: str
        :rtype: bool
        
        valiation criteria:
            - the string only contains the followin characters 
                - '{', '(',']','[',')','}'
                - one of more digits
            - all open brackets (,),{,},(,) are followed by an 
              approriate closing bracket
             
            - open bracket must be closed in the correct order

        return True if the input string is valid, else false
        '''

        if type(s) != str:
            # punt early if bad input
            return False
        
        left_brackets = ['(','{','[']
        right_brackets = [')','}',']']
        stack = []

        # import pdb; pdb.set_trace()
        for char in s:
            if char in left_brackets:
                stack.append(char)
            elif char in right_brackets:
                if len(stack) < 1: #if stack is empty
                    return False
                if left_brackets.index(stack.pop()) != right_brackets.index(char):
                    # stack doesn't have the correct left bracket as its top
                    # element
                    return False
            elif not char.isdigit():
                return False

        # we are done iterating over the string. 
        # The stack has to be empty if string contained matching brackets in
        # a correct order
        return len(stack) == 0 
    
   
if __name__ == "__main__":
    import sys
    
    if (len(sys.argv) == 1):
        print("Usage: {} \'string_to_validate\'".format(sys.argv[0]));
        sys.exit(1)

    if len(sys.argv[1:]) > 0:
        res = StringValidator().validate_brackets(sys.argv[1])
        if res:
            print("input \"{}\" is a valid string".format(sys.argv[1]))
        else:
            print("input \"{}\" is NOT a valid string".format(sys.argv[1]))


