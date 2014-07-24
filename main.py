from bs4 import BeautifulSoup as bsp
import urllib2

#q = urllib2.urlopen('http://www.quora.com/Computer-Science/What-important-topics-of-number-theory-should-every-programmer-know?share=1')
#q = urllib2.urlopen('https://www.quora.com/Computer-Programming/What-are-the-best-programming-blogs?share=1')
##q  =urllib2.urlopen('http://www.quora.com/Google/Which-programming-languages-should-I-know-to-get-an-internship-or-job-at-a-top-notch-company-like-Google-Facebook-Apple-etc?share=1')
##q = urllib2.urlopen('https://www.quora.com/Computer-Science/What-are-some-interesting-coding-projects-that-I-can-complete-in-7-14-days-to-build-my-resume-for-a-summer-internship?share=1')
q = urllib2.urlopen('http://www.quora.com/How-do-I-find-the-time-complexity-of-any-given-algorithm?share=1')
soup = bsp(q)

divs = soup.find_all('div',{'class':'pagedlist_item'})
print len(divs)
print '%%%%%%'
ans_count = soup.find('div',class_='answer_header_text').text.split()
count = int(ans_count[0])
print count
print "$$$$$$$$$$$$"
#print count--count determines the number of answers a question has.
question = {}
question['ans_count'] = count
if count<6:
    count = len(divs)-1
else:
    count=6
print count
print "^^^^^^^^^^^^"
for i in range(count):
    print i
    print "...."
    if divs[i].find('div',class_='answer_content').text:
        print divs[i].find('div',class_='answer_content').text
        print '*************************'
