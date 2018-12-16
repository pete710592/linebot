#!/usr/bin/env python
import rospy
import requests
from bs4 import BeautifulSoup
from hbc_msgs.msg import MailStamped

class Loop_readMail(object):
	def __init__(self):
		self.pub_mail = rospy.Publisher('/mail', MailStamped, queue_size=1)
		self.publishMail()

	def publishMail(self):
		while not rospy.is_shutdown():
			peopleNo,kind,mailNo,mailNum,send = self.getUserInfo()  # get data from the server
			self.printUserInfo(peopleNo,kind,mailNo,mailNum,send)  #optional
			
			for i in range(len(send)):
				# 1.The employee is in the company.
				# 2.There are still mails that are not received.
				# 3.Haven't sent a query yet.
				if(send[i]=="1" and int(mailNum[i])>0):
					# publish to mail_trigger.py
					override_msg = MailStamped()				
					override_msg.data = True
					override_msg.ID = peopleNo[i]
					override_msg.mailNum = mailNum[i]
					self.pub_mail.publish(override_msg)
					
					# set the inquiry(send) column to 0
					sendData = {'mailNo':int(mailNo[i]),'tt':'false','token':'7XWE32L52T03DH61'}
					r = requests.get("http://maplericemilk.ddns.net/setsend.php",params=sendData)
	
	def getUserInfo(self):
		sendData = {'token':'7XWE32L52T03DH61'}
		r = requests.get("http://maplericemilk.ddns.net/read.php",params=sendData)
		sp = BeautifulSoup(r.text,'html.parser')
		peopleNo = []
		kind = []
		mailNo = []
		mailNum = []
		send = []
		amount = sp.select("#amount")[0].text
		for i in range(int(amount)):
			peopleNo.append(sp.select("#peopleNo"+str(i))[0].text.encode('utf-8'))
			kind.append(sp.select("#kind"+str(i))[0].text.encode('utf-8'))
			mailNo.append(sp.select("#mailNo"+str(i))[0].text.encode('utf-8'))
			send.append(sp.select("#send"+str(i))[0].text.encode('utf-8'))
		for i in range(len(peopleNo)):
			sendData = {'stuffID':peopleNo[i],'token':'7XWE32L52T03DH61'}
			r = requests.get("http://maplericemilk.ddns.net/mailNum.php",params=sendData)
			sp = BeautifulSoup(r.text,'html.parser')
			mailNum.append(sp.select("#mailNum")[0].text.encode('utf-8'))
		return peopleNo,kind,mailNo,mailNum,send
	
	def printUserInfo(self,peopleNo,kind,mailNo,mailNum,send):
		print("peopleNo: " + str(peopleNo))
		print("kind: " + str(kind))
		print("mailNo: " + str(mailNo))
		print("mailNum: " + str(mailNum))
		print("send: " + str(send))
	
if __name__ == "__main__":
	rospy.init_node("loop_readMail",anonymous=False)
	loop_readMail = Loop_readMail()
	rospy.spin()