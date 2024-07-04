import math
import numpy as np

class Rpn:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def eval(self, tokens):
        for token in tokens:
            if isinstance(token, (int, float)):
                self.push(token)
            elif token in ['+', '-', '*', '/', '**']:
                self.handle_two_arg_op(token)
            elif token in ['sqr', 'sqrt', 'sin', 'cos', 'tan', 'exp', 'log', 'mean']:
                self.handle_one_arg_op(token)
            else:
                raise ValueError(f"Unknown token: {token}")
        
        if len(self.stack) != 1:
            raise ValueError("The RPN expression did not result in a single value")
        return self.pop()

    def handle_two_arg_op(self, op):
        if len(self.stack) < 2:
            raise ValueError("Not enough operands for two-argument operation")
        b = self.pop()
        a = self.pop()
        if op == '+':
            self.push(a + b)
        elif op == '-':
            self.push(a - b)
        elif op == '*':
            self.push(a * b)
        elif op == '/':
            self.push(a / b)
        elif op == '**':
            self.push(a ** b)

    def handle_one_arg_op(self, op):
        if len(self.stack) < 1:
            raise ValueError("Not enough operands for one-argument operation")
        a = self.pop()
        if op == 'sqr':
            self.push(a ** 2)
        elif op == 'sqrt':
            self.push(math.sqrt(a))
        elif op == 'sin':
            self.push(math.sin(a))
        elif op == 'cos':
            self.push(math.cos(a))
        elif op == 'tan':
            self.push(math.tan(a))
        elif op == 'exp':
            self.push(math.exp(a))
        elif op == 'log':
            self.push(math.log(a))
        elif op == 'mean':
            self.push(np.mean(a))

    def __call__(self, tokens):
        return self.eval(tokens)

class RpnStr(Rpn):
    def __call__(self, expr_str):
        tokens = expr_str.split()
        processed_tokens = []
        for token in tokens:
            try:
                processed_tokens.append(float(token))
            except ValueError:
                processed_tokens.append(token)
        return self.eval(processed_tokens)

class AstroIO:
    def read_file(self, filename):
        from astropy.io import fits
        with fits.open(filename) as hdul:
            return hdul[0].data

    def write_file(self, data, filename):
        from astropy.io import fits
        fits.writeto(filename, data, overwrite=True)

class RpnAstroFiles(RpnStr, AstroIO):
    def __call__(self, argv, output_filename):
        tokens = []
        for arg in argv:
            if arg.endswith('.fits'):
                tokens.append(self.read_file(arg))
            else:
                try:
                    tokens.append(float(arg))
                except ValueError:
                    tokens.append(arg)
        result = self.eval(tokens)
        self.write_file(result, output_filename)
