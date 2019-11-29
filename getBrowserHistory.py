f = open(r"C:\Users\seanb\AppData\Local\Google\Chrome\User Data\Default\History", 'rb')
data = f.read()
f.close()
f = open('your_expected_file_path', 'w')

# TODO: (if we use this method) -  repr(data) won't do anything useful
# This is because we are pulling from a SQL database, so we need to query it.
f.write(repr(data))
f.close()

#it seems as though I have a few options:
    #1. use browserhistory as bh and have the program collect the historyy
        #when the browser is closed
    #2. We know where the chrome history database is, we can access the path
        #and then the variable.  We can use os.environ.get("USERPROFILE") to
    #3.

# import os
# os.system("taskkill /im chrome.exe /f")