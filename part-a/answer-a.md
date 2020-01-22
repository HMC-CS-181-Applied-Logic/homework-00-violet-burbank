## Part a

### Describe what the code in `z3-test.py` is doing in a paragraph or two.

 This code first defines variables a and b as booleans and x and y as integers. Then, we create f, a logic statement to test if all the following are true: a is false, b is true, x is between 0 and 100, and x is less than y. After this, we create a solver object to check if this statement is satisfied by some setting of x, y, a and b. There is a way to satisfy this function, which would be setting x = 99, y = 100, b = True, a = False. We print these values out.

 We then add a constraint to the sovler that mandates that y must be less than 1. We check if there is a satisfying assignment, and find that there are none. This makes sense, because there is no way for x to be greater than 0 and less than y if y must be less than one. Since we cannot find a satisfying assignment, there is nothing else that needs to be printed.