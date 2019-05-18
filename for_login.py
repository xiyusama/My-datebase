# _*_  coding: utf-8  _*_
#导入selenium模块
from selenium import webdriver
from time import sleep
#导入显性等待模块
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import HTMLTestRunner

#建立class类
class Login(unittest.TestCase):
	#初始化工作
	def setUp(self):
		print("初始化工作开始")
		#注意需要把self入参
		self.driver = webdriver.Chrome()
		self.driver.get("http://www.baidu.com")
		print(self.driver.title)
		self.driver.implicitly_wait(4)
	
	#结束工作
	def tearDown(self):
		print("测试完成")
	
	#开始封装用例
	def test_login(self):
		print("用例开始")

		#输入账号密码并登陆,注意先清除以防止缓存数据
		try:
			#把self.driver赋值给driver
			driver = self.driver
			#用例执行
			driver.find_element_by_css_selector("#u1 > a.lb").click()
			driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
			driver.find_element_by_id("TANGRAM__PSP_10__userName").clear()
			driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("659161420")
			driver.find_element_by_id("TANGRAM__PSP_10__password").clear()
			driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("abc19852013")
				
			cli = driver.find_element_by_id("TANGRAM__PSP_10__submit")
			

			
			# 利用ActionChains鼠标键盘行为来实现点击登录按钮
			ActionChains(driver).click(cli).perform()

			
			sleep(20)
			usr_name = driver.find_element_by_class_name("user-name")
			print("ok")
			print(usr_name.text)

		except:
			driver.get_screenshot_as_file("./error.png")
			print("fail")



		finally:
			print("test finished")

if __name__ == '__main__':
	unittest.main()

	suite = unittest.TestSuite()
	suite.addTest(Login("test_login"))
	fp = open("./result.html","wb")
	# stream定义一个测试报告写入的文件，title就是标题，description就是描述
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"登录测试报告",description=u"测试用例执行情况")
	runner.run(suite)
	fp.close()










