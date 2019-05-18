# _*_ coding: utf-8 _*_
#导入对应模块
from selenium import webdriver
from time import sleep
#导入显性等待模块
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#导入nittest模块
import unittest
import HTMLTestRunner


#初始化工作
class Search(unittest.TestCase):
	def setUp(self):
		print("初始化工作开始")
		
		#驱动部分
		self.driver = webdriver.Chrome()
		
		self.driver.get("http://www.baidu.com")
		#打印标题title
		print(self.driver.title)

		#隐性等待
		self.driver.implicitly_wait(4)
		#定义初始数据
		
		self.Search_Box = "演员的自我修养"
	#结束时工作
	def tearDown(self):
		
		print("结束测试时的清除工作")
	#关闭浏览器
		self.driver.close()
	#搜索的测试用例进行封装
	def test_search(self):
		print("搜索的用例开始")
		driver = self.driver
		#定位文本搜索框，输入内容：演员的自我修养
		driver.find_element_by_class_name("s_ipt").send_keys("演员的自我修养")
		#点击搜索按钮
		driver.find_element_by_id("su").click()
		#仅测试提取文本信息
		judge = driver.find_element_by_class_name("pf")
		print (judge.text)

		self.assertEqual(self.Search_Box,"演员的自我修养",msg = "wrong")
		sleep(3)
		#清除输入框内容并点击搜索按钮，这个时候为百度首页
		driver.find_element_by_class_name("s_ipt").clear()
		driver.find_element_by_id("su").click()

		try:
			ele = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID,"kw")))
			ele.send_keys("ces")
			print("ok")


		except:
			print("fail")

		finally:
			print("test finished")




if __name__ == '__main__':
	unittest.main()
	
	suite = unittest.TestSuite()
	suite.addTest(Search("test_search"))


	fp = open("./result.html","wb")
	# stream定义一个测试报告写入的文件，title就是标题，description就是描述
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"搜索测试报告",description=u"测试用例执行情况")

	runner.run(suite)
	fp.close()

   



