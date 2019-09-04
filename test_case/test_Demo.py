import pytest
import allure

class TestDemo:

    @allure.severity("blocker")
    def test_demo1(self):
        print("i am test_demo1")
        assert True

    @allure.step("test demo Two")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_demo2(self):
        print("i am test_demo2")
        assert False

    @allure.step("test demo 3")
    @allure.severity("blocker")
    def test_demo3(self):
        allure.attach("this is demo3 attach")
        print("i am test_demo3")
        assert False


