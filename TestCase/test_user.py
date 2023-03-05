# coding=utf-8
import allure
from Page.login_page import LoginPage


@allure.feature("用户模块")
@allure.story("PC端用户相关功能")
class TestUser:

    @allure.title("登录")
    def test_login(self, driver):
        """验证可登录成功"""

        lp = LoginPage(driver)
        lp.open()
        lp.input(lp.username_input_box, 'xxx')
        lp.input(lp.password_input_box, 'xxx')
        lp.click(lp.login_button)
        lp.wait(3)
        actual_result = lp.get_text(lp.current_user)
        assert actual_result == "xxx"



