#coding=utf-8
import smtplib
import os ,time,datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

class MailUtils():
	#表示一个类方法，不需要实例化，可以直接调用
	@classmethod
	def send_test_report(cls):
		#邮件信息配置. 授权码 
		sender = '18676748367@163.com'
		receiver = '1248379494@qq.com' 
		auth_code = 'Maze123'  #设置客户端授权码，不是密码

		smtpserver = 'smtp.163.com'
		subject = '自动化测试报告'

		#读取文件内容
		f = open("./result.html", 'rb')
		mail_body = f.read()
		f.close()

		#HTML 形式的文件内容
		html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
		html['Subject'] = subject
		html['from'] = sender
		html['to'] = receiver

		消息体内容
		msg = MIMEText("<html> <h2>大家好，这是今天的测试报告</h2></html>",_subtype="html",_charset="utf-8")
		msg["Subject"] = subject
		msg["from"] = sender
		msg["to"] = receiver

		# html附件 将测试报告放在附件中发送
		att1 = MIMEText(mail_body, 'base64', 'gb2312')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = 'attachment; filename="baidu_result.html"'  # 这里的filename可以任意写



		msg = MIMEMultipart()
		msg['Subject'] = subject  # 邮件的标题
		msg.attach(html)  # 将html附加在msg里
		msg.attach(att1)  # 新增一个附件 



		#连接 登录 上smtp服务器
		smtp = smtplib.SMTP() 
		smtp.connect('smtp.163.com') 
		smtp.login(sender, auth_code) 

		#发送邮件
		smtp.sendmail(sender, receiver, msg.as_string()) 
		smtp.quit()