from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from bs4 import BeautifulSoup
from textblob import TextBlob
import browserhistory as bh
import os
import requests

class ScreenManagement(ScreenManager):
    pass


class StartPage(Screen):
    pass

class InputPage(Screen):
    #TODO: create values within the class to hold the current statement and returnimage


    def analyzelinetext(self, semantic):
        opinion = TextBlob(semantic)
        polarity  = str(opinion.sentiment.polarity)[0:4]
        if (polarity[0] == '-'): #accounts for the space a negative marker will take in the string.
            polarity = str(opinion.sentiment.polarity)[0:5]
        subjectivity = str(opinion.sentiment.subjectivity)[0:4]
        statement = "The statement you entered has a polarity score of " + polarity + "\n" \
        + "and a subjectivity score of " + subjectivity
        return statement

    def returnimage(self, semantic):
        #TODO: call external function for analysis of first line input
        #TODO: call external function for analysis of second line input
        #TODO: combine the two and output into GUI
        returnphoto = "photoreplace.jpg"
        return returnphoto

#DEFINE GLOBAL VARIABLES FOR USE IN GRABBING THE IMAGE AND TEXT OUTPUT
sub = ""
pol =""
class HistoryPage(Screen):


    subjectivity = ""
    polarity = ""

    def getimage(self):
            print(pol, sub)
            return "photoreplace.jpg"


    def evaluatehistory(self):
        textContent = []
        data = ''
        numLines = 0
        polarity = 0
        subjectivity = 0

        """ GET BROWSER HISTORY
        comment out block when done testing
        ----------------------------------------"""
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
                break
            if(numLines ==0):
                numLines = 1
        subjectivity = subjectivity/numLines
        polarity = polarity/numLines
        #print(numLines, polarity, subjectivity, "\naverage polarity " + str(polarity / numLines), "\naverage subjectivity " + str(subjectivity / numLines))
        subjectivity = str(subjectivity)[0:4]
        polarity = str(polarity)[0:4]
        if(polarity[0] == '-'):
            polarity = str(opinion.sentiment.polarity)[0:5]

        sub = subjectivity
        pol = polarity


        statement =  "Your browser history has an average polarity: " + pol + "\n" \
        + "and a subjectivity of " + sub



        #self.subjectivity = subjectivity
        #self.polarity = polarity
        return statement
        # print(page_content.find_all("p"))



class FeedbackPage(Screen):
    pass

class TestApp(App):
    title = "Welcome to Hue"

    def build(self):
        return ScreenManagement()


if __name__ == "__main__":
    TestApp().run()