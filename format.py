import re
import os
import subprocess

def getFiles(path: str) -> list[str]:
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]        

def getSubdirectories(path: str) -> list[str]:
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path,d))]     

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


def format(markdownString: str):
    latexRegex = r"(?<!\\)\$\$|(?<!\\)\$"#matches text between single or double dollar signs, but doesn't match \$
    #see https://stackoverflow.com/questions/35004800/regex-match-a-dollar-without-a-backslash-before-it
    dollars=re.findall(latexRegex,markdownString)
    body=re.split(latexRegex,markdownString)
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

    return parsed

def formatPosts(root: str, dir: str):
    unformattedSubdir = os.path.join(root,"unformatted", dir)
    files = getFiles(unformattedSubdir)
    for file in files:
        with open(os.path.join(unformattedSubdir,file),"r") as rawFile:
            rawFileText = rawFile.read()
            formattedFileText = format(rawFileText)
        
        if dir == "published":
            formattedPath = os.path.join(root,"_posts",file)
        if dir == "drafts":
            formattedPath = os.path.join(root,"_drafts",file)

        with open(formattedPath,"w") as formattedFile:
            formattedFile.write(formattedFileText)
            formattedFile.close()
            subprocess.run(["git","add", formattedPath])
        

thisDir = os.path.dirname(os.path.realpath(__file__))
files = getFiles(os.path.join(thisDir,"unformatted"))
directories = getSubdirectories(os.path.join(thisDir,"unformatted"))


for dir in directories:
    if dir in ["published", "drafts"]:
        formatPosts(thisDir, dir)