# Style and efficiency:

- The comments are not very helpful and sometimes redundant. Some of them state the obvious, while others are incorrect. The comments should explain the purpose of the code and the logic behind it, rather than simply describing what each line does. Basically keep it simple and direct, do not overthink it.
- The function could be made more efficient by converting the input number to a string and checking if the string is equal to its reverse. This would eliminate the need for the loop and make the function much simpler and faster.

# Logical errors:
    I will be using the term(code line) for denoting actual lines of code(excluding comments)
------------------------------------------------------------------------------------------------

- The while loop condition in code line 7 is incorrect. It should be while num != 0 instead of while num != x.
-  Also, the num variable in code line 6 should be initialized to x.abs instead of x, since we want to work with the absolute value of the input number.
-   The variable "reversed" should be initialized to zero before the loop, not inside the loop. Otherwise, the loop will not work correctly. ontop of that "reversed" is misspelled in codeline 5 as "reversd" but spelt as "reversed' in insuing variable calls, which will definately lead to erros.
-   The condition for returning false(in codeline 12) after the loop is incorrect. It should be if reversed != x.abs, not if reversed != x.

# Takeaways
- overall a great effort, still areas to improve upon. particullary on the commenting and efficiency of the code.
- Always read through your code after completing to check for any misspelt characters or syntax errors.
- Always keep comments brief and to the point, it is also best practice to comment what you want to achieve with the code at the beggining of the function. Example below :

       my_func(x):
           """What my function does"""
