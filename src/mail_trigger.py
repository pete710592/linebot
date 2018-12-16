#!/usr/bin/env python
import rospy
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
from linebot.exceptions import LineBotApiError
from hbc_msgs.msg import MailStamped

# Channel Access Token
line_bot_api = LineBotApi('6CXOEtUWC0yteVKp84RJaUHuaJBf8i8VryR1mtT9gvqSuN2v5gaYl9EdUuYuUebPGMFCiQsWt3xKrLjtB6JlmQkaBagdDBBTsyi/8mL+TZlQQttuYdT5jCIRkVds4oyP+Vj2L9Ty9aYyN6wU8y7MaAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('22ee390e67704d39b3ca17d0881f30de')

class MailTrigger(object):
	def __init__(self):
		self.sub_mail = rospy.Subscriber('/mail', MailStamped, self.cbMail, queue_size=1)
		
	def cbMail(self, mail_msg):
		mail_msg = mail_msg
		ID = mail_msg.ID
		mailNum = mail_msg.mailNum
		self.deliver(ID, mailNum)
		print("An inquiry message has been sent successfully.")
		
	def deliver(self, ID, mailNum):
		message = TemplateSendMessage(
			alt_text='Mail trigger',
			template=ButtonsTemplate(
				thumbnail_image_url='https://uwaterloo.ca/central-stores/sites/ca.central-stores/files/styles/body-500px-wide/public/uploads/images/little_man_holding_red_envelope.jpg',
				title='Duckiebot #01',
				text='You have ' + mailNum + ' mails. \nWhat can I do for you?',
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
		line_bot_api.push_message(ID, message)  #send a message to a specified client

if __name__ == "__main__":
	rospy.init_node("mail_trigger",anonymous=False)
	mailTrigger = MailTrigger()
	rospy.spin()