from flask import Flask
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
  return 'Hello, Docker!'

@app.route('/selenium', methods=['GET'])
def selenium_test():
  print("sample test case started")

  # settings for selenium chrome driver
  options = Options()
  options.add_argument('--remote-debugging-port=9222')
  options.add_argument("--headless")
  options.add_argument("window-size=1400,1500")
  options.add_argument("--disable-gpu")
  options.add_argument("--no-sandbox")
  options.add_argument("start-maximized")
  options.add_argument("enable-automation")
  options.add_argument("--disable-infobars")
  options.add_argument("--disable-dev-shm-usage")

  driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)
  #driver=webdriver.firefox()
  #driver=webdriver.ie()

  #maximize the window size
  driver.maximize_window()

  #navigate to the url
  driver.get("https://www.google.com/")

  #identify the Google search text box and enter the value
  driver.find_element("name", "q").send_keys("javatpoint")
  time.sleep(3)

  #click on the Google search button
  driver.find_element("name", "btnK").send_keys(Keys.ENTER)
  time.sleep(3)

  #close the browser
  driver.close()

  print("sample test case successfully completed")

  return 'Hello, Selenium!'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
  