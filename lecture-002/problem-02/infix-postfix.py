def check_prec(c: str) -> int:
    if (c == '^'):
        return 3;
    elif c == '/' or c == '*':
        return 2;
    elif c == '+' or c == '-':
        return 1;
    else:
        return -1;

def infix_to_postfix(exp:str) -> str:
    operators = ["/", "*", "^", "+", "-"]
    
    stack: list[str] = []
    postfix_expression = ""
    
    for character in exp:
        if character == "(":
            stack.append(character)
        
        elif character == ")":
            current_stack_length = len(stack) - 1
            
            while current_stack_length > -1:
                if stack[current_stack_length] == "(":
                    stack.pop()
                    break
                
                postfix_expression = postfix_expression + stack[current_stack_length]
                stack.pop()
                current_stack_length -= 1
                
                
        elif character in operators:
            while(len(stack) > 0 and check_prec(character) <= check_prec(stack[len(stack) - 1])):
                operator = stack.pop()
                postfix_expression += operator
                
            stack.append(character)
            
        else: postfix_expression = postfix_expression + character
        
    for i in range(len(stack)):
        operator = stack.pop()
        if operator != ")":
            postfix_expression = postfix_expression + operator
            
    return postfix_expression

def eval_postfix(exp: str) -> int:
    stack = []
    operators = ["/", "*", "^", "+", "-"]
    
    for character in exp:
        if character not in operators:
            stack.append(character)
            
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            result = ""
            if character == "/":
               result = str(b/a)
               
            elif character == "*":
                result = str(b*a)
                
            elif character == "^":
                result = str(b ** a);
                
            elif character == "+":
                result = str(b+a)
                
            elif character == "-":
                result = str(b-a)
                
            stack.append(result)
            
    return stack.pop() 
                
    
    

postfix_exp = infix_to_postfix("2+3*4")
print(eval_postfix(postfix_exp))
    