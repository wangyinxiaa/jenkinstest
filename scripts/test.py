import allure
def test_a():
    print("aaa")
    assert 1
@allure.step(title="测试步骤001")
def test_login():
    allure.attch("登录","输入用户名")
    print("aaa")
    allure.attach("登录","输入密码")
    print("bbb")
    allure.attch("登录","点击登录")
    print("aaa")
    assert 0


