class Battery:
    def get_battery_capacity(battery='BAT1'):
        with open(f'/sys/class/power_supply/{battery}/capacity', 'r') as file:
            res = int(file.read())
        return res

    def get_battery_health_in_percentage(battery='BAT1'):
        with open(f'/sys/class/power_supply/{battery}/charge_full_design') as file:
            max_bat_health = file.read()
        with open(f'/sys/class/power_supply/{battery}/charge_full') as file:
            res = round(int(file.read()) / int(max_bat_health) * 100, 1)
        return res

    def get_battery_charging_status(battery='BAT1'):
        res = False
        with open(f'/sys/class/power_supply/{battery}/status', 'r') as file:
            status = file.read()[:-1]
            if status in ('Charging', 'Full', 'Not charging'):
                res = True
        return res


print(Battery.get_battery_capacity())
print(Battery.get_battery_health_in_percentage())
print(Battery.get_battery_charging_status())
