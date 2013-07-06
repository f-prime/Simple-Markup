
class Simple:
    def __init__(self):
        self.rules = {
                

                "=":self.h1,
                "==":self.h2,
                "===":self.h3,
                "====":self.h4,
                "=====":self.h5,
                "!":self.bold, 
                "/":self.italic,
                "_":self.underline,
                "$":self.code,
                '"':self.orderedlist,
                "*":self.listnum,
                "'":self.unorderedlist,
                "__":self.hr,
                "#":self.link,
                }
        self.code = False
        self.ul = False
        self.ol = False
        self.out = []
    def compile(self, file, out):
        with open(file, 'rb') as file:
            for x in file.readlines():
                self.put = False
                self.out.append("<br/>")
                x = x.split()
                for y in self.rules:
                    try:
                        if x[0] == y:
                            self.put = True
                            self.rules[y](x)
                            break
                    except IndexError:
                        pass
                if not self.put:
                    self.out.append(' '.join(x))
            with open(out, 'wb') as file:
                file.write("".join(self.out))
    
    def h1(self, line):
        self.out.append("<h1>"+line[1]+"</h1>")

    def h2(self, line):
        self.out.append("<h2>"+line[1]+"</h2>")

    def h3(self, line):
        self.out.append("<h3>"+line[1]+"</h3>")

    def h4(self, line):
        self.out.append("<h4>"+line[1]+"</h4>")
    
    def h5(self, line):
        self.out.append("<h5>"+line[1]+"</h5>")

    def bold(self, line):
        self.out.append("<strong>"+line[1]+"</strong>")

    def italic(self, line):
        self.out.append("<i>"+line[1]+"</i>")

    def underline(self, line):
        self.out.append("<u>"+line[1]+"</u>")

    def code(self, line):
        if self.code:
            self.out.append("</code>")
            self.code = False
        else:
            self.out.append("<code>")
            self.code = True

    def unorderedlist(self, line):
        if self.ul:
            self.out.append("</ul>")
            self.ul = False
        else:
            self.out.append("<ul>")
            self.ul = True

    def orderedlist(self, line):
        if self.ol:
            self.out.append("</ol>")
            self.ol = False
        else:
            self.out.append("<ol>")
            self.ol = True

    def listnum(self, line):
        self.out.append("<li>"+line[1]+"</li>")

    def hr(self, line):
        self.out.append("<hr/>")
    
    def link(self, line):
        stuff = line[1].split(":")
        name = stuff[1]
        url = stuff[0]
        data = "<a href=\"{0}\">{1}</a>".format(url, name)
        self.out.append(data)
