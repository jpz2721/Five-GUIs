import lark

grammar = """
start: burger_expression
burger_expression: "Can I get a burger with" burger_item ("," burger_item)* ", and" burger_item "?" 
                |  "Can I get a burger with a" burger_item ("," burger_item)* ", and" burger_item "?"
burger_item: INT? (top_bun | patty | tomato | cheese | pickle | bottom_bun | onion | napkin)
top_bun: "top bun" | "top buns" | "a top bun"
patty: "patty" | "patties" | "a patty"
cheese: "slice of cheese" | "slices of cheese" | "a slice of cheese"
pickle: "pickle" | "pickles" | "a pickle"
onion: "onion slice" | "onion slices" | "an onion slice"
tomato: "tomato slice" | "tomato slices" | "a tomato slice"
bottom_bun: "bottom bun" | "bottom buns" | "a bottom bun"
napkin: "a napkin" | "napkins"

%import common.INT
%import common.WS
%import common.CRLF
%ignore WS
"""

parser = lark.Lark(grammar, parser="lalr")

def evaluate_burger_expression(expression):
    tree = parser.parse(expression)
    result = ""
    for i, item in enumerate(tree.children[0].children):
        if len(item.children) < 2:
            ingredient = item.children[0].data
        else:
            number = item.children[0].value
            ingredient = item.children[1].data
            result += str(number)

        if ingredient == "top_bun":
            result += "("
            print(result)
        elif ingredient == "patty":
            result += "+"
            print(result)
        elif ingredient == "tomato":
            result += "-"
            print(result)
        elif ingredient == "cheese":
            result += "*"
            print(result)
        elif ingredient == "pickle":
            result += "/"
            print(result)
        elif ingredient == "onion":
            result += "**"
            print(result)
        elif ingredient == "bottom_bun":
            result += ")"
            print(result)
        elif ingredient == "napkin":
            print(result)
        else:
            pass
    return "Of course! Your total will be $" + str(eval(result))

print("Example 1: \nHi there! Welcome to Five GUIs, may I take your order? \nType Your Order Here: Can I get a burger with a top bun, 5 slices of cheese, 10 patties, 7 bottom buns, a tomato slice, and 10 napkins?")
order = "Can I get a burger with a top bun, 5 slices of cheese, 10 patties, 7 bottom buns, a tomato slice, and 10 napkins?"
order_up = evaluate_burger_expression(order)

print(order_up)