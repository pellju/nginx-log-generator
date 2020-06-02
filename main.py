import random
import datetime

listOfUserAgents = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; rv:11.0) like Gecko", #IE 11/Win10
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko", #IE11/Win8.1
    "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko", #IE11/Win7
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15", #Safari 13.0 MacOS 10.15
    "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36", #Chrome 83, Win10
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4083.0 Safari/537.36", #Chrome 82, MacOS 10.14.6
    "Mozilla/5.0 (X11; CrOS x86_64 12871.34.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.42 Safari/537.36", #Chrome 81, Chromium OS
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/14.04.6 Chrome/81.0.3990.0 Safari/537.36", #Chrome 81, Ubuntu 14
    "Mozilla/5.0 (Windows NT 10.0; rv:76.0) Gecko/20100101 Firefox/76.0", #Firefox 76, Win10
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0", #Firefox 75, Ubuntu
    "Mozilla/5.0 (Linux; Android 10; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36" #Chrome 79, Android 10
]

def generateIP():
    ip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
    return(ip)

def currentNginxTime():
    x = datetime.datetime.now()
    dayNumber = x.day
    if int(dayNumber) < 10:
        dayNumber = "0" + str(x.day)

    thisTime = "[" + str(dayNumber) + "/" + str(x.strftime("%b")) + "/" + str(x.year) + ":" + str(x.hour) + ":" + str(x.minute) + ":" + str(x.second) + " +0000]"
    #TODO: Convert hours to UTC.
    return(thisTime)

def generateUserAgent():
    a = random.randint(0,10)
    ua = listOfUserAgents[a]
    return(ua)

def generateFinalLine():
    finalLine = generateIP() + " - - " + currentNginxTime() + '"GET / HTTP/1.1" 200 47 "-" "' + generateUserAgent() + '" "-"'
    return(finalLine)

def main (howManyLines):
    f = open("access.log", "a")

    #TODO: Create a check if howManyLines is int or not
    for i in range(int(howManyLines)): #This might be a bad idea.
        f.write("\n" + generateFinalLine())

    f.close()

howManyLines = input("Please enter the number of how many lines you want to create: ")
main(howManyLines)
