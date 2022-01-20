class Solution:
    def isValid(self, s: str) -> bool:
        # The stack to keep track of opening brackets.
        stack = []
        
        # Hash map for keeping track of mapping. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}
        
        # For every bracket in the expression.
        for char in s:
            
            # If the character is an closing bracket
            if char in mapping:
                
                # Pop the topmost element from the stack, if it is non empty
                # Otherwise return False
                if stack:
                    top_element = stack.pop()
                else:
                    return False
                
                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)
        
        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
