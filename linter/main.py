# Hack112
import importlib
from cmu_112_graphics import *
import random

HOMEWORK = 'bshw' # Don't include .py

def sentanceCase(phrase):
    return str(phrase)[0].upper() + str(phrase)[1:]

def main():
    hw = importlib.import_module(HOMEWORK)
    try:
        hw.main()
    except Exception as e:
        global exception
        exception = str(type(e).__name__)
        print(sentanceCase(exception), '-', insults[exception][0])
        MyApp(width=500, height=300)
       
class MyApp(App):
    def appStarted(self):
        self.timerDelay = 100
        self.time = 0
        self.imageObject = Image.open(f'gifs/{insults[exception][1]}')

    def timerFired(self):
        self.time += 1

    def redrawAll(self, canvas):
        frame = self.imageObject.seek(self.time % self.imageObject.n_frames)
        canvas.create_image(self.width / 2, self.height / 2, image=ImageTk.PhotoImage(self.imageObject))

insults = {
    'AssertionError': ("That’s common sense! And your tiny mind is not common!", "AssertionError.gif"), 
    'AttributeError': ("Get your sh*t together!", "AttributeError.gif"),
    'BaseException': ("Try not to throw it on there, yeah? We're f*cking cooking, not playing darts.", "BaseException.gif"),
    'EOFError': ("You f*cking donkey!", "EOFError.gif"), 
    'IndentationError': ("Hey, panini head, listen to me! You're gonna kill someone!", "IndentationError.gif"),
    'IndexError': ('''I wish you would jump in the oven!
                That would make my life a lot easier!''', "IndexError.gif"),
    'KeyError': ("You deserve a kick in the nuts.", "KeyError.gif"),
    'MemoryError': ("I wouldn’t trust you running a bath let alone a restaurant", "MemoryError.gif"),
    'ModuleNotFoundError': ("What are you? An idiot sandwich", "ModuleNotFoundError"),
    'NameError': ('''I’ve never, ever, ever, ever, ever met someone I believe in as 
                little as you.''', "NameError.gif"),
    'OverflowError': ("There’s enough garlic in here to kill every vampire in Europe.", "OverflowError.gif"),
    'RecursionError': ('Forecast for tomorrow? 100 percent chance of tears.', "RecursionError.gif"),
    'ReferenceError':('It’s not as if you’re the captain of the Titanic... you’re the fucking iceberg!', "ReferenceError.gif"),
    'RuntimeError': ('My gran could do better! And she’s dead!', "RuntimeError.gif"),
    'SyntaxError': ("""You do seriously surprise me...
                      You surprise me as to how sh*t you are.""", "SyntaxError.gif"),
    'SystemError': ("Can you just shut the f*ck up for 30 seconds?", "SystemError.gif"),
    'TabError': ("It's like f*cking baby vomit.", "TabError.gif"),
    'TypeError': ("This lamb is so undercooked, it's following Mary to school!", "TypeError.gif"),
    'UnboundLocalError': ("Of course you don't put f*cking salad [in the microwave]!", "UnboundLocalError.gif"),
    'UnicodeError': ("You give me them anaemic bits of sh*t, I’ll f*cking throw them up your @ss sideways.", "UnicodeError.gif"),
    'ValueError': ('This is a really tough decision… ’cause you’re both crap.', "ValueError.gif"),
    'ZeroDivisionError': ("You f*cking donut.", "ZeroDivisionError.gif"),
    '_LintError': ("How f*cking depressing is that?", "_LintError.gif"),
    '_mvcViolation':("It’s sort of prehistoric looking.", "_mvcViolation.gif")
    }

main()