import instappium

session = instappium.InstAppium(username='xxx', password='yyy', device='emulator-5554', show_logs=True)

session._webdriver.go_search('watermelodie', 'accounts')
