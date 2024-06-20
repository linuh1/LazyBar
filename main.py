from battery import Battery
import time

while True:
    print(str(Battery.get_battery_capacity()) + '%')
    print(str(Battery.get_battery_health_in_percentage()) + '%')
    if Battery.get_battery_charging_status():
        print('Charging')
    else:
        print('Not charging')
    time.sleep(1)
    print('\n' * 30)
