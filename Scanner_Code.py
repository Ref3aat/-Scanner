# Define classification sets
keywords = {'int', 'float', 'return', 'if', 'else', 'for', 'while', 'do', 'break', 'continue', 'switch',
            'case', 'default', 'char', 'double', 'long', 'short', 'void', 'static'}

operators = {'+', '-', '*', '/', '%', '=', '>', '<', '!', '&', '|'}

special_characters = {';', '{', '}', '(', ')', '[', ']', '!', '&', '|'}  

whitespace = {' ', '\t', '\n'}

# Scanner function to process the code
def scanner(code_input):
    tokens = []
    token_buffer = ""

    for ch in code_input:
        if ch in whitespace:
            if token_buffer:
                if token_buffer in keywords:
                    tokens.append((token_buffer, "Keyword"))
                elif token_buffer.isdigit():
                    tokens.append((token_buffer, "Number"))
                else:
                    tokens.append((token_buffer, "Identifier"))
                token_buffer = ""
        elif ch in special_characters:
            if token_buffer:
                if token_buffer in keywords:
                    tokens.append((token_buffer, "Keyword"))
                elif token_buffer.isdigit():
                    tokens.append((token_buffer, "Number"))
                else:
                    tokens.append((token_buffer, "Identifier"))
                token_buffer = ""
            tokens.append((ch, "Special Character"))
        elif ch in operators:
            if token_buffer:
                if token_buffer in keywords:
                    tokens.append((token_buffer, "Keyword"))
                elif token_buffer.isdigit():
                    tokens.append((token_buffer, "Number"))
                else:
                    tokens.append((token_buffer, "Identifier"))
                token_buffer = ""
            tokens.append((ch, "Operator"))
        else:
            token_buffer += ch

    # Handle any remaining tokens
    if token_buffer:
        if token_buffer in keywords:
            tokens.append((token_buffer, "Keyword"))
        elif token_buffer.isdigit():
            tokens.append((token_buffer, "Number"))
        else:
            tokens.append((token_buffer, "Identifier"))

    return tokens

# Test the code
user_code = input("Enter a code in C: ")
token_output = scanner(user_code)
for token, category in token_output:
    print(f"{token}: {category}")
