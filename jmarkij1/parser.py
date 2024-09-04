"""
parser.py -- implement parser for simple expressions

Accept a string of tokens, return an AST expressed as a stack of dictionaries
"""

"""
    simple_expression = number | "(" expression ")" | "-" simple_expression
    factor = simple_expression
    term = factor { "*"|"/" factor }
    expression = term { "+"|"-" term }
"""

from pprint import pprint
from tokenizer import tokenize

def parse_simple_expression(tokens):
    """
    simple_expression = number | "(" expression ")" | "-" simple_expression
    """
    if tokens[0]["tag"] == "number":
        return tokens[0], tokens[1:]
    if tokens[0]["tag"] == "(":
        tokens = tokens[1:]
        node, tokens = parse_expression(tokens)
        assert tokens[0]["tag"] == ")", "Error: expected a ')'"
        return node, tokens[1:]
    if tokens[0]["tag"] == "-":
        node, tokens = parse_simple_expression(tokens[1:])
        node = {"tag":"negate", "value":node}
        return node, tokens[1:]
    

def parse_expression(tokens):
    return parse_simple_expression(tokens)

def test_parse_simple_expression():
    """
    simple_expression = number | "(" expression ")" | "-" simple_expression
    """
    print("testing parse_simple_expression()")
    tokens = tokenize("2")
    ast, tokens = parse_simple_expression(tokens)
    assert ast["tag"] == "number"
    assert ast["value"] == 2
    pprint(ast)
    tokens = tokenize("(2)")
    ast, tokens = parse_simple_expression(tokens[1:])
    assert ast["tag"] == "number"
    assert ast["value"] == 2
    pprint(ast)
    tokens = tokenize("-2")
    ast, tokens = parse_simple_expression(tokens)
    assert ast == { "tag": "negate", "value": {"position": 1, "tag": "number", "value": 2} }
    pprint(ast)
    tokens = tokenize("-(2)")
    ast, tokens = parse_simple_expression(tokens)
    assert ast == { "tag": "negate", "value": {"position": 2, "tag": "number", "value": 2} }
    pprint(ast)


def parse_factor(tokens):
    """
    factor = simple_expression
    """

# def test_parse_factor():
#     print("testing parse_factor()")
#     for s in ["2", "(2)", "-2"]:
#         assert parse_factor(tokenize(s)) == parse_expression(tokenize(s))


if __name__ == "__main__":
    test_parse_simple_expression()
    # test_parse_factor()
    print("done")
