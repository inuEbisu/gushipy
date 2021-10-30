import random as r
import config as c

def check(code: str, checker: str) -> bool:
    if checker == "":
        return True
    
    chs = checker.split("|")
    for i in chs:
        if code.startswith(i):
            return True
    return False

class Gushi(dict):
    def __init__(self, title: str, author: str, context: str, code: int):
        self["title"] = title
        self["author"] = author
        self["context"] = context
        self["code"] = code
    
    def _random_sen(self) -> str:
        cont = self["context"]
        sens = cont.split()
        sub = r.randint(0, len(sens)-1)
        sen = sens[sub]
        return sen

    def gen(self) -> tuple:
        sen_raw = self._random_sen()

        sen = sen_raw
        for p in c.punc:
            sen = sen.replace(p,f"|")
        
        subsens = sen.split("|")
        subsens = list(filter(None, subsens))

        sub = r.randint(0, len(subsens)-1)
        ans = subsens[sub]
        
        question = sen_raw.replace(ans, c.replacement)
        question = question.replace("|","")
        question += f"({self['author']}《{self['title']}》)"
        ans = ans.replace("|","")

        return (question,ans)
        

    
class GushiList(list):
    def __init__(self, g: list = []):
        for x in g:
            self.append(x)

    def random(self, code: str = "") -> Gushi:
        gl = GushiList()
        for g in self:
            if check(g["code"],code):
                gl.append(g)
        
        if gl == []:
            raise Exception("Invaild Code")
        
        sub = r.randint(0, len(gl)-1)
        return gl[sub]
    
    def gen(self, code: str = "", amount: int = 1) -> tuple:
        if amount < 1:
            raise Exception("amount is too small, it must be larger than 0")

        questions = ""
        answers = ""
        for i in range(1, amount + 1):
            t = self.random(code).gen()

            question = f"{i}. " + t[0]
            questions += question + "\n"

            answer = f"{i}. " + t[1]
            answers += answer + "\n"
    
        questions = questions.strip()
        answers = answers.strip()
        return (questions,answers)