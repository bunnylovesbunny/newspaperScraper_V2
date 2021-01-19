import os

def runny():
    print("Starting script1")
    os.system("python newsscraper.py")
    print("script1 ended")
    print( "Starting script2")
    os.system("python sendnews.py")
    print("script2 ended")
    print ("Starting script3")
    os.system ("python prothomalo.py")
    print ("script3 ended")


runny()