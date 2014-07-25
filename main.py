import webapp2
import urllib2
import urlparse
import sys
sys.path.insert(0,'libs')
from bs4 import BeautifulSoup as bsp

question = {}
def Quora(self,r_url):
    html_=urllib2.urlopen(r_url)
    soup = bsp(html_)
    question['title'] = soup.title.string
    question['url'] = r_url
    details = soup.find_all('div',class_='question_details_text')
    for detail in details:
        question['details'] = detail.text
    topics = soup.find_all('div',class_='topic_list_item')
    for topic in topics:
        question['topics'] = [topic.text]

    ans_count = soup.find('div',class_='answer_header_text').text.split()
    count = int(ans_count[0])
    question['answer_count'] = count
    answers = soup.find_all('div',class_='pagedlist_item')
    if count < 6:
        count = len(answers)-1
    else:
        count = 6

    for i in range(count):
        if answers[i].find('div',class_='answer_content'):
            self.response.write(answers[i].find('div',class_='answer_content').text)
            self.response.write('-----------------------------------------------------------------')
    
    

class MainHandler(webapp2.RequestHandler):
    def get(self):
        url = self.request.url
        p = urlparse.urlparse('http://q.goel.im/url=http://www.quora.com/Computer-Science/What-important-topics-of-number-theory-should-every-programmer-know?share=1')
        path = p.path
        tuple_ = path.partition('=')
        result_url = tuple_[2]+'?share=1'
        try:
            Quora(self,result_url)
        except HTTPException():
            self.response.write('TLE')





app = webapp2.WSGIApplication([
    ('/url', MainHandler)
], debug=True)
