from utils.general import string_to_boolean, roundup_nearest_ten, roundup_nearest_one

def compute_temperature_settings(temperature_value, temperature_type):

    if temperature_type == "celsius":
        return convert_from_celsius(temperature_value)

    if temperature_type == "celsius_fan":
        return convert_from_celsius_fan(temperature_value)

    if temperature_type == "fahrenheit":
        return convert_from_fahrenheit(temperature_value)

    if temperature_type == "gas_mark":
        return convert_from_gas_mark(temperature_value)

def create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark, user_temperature_type):

    temperature_object = {
        "celsius": str(celsius),
        "celsius_fan": str(celsius_fan),
        "fahrenheit": str(fahrenheit),
        "gas_mark": str(gas_mark),
        "user_temperature_type": user_temperature_type
    }
    return temperature_object

def convert_from_celsius(temperature_value):
    celsius = temperature_value
    celsius_fan = temperature_value - 20
    fahrenheit = roundup_nearest_ten(int((celsius * 9/5) + 32))
    gas_mark = roundup_nearest_one(int((celsius - 121) / 14))
    user_temperature_type = 0
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark, user_temperature_type)

def convert_from_celsius_fan(temperature_value):
    celsius = temperature_value + 20
    celsius_fan = temperature_value
    fahrenheit = roundup_nearest_ten(int((celsius * 9/5) + 32))
    gas_mark = roundup_nearest_one(int((celsius - 121) / 14))
    user_temperature_type = 1
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark, user_temperature_type)

def convert_from_fahrenheit(temperature_value):
    celsius = roundup_nearest_ten(int((temperature_value - 32) * 5/9))
    celsius_fan = celsius - 20
    fahrenheit = temperature_value
    gas_mark = roundup_nearest_one(int((celsius - 121) / 14))
    user_temperature_type = 2
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark, user_temperature_type)

def convert_from_gas_mark(temperature_value):
    celsius = roundup_nearest_ten(int((temperature_value * 14) + 121))
    celsius_fan = celsius - 20
    fahrenheit = roundup_nearest_ten(int((celsius * 9/5) + 32))
    gas_mark = temperature_value
    user_temperature_type = 3
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark, user_temperature_type)
