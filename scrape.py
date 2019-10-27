from bs4 import BeautifulSoup
import requests
from textblob import TextBlob
# Here, we're just importing both Beautiful Soup and the Requests library
page_link = 'https://medium.com/the-business-of-being-happy-and-healthy/how-i-read-more-books-than-anyone-i-know-aea13b104ec2'
# this is the url that we've already determined is safe and legal to scrape from.
page_response = requests.get(page_link, timeout=5)
# here, we fetch the content from the url, using the requests library
page_content = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.
textContent = []
data = ''
numLines = 0
polarity = 0
subjectivity = 0

""" GET BROWSER HISTORY
comment out block when done testing
----------------------------------------"""
import browserhistory as bh
import os
try:
    os.system("taskkill /im chrome.exe /f")
    for i in range(5):
        print("--------------------------------------------------")
    print("Program begins now")
    print("--------------------------------------------------")
except:
    print("chrome was already closed")
dict_obj = bh.get_browserhistory()
dict_obj.keys()
page_link = dict_obj['chrome'][0][0]
print(page_link)
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")




#TODO (optional for now): find out how to stop when there are no longer <p> tags (right now, just runs through and breaks if Index Error
for i in range(0, 40):
    try:
        paragraphs = page_content.find_all("p")[i].text
        textContent.append(paragraphs)
        #dependent on if we can list all p tags-TODO: will probably move this to it's own loop so we can first load up with p tags
        opinion = TextBlob(textContent[i])
        numLines += 1
        polarity += opinion.sentiment[0]
        subjectivity += opinion.sentiment[1]
        # print(opinion.sentiment)
    except IndexError:
        break;
print(numLines, polarity, subjectivity, "\naverage polarity " + str(polarity / numLines), "\naverage subjectivity " + str(subjectivity / numLines))
# print(page_content.find_all("p"))




#TODO: Probably delete all of this, and treat each index of textContent as its own string.  Run through opinion, store, GET AVERAGE.
#
# print(textContent)
# for i in range (0,2):
#     data = data.join(textContent[i])
#     print(data)
#
# opinion = TextBlob(data)
# print(opinion.sentiment)

# In my use case, I want to store the speech data I mentioned earlier.  so in this example, I loop through the paragraphs, and push them into an array so that I can manipulate and do fun stuff with the data.