"""




Token = _TokenType()

# Special token types
Text = Token.Text
Whitespace = Text.Whitespace
Newline = Whitespace.Newline
Error = Token.Error
# Text that doesn't belong to this lexer (e.g. HTML in PHP)
Other = Token.Other

# Common token types for source code
Keyword = Token.Keyword
Name = Token.Name
Literal = Token.Literal
String = Literal.String
Number = Literal.Number
Punctuation = Token.Punctuation
Operator = Token.Operator
Comparison = Operator.Comparison
Wildcard = Token.Wildcard
Comment = Token.Comment
Assignment = Token.Assignment

# Generic types for non-source code
Generic = Token.Generic

# String and some others are not direct childs of Token.
# alias them:
Token.Token = Token
Token.String = String
Token.Number = Number

# SQL specific tokens
DML = Keyword.DML
DDL = Keyword.DDL
CTE = Keyword.CTE
Command = Keyword.Command


"""
import sqlparse


class FlowNode:
    pass
