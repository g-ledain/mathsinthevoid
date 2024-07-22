import re
import os

def leadingContainsNewline(myString: str)-> bool:
    newString = myString
    if newString == "":
        return False
    while newString[0].isspace():
        if newString == "":
            return False
        if newString[0]=="\n":
            return True
        else:
            newString = newString[1:]
    return False

def trailingContainsNewline(myString: str) -> bool:
    return leadingContainsNewline(myString[::-1])
        

thisDir = os.path.dirname(os.path.realpath(__file__))
for subdir, dirs, files in os.walk(os.path.join(thisDir,"unformatted")):
    for file in files:
        with open(os.path.join(thisDir,"unformatted",file),"r") as rawFile:
            rawFileText = rawFile.read()
        latexRegex = r"(?<!\\)\$\$|(?<!\\)\$"#matches text between single or double dollar signs, but doesn't match \$
        #see https://stackoverflow.com/questions/35004800/regex-match-a-dollar-without-a-backslash-before-it
        dollars=re.findall(latexRegex,rawFileText)
        body=re.split(latexRegex,rawFileText)
        parsed=body[0]
        for i in range(len(dollars)):
            dollarPart=dollars[i]
            bodyPart = body[i+1]
            newLine=""
            mathMode=""
            
            if dollarPart=="$$":
                mathMode="display"
                tag="div"
            if dollarPart=="$":
                mathMode="inline"
                tag="span"
            
            if i%2==0:#opening delimiter
                if not trailingContainsNewline(body[i]) and mathMode=="display":
                    newLine="\n"
                parsed+=newLine
                parsed+="<"+tag+">"
                parsed+=dollarPart 
            if i%2!=0:#closing delimiter
                if not leadingContainsNewline(bodyPart) and mathMode=="display":
                    newLine="\n"
                parsed+=dollarPart
                parsed+="</"+tag+">"
                parsed+=newLine
            parsed+=bodyPart
            
        with open(os.path.join(thisDir,"_posts",file),"w") as parsedFile:
            parsedFile.write(parsed)
            parsedFile.close()
