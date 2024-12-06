class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    postfix = []

    for char in expression:
        if char.isalnum():  # Operand
            postfix.append(char)
        elif char == '(':  # Left Parenthesis
            stack.push(char)
        elif char == ')':  # Right Parenthesis
            while not stack.isEmpty() and stack.top() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '(' from stack
        else:  # Operator
            while (not stack.isEmpty() and stack.top() != '(' and
                   precedence[char] <= precedence[stack.top()]):
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.isEmpty():
        postfix.append(stack.pop())

    return ''.join(postfix)

def evaluate_postfix(expression):
    stack = Stack()

    for char in expression:
        if char.isdigit():  # Operand
            stack.push(int(char))
        else:  # Operator
            val2 = stack.pop()
            val1 = stack.pop()
            if char == '+':
                stack.push(val1 + val2)
            elif char == '-':
                stack.push(val1 - val2)
            elif char == '*':
                stack.push(val1 * val2)
            elif char == '/':
                stack.push(val1 / val2)
            elif char == '^':
                stack.push(val1 ** val2)

    return stack.pop()

# Example usage
infix_expr = "3+4*2/(1-5)^2^3"
postfix_expr = infix_to_postfix(infix_expr)
print("Infix Expression:", infix_expr)
print("Postfix Expression:", postfix_expr)

result = evaluate_postfix(postfix_expr)
print("Evaluation Result:", result)
