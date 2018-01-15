#!/usr/bin/env python

HMDSyntaxDefault = {

    # primitive
    'STRING': r"[A-Za-z?'_]+",
    'NUMBER': r'[\d]+',
    'SPACE': r'[ ]+',

    # rule binding
    'RULE_BEGIN': r'[(]',
    'RULE_END': r'[)]',

    # match: positive
    'MATCH_NEXT': r'[+]',
    'MATCH_BEFORE': r'[-]',
    'MATCH_ALWAYS': r'[@]',

    # match: negative
    'MATCH_NOT': r'[!]',

    # grammar
    'GRAMMAR_HAT': r'[\^]',
    'GRAMMAR_WILD': r'[%]',
    'GRAMMAR_OR': r'[|]',

    # variables
    'VARIABLE_IDENTIFIER': r'[$]',
    'VARIABLE_ASSIGNMENT': r'[=]',

    # comment
    'COMMENT': r'[#]'
}

#
# language override
#

# korean
HMDSyntaxKorean = HMDSyntaxDefault.copy()
HMDSyntaxKorean['STRING'] = ''
