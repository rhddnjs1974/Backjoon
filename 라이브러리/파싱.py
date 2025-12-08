def calculate(expr):

    # 1. 토큰화 (문자열 -> 토큰 리스트)
    tokens = []
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch.isspace():  # 공백 무시
            i += 1
            continue
        if ch.isdigit():  # 숫자
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            tokens.append(int(expr[i:j]))
            i = j
        elif ch in "+-*/()":
            tokens.append(ch)
            i += 1

    # 2. 재귀 하강 파서

    idx = 0

    def parse_expression():
        """
        expression := term (('+' | '-') term)
        """
        nonlocal idx
        value = parse_term()
        while idx < len(tokens) and tokens[idx] in ('+', '-'):
            op = tokens[idx]
            idx += 1
            right = parse_term()
            if op == '+':
                value += right
            else:
                value -= right
        return value

    def parse_term():
        """
        term := factor (('*' | '/') factor)
        """
        nonlocal idx
        value = parse_factor()
        while idx < len(tokens) and tokens[idx] in ('*', '/'):
            op = tokens[idx]
            idx += 1
            right = parse_factor()
            if op == '*':
                value *= right
            else:
                value /= right
        return value

    def parse_factor():
        """
        factor := NUMBER
                | '(' expression ')'
                | ('+' | '-') factor  # 단항 연산자
        """
        nonlocal idx

        tok = tokens[idx]

        # 단항 +, -
        if tok in ('+', '-'):
            idx += 1
            val = parse_factor()
            return +val if tok == '+' else -val

        # 괄호
        if tok == '(':
            idx += 1
            val = parse_expression()

            idx += 1
            return val

        # 숫자
        if isinstance(tok, int):
            idx += 1
            return tok

    # 3. 파싱 시작 & 남은 토큰 검사
    result = parse_expression()

    return result


a = input()
print(calculate(a))