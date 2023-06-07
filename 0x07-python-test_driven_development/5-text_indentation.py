#!/usr/bin/python3
""" 
Text indentation
"""

def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")

    ch = 0
    while ch < len(text) and text[ch] == ' ':
        ch += 1

    while ch < len(text):
        print(text[ch], end="")
        if text[ch] == "\n" or text[ch] in ".?:":
            print("\n")
            ch += 1
            while ch < len(text) and text[ch] == ' ':
                ch += 1
            continue
        ch += 1
