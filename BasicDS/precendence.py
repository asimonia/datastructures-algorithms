"""
B * C 		* is an infix operator

A + B * C	Which operands do they work on? What takes precendence?

Each operator has a precendence level.  Operators of higher
precendence are used before ones of lower.

A + B * C		B * C are done first, and then A is added to the result.
(A + B) * C		would force the addition of A and B to be done first.

prefix			requires that all operators precede the two operands
postfix			requires that all operators come after the two operands

A + B * C 	=> 		 + A * B C		(infix to pre-fix)
A + B * C	=>		 A B C * +		(infix to post-fix)

Prefix and Postfix do NOT need parens to evaluate the expression
to a value, whereas Infix expressions do!

A + B * C + D =>
pre-fix 		+ + A * B C D
post-fix		A B C * + D +

(A + B) * (C + D) =>
pre-fix			* + A B + C D
post-fix		A B + C D + *

A * B + C * D =>
pre-fix			+ * A B * C D 
post-fix		A B * C D * +

A + B + C + D =>
pre-fix			+ + + A B C D
post-fix		A B + C + D +



"""
from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))
