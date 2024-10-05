import ast

class ASTAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.has_long_identifiers = False
        self.max_nesting_level = 0
        self.current_nesting_level = 0

    def visit_FunctionDef(self, node):
        self._check_identifier_length(node.name)
        self.generic_visit(node)  # Visit function body without increasing nesting level

    def visit_If(self, node):
        self._enter_block()
        self.generic_visit(node)
        self._leave_block()

    def visit_For(self, node):
        self._enter_block()
        self.generic_visit(node)
        self._leave_block()

    def visit_While(self, node):
        self._enter_block()
        self.generic_visit(node)
        self._leave_block()

    def visit_With(self, node):
        self._enter_block()
        self.generic_visit(node)
        self._leave_block()

    def _check_identifier_length(self, identifier):
        if len(identifier) == 13:
            self.has_long_identifiers = True

    def _enter_block(self):
        self.current_nesting_level += 1
        if self.current_nesting_level > self.max_nesting_level:
            self.max_nesting_level = self.current_nesting_level

    def _leave_block(self):
        self.current_nesting_level -= 1

def analyze_code(code):
    tree = ast.parse(code)
    analyzer = ASTAnalyzer()
    analyzer.visit(tree)
    return analyzer.has_long_identifiers, analyzer.max_nesting_level

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ast_analysis.py <filename>")
        sys.exit(1)

    with open(sys.argv[1], "r") as source_file:
        code = source_file.read()

    has_long_identifiers, max_nesting_level = analyze_code(code)
    print(f"Identifiers with length 13: {'Yes' if has_long_identifiers else 'No'}")
    print(f"Maximum control structure nesting: {max_nesting_level}")