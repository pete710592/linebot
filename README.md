【Linebot on RaspberryPi】<br><br>



Install
-------
    $ pip install line-bot-sdk
    $ pip install line-bot-sdk
    $ pip install flask
    $ cd ~/duckietown/catkin_ws/src
    $ git clone https://github.com/pete710592/linebot.git



Current status
-------
**1. Line17**
```python
title='Duckiebot #01'
```
我目前是假定一個機器人做問問題的動作

**2. Line21,26**
```python
PostbackTemplateAction(
	label='drop it for me',  # displayed on the screen
	text='action #101',  # after push the button, displayed in the dialog
	data='action=buy&itemid=1'
),
MessageTemplateAction(
	label='get it by myself',  # displayed on the screen
	text='action #102'  # after push the button, displayed in the dialog
)
```
  PostbackTemplateAction,MessageTemplateAction 這兩個功能不知道差在哪，還要查

**3. Line18**
```python
text='You have 2 mails. \nWhat can I do for you?'
```
  幾封信是需要接收的



Reference
-------
https://xiaosean.github.io/chatbot/2018/04/10/LineChatbot/