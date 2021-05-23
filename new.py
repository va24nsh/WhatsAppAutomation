from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("Enter chat name or group name: ")
msg = input("Enter your message: ")
count = int(input("Enter count: "))

input("Enter anything after scaning QR code")

# //*[@id="pane-side"]/div[1]/div/div/div[13]/div/div/div/div[2]/div[1]/div[1]/span
# //*[@id="main"]/footer/div[1]/div[2]/div/div[2]
# //*[@id="main"]/footer/div[1]/div[3]/button/span

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for index in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span").click()

print("Success")
