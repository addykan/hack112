# Hack112
import hw10
'''
Structure:
Import actual code file, run it inside a try block
Add exceptions for everything
'''
def main():
    try:
        hw10.main()
    except Exception as e:
        print(str(e)[0].upper() + str(e)[1:] + '.', insults[str(type(e).__name__)])
       
insults = {
    'AssertionError': "That’s common sense! And your tiny mind is not common!", 
    'AttributeError': "Get your shit together!",
    'BaseException': "Try not to throw it on there, yeah? We're f***ing cooking, not playing darts.",
    'EOFError': "You f*cking donkey", 
    'IndentationError': "Hey, panini head, listen to me! You're gonna kill someone!",
    'IndexError': '''I wish you would jump in the oven!
                That would make my life a lot easier!''',
    'KeyError': "You deserve a kick in the nuts.",
    'MemoryError': "I wouldn’t trust you running a bath let alone a restaurant",
    'ModuleNotFoundError': '''You know, if you sauté scallops in a non-stick pan,
                            they won’t stick. That’s why it’s called f*cking
                            non-stiiiiiiiiiiick!''', 
    'NameError': '''I’ve never, ever, ever, ever, ever met someone I believe in as 
                little as you.''',
    'RecursionError': 'Forecast for tomorrow? 100 percent chance of tears.',
    'ReferenceError':'It’s not as if you’re the captain of the Titanic... you’re the fucking iceberg!',
    'OverflowError': "There’s enough garlic in here to kill every vampire in Europe.",
    'TabError': "It's like f***ing baby vomit.",
    'TypeError': "This lamb is so undercooked, it's following Mary to school!",
    'UnboundLocalError': "Of course you don't put f***ing salad [in the microwave]!",
    'UnicodeError': "You give me them anaemic bits of sh*t, I’ll f*cking throw them up your ass sideways.",
    'ValueError': 'This is a really tough decision… ’cause you’re both crap.',
    'ZeroDivisionError': "You f*cking donut."
    }

main()