# coding=utf-8
import os
import time
from Log import log
from Config import config
from selenium import webdriver
from appium import webdriver as app_driver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

config = config.MyConfig()
log = log.MyLog


def describe(func):
    def function(*args, **kwargs):
        i = 1
        while i <= 3:
            try:
                # 给对浏览器的每个操作加上日志记录
                if func.__name__ == 'chrome_driver':
                    log.info('启动谷歌浏览器并最大化窗口')
                elif func.__name__ == 'open':
                    log.info('打开 ' + (args[0].url)[1] + ' 页面')
                elif func.__name__ == 'wait':
                    log.info('等待 ' + str(args[1]) + ' 秒')
                elif func.__name__ == 'input':
                    log.info('在 ' + args[1][1] + ' 输入：' + args[2])
                elif func.__name__ == 'click':
                    log.info('点击 ' + args[1][1])
                elif func.__name__ == 'get_text':
                    log.info('获取 ' + args[1][1] + ' 的文本属性')
                elif func.__name__ == 'clear':
                    log.info('清空 ' + args[1][1] + ' 的字符')
                elif func.__name__ == 'get_attribute':
                    log.info('获取 ' + args[1][1] + ' 的属性：' + args[2] + '的值')
                elif func.__name__ == 'get_title':
                    log.info('获取页面的标题')
                elif func.__name__ == 'switch_to_frame':
                    log.info('切换到 ' + args[1][1])
                elif func.__name__ == 'switch_to_content':
                    log.info('退出frame，回到页面')
                elif func.__name__ == 'js':
                    log.info('执行js: ' + args[1][1])
                elif func.__name__ == 'right_click':
                    log.info('模拟鼠标右击 ' + args[1][1])
                elif func.__name__ == 'double_click':
                    log.info('模拟鼠标双击 ' + args[1][1])
                elif func.__name__ == 'move_to_element':
                    log.info('模拟鼠标悬停在 ' + args[1][1])
                elif func.__name__ == 'drag_and_drop':
                    log.info('模拟鼠标把元素 ' + args[1][1] + ' 拖拽到 ' + args[2][1])
                elif func.__name__ == 'switch_to_windows_by_title':
                    log.info('浏览器窗口切换到 ' + args[1])
                elif func.__name__ == 'forward':
                    log.info('浏览器前进')
                elif func.__name__ == 'back':
                    log.info('浏览器后退')
                elif func.__name__ == 'refresh':
                    log.info('刷新当前页面')
                elif func.__name__ == 'close':
                    log.info('关闭当前窗口')
                elif func.__name__ == 'is_element_exist':
                    log.info('判断元素 ' + args[1][1] + ' 是否存在')
                elif func.__name__ == 'quit':
                    log.info('退出浏览器')
                elif func.__name__ == 'android_app_driver':
                    log.info('启动安卓app')
                elif func.__name__ == 'ios_app_driver':
                    log.info('启动iOS app')
                elif func.__name__ == 'click_coordinates':
                    log.info('点击屏幕，横纵坐标位置比例(' + args[1][1] + ',' + args[2][1] + ')')
                elif func.__name__ == 'switch_h5':
                    log.info('切换到app h5页面')
                elif func.__name__ == 'switch_app':
                    log.info('切换到app原生页面')
                elif func.__name__ == 'enableAppiumUnicodeIME':
                    log.info('设置appium输入法生效')
                elif func.__name__ == 'enableSogouIME':
                    log.info('设置搜狗输入法生效')
                elif func.__name__ == 'quit_app':
                    log.info('关闭app')
                else:
                    log.error('未知操作')

                ret = func(*args, **kwargs)
                break
            except:
                log.warning('操作失败%s次' % i)
                if i == 3:
                    curr_path = os.path.dirname(os.path.realpath(__file__))
                    image_name = os.path.join(os.path.dirname(curr_path),
                                              'TestReport',
                                              'images',
                                              time.strftime("%Y_%m_%d_%H_%M_%S") + '.png')
                    log.error('不再重试，可通过记录日志的时间找到对应的截图～')
                    args[0].driver.get_screenshot_as_file(image_name)
                    raise
                i += 1
        return ret

    return function


@describe
def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


@describe
def android_app_driver(appPackage, appActivity):
    # 启动安卓app

    app_parameters = {
        'platformName': 'Android',
        'platformVersion': 'x.x',
        'deviceName': 'xxx',
        'appPackage': appPackage,
        'appActivity': appActivity,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'noSign': True,
        # 'app': r'D:\app\test.apk'
        # 'newCommandTimeout': '70'
    }
    return app_driver.Remote('http://127.0.0.1:4723/wd/hub', app_parameters)


@describe
def ios_app_driver(bundleId, udid):
    # 启动iOS app

    app_parameters = {
        'platformName': 'ios',
        'platformVersion': 'x.x',
        'deviceName': 'xxx',
        'bundleId': bundleId,
        'udid': udid,
    }
    return app_driver.Remote('http://127.0.0.1:4723/wd/hub', app_parameters)


@describe
def quit(driver):
    driver.quit()


@describe
def quit_app(driver):
    driver.quit()


class WebBaseUI:
    pc_host = config.get_conf('web_ui', 'pc_host')

    def __init__(self, driver, pc_host=pc_host):
        self.pc_host = pc_host
        self.driver = driver

    def locate_element(self, loc):
        time.sleep(0.5)
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(loc[0]))

    @describe
    def open(self):
        self.driver.get(self.pc_host + self.url[0])

    @describe
    def wait(self, sec):
        time.sleep(sec)

    @describe
    def click(self, loc):
        self.locate_element(loc).click()

    @describe
    def clear(self, loc):
        self.locate_element(loc).clear()

    @describe
    def input(self, loc, text):
        self.locate_element(loc).send_keys(text)

    @describe
    def get_attribute(self, loc, attribute):
        return self.locate_element(loc).get_attribute(attribute)

    @describe
    def get_text(self, loc):
        return self.locate_element(loc).text

    @describe
    def get_title(self):
        return self.driver.title

    @describe
    def js(self, js):
        self.driver.execute_script(js[0])

    @describe
    def switch_to_frame(self, loc):
        self.driver.switch_to.frame(self.locate_element(loc))

    @describe
    def switch_to_content(self):
        self.driver.switch_to.default_content()

    @describe
    def right_click(self, loc):
        ActionChains(self.driver).context_click(self.locate_element(loc)).perform()

    @describe
    def double_click(self, loc):
        ActionChains(self.driver).double_click(self.locate_element(loc)).perform()

    @describe
    def move_to_element(self, loc):
        ActionChains(self.driver).move_to_element(self.locate_element(loc)).perform()

    @describe
    def drag_and_drop(self, loc1, loc2):
        element1 = self.locate_element(loc1)
        element2 = self.locate_element(loc2)
        ActionChains(self.driver).drag_and_drop(element1, element2).perform()

    @describe
    def switch_to_windows_by_title(self, title):
        """
        切换到指定标题的窗口
        :param title: 窗口标题
        :return: 当前窗口的句柄
        """

        current = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if (self.driver.title.__contains__(title)):
                break
        return current

    @describe
    def forward(self):
        self.driver.forward()

    @describe
    def back(self):
        self.driver.back()

    @describe
    def refresh(self):
        self.driver.refresh()

    @describe
    def is_element_exist(self, loc):
        try:
            self.locate_element(loc)
            log.info('页面元素存在')
            return True
        except:
            log.info('页面元素不存在')
            return False

    @describe
    def close(self):
        self.driver.close()


class AppBaseUI:
    def __init__(self, driver):
        self.driver = driver

    def locate_element(self, loc):
        time.sleep(0.5)
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(loc[0]))

    @describe
    def click(self, loc):
        self.locate_element(loc).click()

    @describe
    def clear(self, loc):
        self.locate_element(loc).clear()

    @describe
    def input(self, loc, text):
        self.locate_element(loc).send_keys(text)

    @describe
    def is_element_exist(self, loc):
        try:
            self.locate_element(loc)
            log.info('app元素存在')
            return True
        except:
            log.info('app元素不存在')
            return False

    @describe
    def click_coordinates(self, locationx, locationy):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * locationx)
        y1 = int(y * locationy)
        self.driver.swipe(x1, y1, x1, y1, 500)

    @describe
    def switch_h5(self, h5_name):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": h5_name})

    @describe
    def switch_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})

    @describe
    def enableAppiumUnicodeIME(self):
        os.system('adb shell ime set io.appium.android.ime/.UnicodeIME')

    @describe
    def enableSogouIME(self):
        os.system('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
