Install
-------
    $ pip install line-bot-sdk
    $ pip install flask
    $ cd ~/duckietown/catkin_ws/src
    $ git clone https://github.com/pete710592/linebot.git
    $ git clone https://github.com/pete710592/hbc_msgs.git



Current status
-------
mail_trigger.py目前是用來「觸發」Linebot用的<br>
他會產生選項讓使用者選擇，當使用者決定好要哪個選項時，會觸發到app.py內的內容

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
目前暫時先假定有2封信，到時候會有幾封信是需要接收的還要再改(subscribe)



Reference
-------
https://xiaosean.github.io/chatbot/2018/04/10/LineChatbot/
