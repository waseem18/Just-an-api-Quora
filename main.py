#Changes need to be made!
import webapp2
import urllib2
import urlparse
import sys
sys.path.insert(0,'libs')
from bs4 import BeautifulSoup as bsp
import os
import jinja2
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
                               
                               

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)



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
        p = urlparse.urlparse('http://www.quora.com/Computer-Science/What-important-topics-of-number-theory-should-every-programmer-know?share=1')
        path = p.path
        tuple_ = path.partition('=')
        result_url = tuple_[2]+'?share=1'
        try:
            Quora(self,result_url)
        except HTTPException():
            self.response.write('TLE')





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
