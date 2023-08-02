from theclass import functionsudneed
import datetime
import sys
import os.path
sys.path.append(
	    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from sahana import db_structure
import time
#import main

while True:
	allactivecourse = db_structure.active_courses()

	for course in allactivecourse:
		isclassoutput = functionsudneed.isthereclasstoday(course[0])
		if isclassoutput != "false":
			distance = datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.strptime(isclassoutput, "%H-%M-%S").time()) - datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.now().time())
			if distance < datetime.timedelta(minutes=5):
				functionsudneed.sendwhatsappmessageschool(course[3], course[2], isclassoutput)
				functionsudneed.sendwhatsappmessagetutor("9972910248", course[2], isclassoutput)
				time.sleep(300)



		
		
