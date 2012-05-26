import jinja2
import os
import random
import webapp2

 
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(BlogHandler):

    def generateNumber(self):
        digits = (("0", 1), ("1", 0), ("2", 0), ("3", 0), ("4", 0), ("5", 0), ("6", 1), ("7", 0), ("8", 2), ("9", 1))
        composed_number = [] # Hier wird die aus den Ziffern zusammengesetzte Zahl abgelegt
        value = 0
        result =""
        while len(composed_number) <= 5:
            r = random.randint(0,9)
            composed_number.append(digits[r][0])
            value = value + int(digits[r][1])
        result = result.join(composed_number)
        element = (result, value)
        return element
    
    def get(self):
        bag = []
        while len(bag) <= 3:
            bag.append(self.generateNumber())      
        self.render("front.html", bag = bag)
        
        
    def post(self):
        check = self.request.get('check')
        solution = self.request.get('solution')
        if check == solution:
            message = "Toll, richtig!"
            
            bag = []
            while len(bag) <= 3:
                bag.append(self.generateNumber()) 
            
            self.render("front.html", bag = bag, message = message)
        else:
            message = "Bitte nochmal versuchen!"
            
            bag = []
            while len(bag) <= 3:
                bag.append(self.generateNumber()) 
            
            self.render("front.html", bag = bag, message = message)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

