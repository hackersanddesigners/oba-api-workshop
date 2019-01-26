# Input a piece of text to convert to speach using Microsoft's TTS api
from settings import *
import os, requests, time
from xml.etree import ElementTree

try: input = raw_input
except NameError: pass

class TextToSpeech(object):
	def __init__(self, subscription_key):
		self.subscription_key = subscription_key
		self.tts = input("What would you like to convert to speech: ")
		self.timestr = time.strftime("%Y%m%d-%H%M")
		self.access_token = None

	def get_token(self):
		fetch_token_url = "https://westeurope.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
		headers = {
			'Ocp-Apim-Subscription-Key': self.subscription_key
		}
		response = requests.post(fetch_token_url, headers=headers)
		print("\ntoken:" +str( response.text ))
		self.access_token = str(response.text)


	def save_audio(self):
		base_url = 'https://westeurope.tts.speech.microsoft.com/'
		path = 'cognitiveservices/v1'
		constructed_url = base_url + path
		headers = {
			'Authorization': 'Bearer ' + self.access_token,
			'Content-Type': 'application/ssml+xml',
			'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
			'User-Agent': 'Speech'
		}
		xml_body = ElementTree.Element('speak', version='1.0')
		xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
		voice = ElementTree.SubElement(xml_body, 'voice')
		voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
		voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)')
		voice.text = self.tts
		body = ElementTree.tostring(xml_body)

		response = requests.post(constructed_url, headers=headers, data=body)

		if response.status_code == 200:
			with open('sample-' + self.timestr + '.wav', 'wb') as audio:
				audio.write(response.content)
				print("\nStatus code: " + str(response.status_code) + "\nYour TTS is ready for playback.\n")
		else:
			print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")


if __name__ == "__main__":
	#MS_Azure_Key should be set in .env and loaded in settings.py
	subscription_key = MS_Azure_Key
	app = TextToSpeech(subscription_key)
	app.get_token()
	app.save_audio()