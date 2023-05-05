# Five-GUIs

Welcome to Five GUIs!

In this program, the grammar revolves around burger items that correspond to various arithmetic symbols. The user will input a "burger order" that corresponds to a full arithmetic equation, and then the order will be parsed & evaluated by the program, outputting the equation's answer as the price of the burger. 

The format of a user's burger order is as follows: "Can I get a burger with/with a " + the user's selected ingredients and their amounts (separated by commas!) + the final ingredient must be entered as ", and *final ingredient and amount*?" (Oxford comma and "?" are critical!)

Below is the full supported grammar:

top_bun: "top bun" | "top buns" | "a top bun" = Open Parantheses "("

patty: "patty" | "patties" | "a patty" = Addition "+"

tomato: "tomato slice" | "tomato slices" | "a tomato slice" = Subtraction/Negative Sign "-"

cheese: "slice of cheese" | "slices of cheese" | "a slice of cheese" = Multiplication "*"

pickle: "pickle" | "pickles" | "a pickle" = Division "/"

onion: "onion slice" | "onion slices" | "an onion slice" = Exponent "**"

bottom_bun: "bottom bun" | "bottom buns" | "a bottom bun" = Closed Parentheses ")"

napkin: "a napkin" | "napkins" = Nothing (They're Free! *More on Napkins in the first example*)

Here are some example equations: 

Input: Can I get a burger with 2 patties, 4 slices of cheese, and 3 napkins?
Equation: 2 patties 4 slices of cheese 3 napkins = 2 + 4 * 3 = 14 
Output: Of course! Your total will be $14
(Napkins are best used when you want to end your order with a number instead of an operator like above!)

Input: Can I get a burger with a top bun, 20 pickles, 5 bottom buns, a patty, and 5 napkins?
Equation: Top bun 20 pickles 5 bottom buns a patty 5 napkins = (20/5)+5 = 9
Output: Of Course! Your total will be $9

Input: Can I get a burger with a tomato slice, 10 slices of cheese, a bottom bun, 4 onion slices, and 2 bottom buns?
Equation: Tomato slice 10 slices of cheese a bottom bun 4 onion slices 2 bottom buns = -10*(4**2) = -160
Output: Of course! Your total will be $-160
(Technically because of negative numbers, you might be paid to eat your burger!)

- Important notes - 
The number "1" acts a little strangely in some places as it can cause unwanted complications - This is why each ingredient can be entered in its singular form (Ex: "a tomato slice, a bottom bun, etc."), but ending an order with something like ", and 1 bottom bun" would still work!

The beginning of your order is case sensitive - Make sure that "Can I ..." is capitalized like so.


Command Line Instructions:

- To run the program from the command line, you must first navigate to wherever the file is saved (Ex. C:\Users\Jack\Zadell3200Final)

- Once you are in the appropriate folder, all you need to do is type "py FIVE_GUIS.py" to execute the file

- After typing the previous line, you will be greeted by the program, be prompted to type in your order:
Example - 
Hi there! Welcome to Five GUIs, may I take your order?
Type Your Order Here: Can I get a burger with 2 patties, a top bun, 2 patties, and 4 bottom buns?

You should now be ready to create your specialized burger!
