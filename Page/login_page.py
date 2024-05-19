# coding=utf-8
from Common.base_page import WebBaseUI
from selenium.webdriver.common.by import By


class LoginPage(WebBaseUI):
    """登录页面"""

    url = ["/user/login", "登录页面"]

    username_input_box = [(By.NAME, "username"), "用户名输入框"]

    password_input_box = [(By.NAME, "pwd"), "密码输入框"]

    login_button = [(By.XPATH, "//input[@type='submit']"), "登录按钮"]

    current_user = [(By.XPATH, "//div/strong"), "当前用户"]
