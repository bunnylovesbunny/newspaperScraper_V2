import os

def runny():
    print("Starting script1")
    os.system("python newsscraper.py")
    print("script1 ended")
    print( "Starting script2")
    os.system("python testDB.py")
    print("script2 ended")

runny()