###Team Name: 
      Idiot Sandwiches

###Team Members:
      Adhvik Kanagala (akanagal)
      Keren Huang (kerenh)
      Michael Crotty (mcrotty)
      Sidney Wang (sidneyw)

###Project Name:
      Hell's Computer

###Description:
      A multifaceted project centered around some of Gordon Ramsay's infamous insults. 
      
      Part 1: a custom linter/debugger that catches standard Python errors and exceptions as well as 112-specific errors, but outputs a Gordon Ramsay insult and a corresponding GIF. 
      
      Part 2: an OpenCV project that detects the user's facial movement, and like Gordon Ramsay, will scream at you if you're doing something wrong.

###Modules Needed:
      - importlib
      - numpy
      - cv2
      - pickle
      - playsound

###Files to be Run:
      - Part 1: Linter --> main.py
      - Part 2: OpenCV --> GordonRamsayOpenCV-Hack112\src\gordon-ramsay.py
          - NOTE: depending on camera, line 12 in gordon-ramsay.py can vary:
              cap = cv2.VideoCapture(1)              <-- What I used.
              cap = cv2.VideoCapture(0)              <-- Default camera.
              cap = cv2.VideoCapture(cv2.CAP_DSHOW)  <-- Popular suggested fix

###Citations:
      - https://github.com/codingforentrepreneurs/OpenCV-Python-Series
      - https://www.101soundboards.com/boards/11084-gordon-ramsay-soundboard
      - https://pythontic.com/image-processing/pillow/
      - https://www.w3schools.com/python/
      - 15-112 Linter (cs112_f20_week10_linter.py)
      - 15-112 Course Notes (https://www.cs.cmu.edu/~112/schedule.html)
      - Our lovely 15-112 TAs and professors
      - Google Images (Educational Use of GIFs)
