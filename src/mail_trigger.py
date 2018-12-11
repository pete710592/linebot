#!/usr/bin/env python
import rospy
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
from linebot.exceptions import LineBotApiError

# Channel Access Token
line_bot_api = LineBotApi('6CXOEtUWC0yteVKp84RJaUHuaJBf8i8VryR1mtT9gvqSuN2v5gaYl9EdUuYuUebPGMFCiQsWt3xKrLjtB6JlmQkaBagdDBBTsyi/8mL+TZlQQttuYdT5jCIRkVds4oyP+Vj2L9Ty9aYyN6wU8y7MaAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('22ee390e67704d39b3ca17d0881f30de')
# User ID
to = "U61f94258daedd7a7e8c2b9519e64e13b"

class MailTrigger(object):
	def __init__(self):
		self.deliver()
		
	def deliver(self):
		message = TemplateSendMessage(
			alt_text='Mail trigger',
			template=ButtonsTemplate(
				thumbnail_image_url='https://uwaterloo.ca/central-stores/sites/ca.central-stores/files/styles/body-500px-wide/public/uploads/images/little_man_holding_red_envelope.jpg',
				title='Duckiebot #01',
				text='You have 2 mails. \nWhat can I do for you?',
				actions=[
					PostbackTemplateAction(
						label='drop it for me',	 # displayed on the screen
						text='action #101',	 # after push the button, displayed in the dialog
						data='action=buy&itemid=1'
					),
					MessageTemplateAction(
						label='get it by myself',  # displayed on the screen
						text='action #102'	# after push the button, displayed in the dialog
					)
				]
			)
		)
		line_bot_api.push_message(to, message)

if __name__ == "__main__":
	rospy.init_node("mail_trigger",anonymous=False)
	mailTrigger = MailTrigger()
	rospy.spin()