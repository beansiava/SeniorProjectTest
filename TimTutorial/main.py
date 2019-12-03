from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from bs4 import BeautifulSoup
from textblob import TextBlob
import browserhistory as bh
import os
import requests
from PIL import Image
import numpy as np


class ScreenManagement(ScreenManager):
    pass


class StartPage(Screen):
    pass


class InputPage(Screen):
    # TODO: create values within the class to hold the current statement and returnimage

    def analyzelinetext(self, semantic):
        opinion = TextBlob(semantic)
        polarity = str(opinion.sentiment.polarity)[0:4]
        # accounts for the space a negative marker will take in the string.
        if (polarity[0] == '-'):
            polarity = str(opinion.sentiment.polarity)[0:5]
        subjectivity = str(opinion.sentiment.subjectivity)[0:4]
        statement = "The statement you entered has a polarity score of " + polarity + "\n" \
            + "and a subjectivity score of " + subjectivity
        global subj
        global pola
        subj = subjectivity
        pola = polarity
        return statement

    def returnimage(self, semantic):
        # TODO: call external function for analysis of first line input
        # TODO: call external function for analysis of second line input
        # TODO: combine the two and output into GUI
        global pola #TODO: FIX THE ISSUE WITH THIS GLOBAL VARIABLE - getting "not defined" error
        global subj
        thresholds = np.loadtxt('thresholds.txt', dtype=float)
        print(thresholds[0])

        if pola < thresholds[0]:
            pClass = "angry"
        elif pola < thresholds[1]:
            pClass = "sad"
        elif pola < thresholds[2]:
            pClass = "neutral"
        else:
            pClass = "happy"

            # Edge cases of perfect subjectivity
        if subj is 6:
            subj -= 1
        img = "..StarGAN/stargan_custom/results/ImageSearch/" + \
            pClass + str(subj+1) + ".jpg"

        print(pol, sub)


        returnphoto = "photoreplace.jpg"

        #pola, subj will fetch photo
        return returnphoto


# DEFINE GLOBAL VARIABLES FOR USE IN GRABBING THE IMAGE AND TEXT OUTPUT
sub = ""
pol = ""


class HistoryPage(Screen):

    subjectivity = ""
    polarity = ""
    global p
    global sClass

    def getimage(self):

        thresholds = np.loadtxt('thresholds.txt', dtype=float)
        print(thresholds[0])

        if p < thresholds[0]:
            pClass = "angry"
        elif p < thresholds[1]:
            pClass = "sad"
        elif p < thresholds[2]:
            pClass = "neutral"
        else:
            pClass = "happy"

            # Edge cases of perfect subjectivity
        if sClass is 6:
            sClass -= 1
        img = "..StarGAN/stargan_custom/results/ImageSearch/" + \
            pClass + str(sClass+1) + ".jpg"

        print(pol, sub)
        return img

    # Must be ran after total polarity is calculated
    def tooSad(self):
        thresholds = np.loadtxt('thresholds.txt', dtype=float)
        if p < thresholds[0]:
            thresholds[0] -= .01
        elif p < thresholds[1]:
            thresholds[1] -= .01
        elif p < thresholds[2]:
            thresholds[2] -= .01
        np.savetxt('thresholds.txt', thresholds)

    def tooHappy(self):
        thresholds = np.loadtxt('thresholds.txt', dtype=float)
        if p < thresholds[0]:
            return  # I mean it is as sad as it gets
        elif p < thresholds[1]:
            thresholds[0] += .01
        elif p < thresholds[2]:
            thresholds[1] += .01
        else:
            thresholds[2] += .01

        np.savetxt('thresholds.txt', thresholds)

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
        pAvg = 0
        sAvg = 0
        pCount = 0
        for i in range(10):
            page_link = dict_obj['chrome'][i][0]
            print(page_link)
            page_response = requests.get(page_link, timeout=5)
            page_content = BeautifulSoup(page_response.content, "html.parser")

            # TODO (optional for now): find out how to stop when there are no longer <p> tags (right now, just runs through and breaks if Index Error
            for i in range(0, 40):
                try:
                    paragraphs = page_content.find_all("p")[i].text
                    textContent.append(paragraphs)
                    # dependent on if we can list all p tags-TODO: will probably move this to it's own loop so we can first load up with p tags
                    opinion = TextBlob(textContent[i])
                    numLines += 1
                    polarity += opinion.sentiment[0]
                    subjectivity += opinion.sentiment[1]
                    # print(opinion.sentiment)
                except IndexError:
                    break
                if(numLines == 0):
                    numLines = 1
            if (numLines == 0):
                print("no usable data was found in the file")
            else:
                print(numLines, polarity, subjectivity, "\naverage polarity " + str(polarity /
                                                                                    numLines), "\naverage subjectivity " + str(subjectivity / numLines))
                if polarity is not 0:
                    pAvg += polarity/numLines
                    sAvg += subjectivity/numLines
                    pCount += 1

        # global pol
        pol = pAvg
        # global sub
        sub = sAvg

        global sClass
        global p
        sClass = int((sAvg/pCount)*5) + 1
        p = pAvg/pCount
        print("P is now")
        print(p)
        #self.subjectivity = subjectivity
        #self.polarity = polarity
        statement = "Your browser history has an average polarity: " + str(pol) + "\n" \
            + "and a subjectivity of " + str(sub)
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
