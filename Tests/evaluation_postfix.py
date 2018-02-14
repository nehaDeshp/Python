'''

Evaluating a postfix expression is easier than evaluating an infix expression because it
does not contain any brackets and there are no operator precedence rules to consider.
A postfix expression can be evaluated using the following algorithm:

	Create a new empty list, values
	For each token in the postfix expression
	If the token is a number then
	Convert it to an integer and add it to the end of values
	Else
	Remove an item from the end of values and call it right
	Remove an item from the end of values and call it left
	Apply the operator to left and right
	Append the result to the end of values
	Return the first item in values as the value of the expression

Write a program that reads a mathematical expression in postfix form from the user,
evaluates it, and displays its value.
[ if you dont know what is postfix expression, you can get more information about postfix in google,still if you dont
understand , you can message me in skype,i will help u]

'''

postfix_expr = input("Enter a Postfix expression")
values = []

postfix_expr=postfix_expr.split(" ")
for token in postfix_expr:
    if(token.isdigit()):
        values.append(int(token))
    else:
        right = values.pop();
        left = values.pop();
        store = {
            "+": left + right,
            "-": left - right,
            "/": left / right,
            "*": left * right,
            "//": left // right,
            "**": left ** right,
            "%": left % right,
        }
        print(store)
        values.append(store[token])
print(values[0])
