import instappium
from instappium.common.model import User

session = instappium.InstAppium(username='xxx', password='yyy', device='emulator-5554', show_logs=True)

session._webdriver.go_user(User('watermelodie'))
