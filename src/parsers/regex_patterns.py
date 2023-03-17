from re import compile

ANY_NON_WHITESPACE = compile(r'\S+')
COMMENT_LINE = compile(r'^\s*#.*$')
CONTENT_LINE = compile(r'^[\d+|\d\-\d].*$')
# regex for an equal sign with around it any amount of whitespace
EQUAL_SIGN_SPLITTER = compile(r'\s*=\s*')
COMPOUND_INDEX = compile(r'\d+\-\d+')
