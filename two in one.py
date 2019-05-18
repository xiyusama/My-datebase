#coding=utf-8
import unittest
import HTMLTestRunner
import for_login , for_search
import time
import smtplib
import os ,time,datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from mail import MailUtils

#创建测试集合
def create_suite():
    print("测试开始")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(for_search.Search))
    suite.addTest(unittest.makeSuite(for_login.Login))
    return suite


if __name__ == '__main__':
    
    suite = create_suite()

    #文件名中加了当前时间，为了每次生成不同的测试报告
    #file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())

    #创建测试报告，此时这个文件还是空文件 wb 以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖，不存在则创建
    fp = open("./result.html","wb")
   
    # stream定义一个测试报告写入的文件，title就是标题，description就是描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度测试报告",description=u"测试用例执行情况",verbosity=2)
    runner.run(suite)
    fp.close()

    MailUtils.send_test_report()