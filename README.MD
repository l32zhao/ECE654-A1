# A1 - AST Analysis Report
* Name: Lucian Zhao

* Student ID: 21050987

* WatIM: l32zhao
* Email: l32zhao@uwaterloo.ca

## Source Repository

https://github.com/l32zhao/ECE654-A1

## CI Execution Example
https://github.com/l32zhao/ECE654-A1/actions/runs/11194024580

## Observations about the used AST library/tool

The `ast` module in Python provides a powerful and flexible way to parse and analyze Python code. It allows for detailed inspection and manipulation of the abstract syntax tree.

One limitation is that it only works with Python code, and analyzing other languages would require different tools.

## High-level description of the implementation

- **Identifier Length Check**: We traverse the AST and check the length of each identifier. If any identifier has a length of 13, we flag it.
- **Control Structure Nesting**: We track the nesting level of control structures (like `if`, `for`, `while`, `with`). We maintain the maximum level encountered during traversal.

## Observations about false positives and false negatives

- **False Positives**: The code might flag identifiers that are not truly problematic if the goal is more specific than just length.
- **False Negatives**: The code might miss nested control structures in complex constructs or dynamically generated code.