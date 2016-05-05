# coding: utf-8

"""
Pashto Transliteration Base Code

Transliterates between PersoArabic and Latin scripts.

[Alexa Little 2015]
"""

import codecs

pairs = [("A", u"آ"), ("a", u"ا" ), ("b", u"ب"), ("C", u"ث"), ("c", u"چ"), ("d", u"د"),
("D", u"ډ"), ("E", u"ږ"), ("e", u"ع"), ("f", u"ف"), ("G", u"غ"), ("g", u"ګ"), 
("h", u"ح"), ("H", u"ځ"), ("I", u"ي"), ("i", u"ې"), ("j", u"ج"), ("J", u"ض"), 
("K", u"خ"), ("k", u"ک"), ("l", u"ل"), ("m", u"م"), ("n", u"ن"), ("N", u"ڼ"), 
("o", u"ه"), ("O", u"ۀ"), ("p", u"پ"), ("P", u"څ"), ("Q", u"ښ"), ("q", u"ق"), 
("r", u"ر"), ("R", u"ړ"), ("S", u"ص"), ("s", u"س"), ("t", u"ت"), ("T", u"ټ"), 
("u", u"ئ"), ("U", u"ۍ"), ("V", u"ظ"), ("v", u"ط"), ("W", u"ؤ"), ("w", u"و"), 
("X", u"ژ"), ("x", u"ش"), ("Y", u"ی"), ("y", u"ے"), ("Z", u"ذ"), ("z", u"ز"),
("0", u"٠"), ("1", u"١"), ("2", u"٢"), ("3", u"٣"), ("4", u"٤"), ("5", u"٥"), 
("6", u"٦"), ("7", u"٧"), ("8", u"٨"), ("9", u"٩"), ("?", u"؟"), ("Y", u"ى")]

infile = sys.argv[1]

with codecs.open(infile, "r", "utf-8") as infile:
        lines = filter(None, (line.rstrip() for line in infile))
        
def askpairs(char, x, y):
    out = ""
    for pair in pairs:
        if pair[x] == char:
            out = pair[y]
            break
        else:
            out = char
    return out

def getletters(x, y):
    outstring = ""
    outlines = []
    for line in lines:
        for char in line:
            outstring += askpairs(char, x, y)
        outlines.append(outstring)
        outstring = ""
    outfile = codecs.open("prtrans", "w", "utf-8")
    for line in outlines:
        outfile.write(line + "\n")

def console():
    val = raw_input("Select destination script (en/pt): ")
    if val == "pt":
        getletters(0, 1)
    elif val == "en":
        getletters(1, 0)
    else:
        print "Not a valid option."
        console()

console()
