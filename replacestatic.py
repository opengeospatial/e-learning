import os, fnmatch
# from https://stackoverflow.com/questions/4205854/python-way-to-recursively-find-and-replace-string-in-text-files
def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

findReplace("./docs", "_static", "static", "*.html")
