#!/usr/bin/env python
import rospy
import requests
from bs4 import BeautifulSoup
from hbc_msgs.msg import MailStamped

class Get_ID_mail(object):
	def __init__(self):
		self.pub_mail = rospy.Publisher('/mail', MailStamped, queue_size=1)
		self.publishMail()

	def publishMail(self):
		while not rospy.is_shutdown():
			sendData = {'stuffName':'blackblackhuangyeeeeee','token':'7XWE32L52T03DH61'}
			r = requests.get("http://maplericemilk.ddns.net/getId.php",params=sendData)
			sp = BeautifulSoup(r.text,'html.parser')
			stuffNo = sp.select("#stuffNo")[0].text
			sendData = {'stuffID':stuffNo,'token':'7XWE32L52T03DH61'}
			r = requests.get("http://maplericemilk.ddns.net/mailNum.php",params=sendData)
			sp = BeautifulSoup(r.text,'html.parser')
			
			override_msg = MailStamped()                
			override_msg.data = True
			override_msg.ID = sp.select("#stuffNo")[0].text
			override_msg.mailNum = sp.select("#mailNum")[0].text
			#override_msg.ID = "U61f94258daedd7a7e8c2b9519e64e13b"
			#override_msg.mailNum = "2"
			self.pub_mail.publish(override_msg)
			print("publish Successfully!")
			rospy.sleep(5)

if __name__ == "__main__":
	rospy.init_node("get_ID_mail",anonymous=False)
	get_ID_mail = Get_ID_mail()
	rospy.spin()