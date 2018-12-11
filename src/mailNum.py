#!/usr/bin/env python
import rospy
import requests
from bs4 import BeautifulSoup

class MailNum(object):
	def __init__(self):
		sendData = {'stuffID':'U61f94258daedd7a7e8c2b9519e64e13b','token':'7XWE32L52T03DH61'}
		r = requests.get("http://maplericemilk.ddns.net/mailNum.php",params=sendData)
		sp = BeautifulSoup(r.text,'html.parser')
		print(sp.select("#mailNum")[0].text)

if __name__ == "__main__":
	rospy.init_node("mailNum",anonymous=False)
	mailNum = MailNum()
	rospy.spin()