from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import random
import time



# driver.refresh()
# driver.quit()
# 拖动滑块
def test_slide():
    # 定位到密码登录
    btn_login = driver.find_element_by_xpath('//*[@id="normalLogin"]')
    ActionChains(driver).click(btn_login).perform()

    # 滑块按钮及其位置
    btn_slide = driver.find_element_by_xpath('//*[@id="nc_2_n1z"]')
    btn_slide_location = btn_slide.location
    print('滑块位置=', btn_slide_location)

    # 滑动条大小
    span_bg = driver.find_element_by_xpath('//*[@id="nc_2__scale_text"]/span')
    span_bg_size = span_bg.size
    print('滑动条大小', span_bg_size)

    # 滑块位移
    x_offset = span_bg_size['width']
    y_offset = 0

    # 抓住滑块
    ActionChains(driver).click_and_hold(btn_slide).perform()
    sum = 0
    while(True):
        i = random.randint(65, 105)
        if x_offset - sum <= 105:
            ActionChains(driver).move_by_offset(x_offset, y_offset).perform()
            break
        ActionChains(driver).move_by_offset(i, y_offset).perform()
        if x_offset - sum <= 0:
            ActionChains(driver).move_by_offset(x_offset, y_offset).perform()
            break
        sum += i
    # 释放滑块
    ActionChains(driver).release(btn_slide).perform()
    test_img()

# 检测图片是否已经产生
def test_img():
    try:
        # 如果检测到图片
        if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath('//*[@id="nc_2_clickCaptcha"]/div[2]/img')):

            # 图片操作
            img = driver.find_element_by_xpath('//*[@id="nc_2_clickCaptcha"]/div[2]/img')
            img_location = img.location
            # 所要查找的字
            # char = driver.find_element_by_xpath('//*[@id="nc_2__scale_text"]/i').xpath('string(.)').extract()[0]
            # print(char)
            print(img_location)
        elif WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath('//*[@id="nc_2__imgCaptcha_img"]/img')):
            print('123====')
            submit = driver.find_element_by_xpath('//*[@id="nc_2_scale_submit"]')
            ActionChains(driver).click(submit).perform()
            pass
    except:
        driver.refresh()
        test_slide()
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.qichacha.com/user_login")
    driver.maximize_window()
    test_slide()

