# import libraries
from urllib import urlopen
from bs4 import BeautifulSoup


# open webpage
url = "http://isitweekendyet.com/"
webpage = urlopen(url).read()

# turn html into beautiful soup
weekendSoup = BeautifulSoup(webpage)

# extract info from soup
answerTag = weekendSoup.body.div

answer = answerTag.string.strip()

# print to screen
print("The answer is " + answer)

# further processing?
