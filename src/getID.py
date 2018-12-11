#!/usr/bin/env python
import rospy
import requests
from bs4 import BeautifulSoup

class GetID(object):
	def __init__(self):
		sendData = {'stuffName':'blackblackhuangyeeeeee','token':'7XWE32L52T03DH61'}
		r = requests.get("http://maplericemilk.ddns.net/getId.php",params=sendData)
		sp = BeautifulSoup(r.text,'html.parser')
		print(sp.select("#stuffNo")[0].text)

if __name__ == "__main__":
	rospy.init_node("getID",anonymous=False)
	getID = GetID()
	rospy.spin()