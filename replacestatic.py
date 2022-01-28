import os, fnmatch
# This file is for building the Github Pages (gh) site.
# after building the project using make ogc
# run replacestatic.py
# rename the build folder to docs,
# From https://stackoverflow.com/questions/4205854/python-way-to-recursively-find-and-replace-string-in-text-files
def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            print filename
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            print find + "===="+replace
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

findReplace("/Users/gobehobona/Documents/GitHub/e-learning/build", "_static", "static", "*.html")
findReplace("/Users/gobehobona/Documents/GitHub/e-learning/build", "_images", "images", "*.html")
