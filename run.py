import os
import time

while True:
    my_time = time.strftime('%H_%M')
    if my_time == '18_00':
        os.system('pytest')
        os.system('allure generate Temp -o TestReport/Report --clean')
        break
    else:
        time.sleep(5)
        print(time.strftime('%H_%M_%S'))
