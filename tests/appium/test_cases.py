# doing one action using the webdriver
import instappium

session = instappium.InstAppium(username='xxx', password='yyy', device='emulator-5554', show_logs=True)

session._webdriver.go_search('whoever you want', 'accounts')


# doing one action using the FSM
from instappium.engine import FSMSession
fsm = FSMSession(session._webdriver)

# should respond idle
fsm.state

# let's go to the home page
fsm.go_homepage()
