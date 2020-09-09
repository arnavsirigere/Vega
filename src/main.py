from src.lexer import Lexer
from src.parser import Parser


def run(file_name, text):
    lexer = Lexer(file_name, text)
    tokens, error = lexer.makeTokens()
    if error:
        return None, error

    parser = Parser(tokens)
    ast = parser.parse()  # ast => Abstract Syntax Tree

    return ast.node, ast.error
