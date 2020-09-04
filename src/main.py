from src.lexer import Lexer


def run(file_name, text):
    lexer = Lexer(file_name, text)
    tokens, error = lexer.makeTokens()

    return tokens, error
