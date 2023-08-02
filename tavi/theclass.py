from twilio.rest import Client
import datetime
#from sahana.db_structure import *
import sys
import os.path
sys.path.append(
		    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from sahana import db_structure
from sahana.db_structure import *

class functionsudneed():
	def sendwhatsappmessagetutor(phone, cn, time):
		account_sid = 'AC21b553ae63f9ee2c39f39236f7d3f5f3'
		auth_token = 'ac83ec71d4725f168494bb12c64555ca'
		client = Client(account_sid, auth_token)

		message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='You have '+cn+' course at '+ time, #time.strftime("%m/%d/%Y, %H:%M:%S"),
  to='whatsapp:+91'+phone
)

	def sendwhatsappmessageschool(phone, cn, time):
		account_sid = 'AC21b553ae63f9ee2c39f39236f7d3f5f3'
		auth_token = 'ac83ec71d4725f168494bb12c64555ca'
		client = Client(account_sid, auth_token)

		message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='You have '+cn+' course to attend at '+ time, #time.strftime("%m/%d/%Y, %H:%M:%S"),
  to='whatsapp:+91'+phone
)

	def translate_text(target: str, text: str) -> dict:
    		from google.cloud import translate_v2 as translate

    		translate_client = translate.Client()
    		if isinstance(text, bytes):
        		text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    		result = translate_client.translate(text, target_language=target)

    		print("Text: {}".format(result["input"]))
    		print("Translation: {}".format(result["translatedText"]))
    		print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    		return result
	
	def istutorauth(un, passwd):	
		allstu = all_stu()
		for tutor in allstu:
			if tutor[2] == un and tutor[3] == passwd:
				return True
		
		return False

	def isschoolauth(un, passwd):	
		allstu = all_scho()
		for tutor in allstu:
			if tutor[2] == un and tutor[3] == passwd:
				return True
		
		return False

	def isthereclasstoday(cid):
		sahana = db_structure.time_set(cid)
		#sahana = [[datetime.datetime(2023, 4, 11), 4], [["Monday", "Tuesday", "Thursday"], "630 PM"]]
		coursestart = dt = datetime.datetime.combine(sahana[0][0], datetime.datetime.min.time())
		courseend = coursestart + datetime.timedelta(days=30*int(sahana[0][1]))
		now = datetime.datetime.now()
		if courseend>now>coursestart:
			if now.strftime("%A") in sahana[1][0]:
				return sahana[1][1]
			else:
				return "false"
		else:
			return "false"
