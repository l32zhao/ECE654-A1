import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.max_depth = 0
        self.current_depth = 0
        self.has_length_13_identifiers = False

    def visit_FunctionDef(self, node):
        # Check for identifier length
        if len(node.name) == 13:
            self.has_length_13_identifiers = True
        self.generic_visit(node)

    def visit_Name(self, node):
        # Check variable names
        if len(node.id) == 13:
            self.has_length_13_identifiers = True
        self.generic_visit(node)

    def visit_If(self, node):
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1

    def visit_For(self, node):
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1

    def visit_While(self, node):
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1

    def analyze(self, code):
        tree = ast.parse(code)
        self.visit(tree)
        return self.has_length_13_identifiers, self.max_depth

if __name__ == "__main__":
    code = """
def some_function():
    for i in range(10):
        if i > 5:
            while i < 10:
                pass
"""
    analyzer = CodeAnalyzer()
    has_13, depth = analyzer.analyze(code)
    print(f"Has 13-length identifier: {has_13}")
    print(f"Max control structure depth: {depth}")
