# The Loose Coupling principle encourages reducing the dependencies between different components in a system.
# Loose coupling makes it easier to modify, replace, or extend individual components without affecting the entire system.


# Bad Example
class WeatherStation:
    def get_temperature(self):
        # Code for fetching temperature from a specific sensor
        temperature = SensorA().read_temperature()
        return temperature


class SensorA:
    def read_temperature(self):
        # Code specific to SensorA
        return 25.0


# Good Example
class WeatherStation:
    def __init__(self, temperature_sensor):
        self.temperature_sensor = temperature_sensor

    def get_temperature(self):
        # Code for fetching temperature using the provided sensor
        temperature = self.temperature_sensor.read_temperature()
        return temperature


class SensorA:
    def read_temperature(self):
        # Code specific to SensorA
        return 25.0


class SensorB:
    def read_temperature(self):
        # Code specific to SensorB
        return 26.5


# Client code
sensor_a = SensorA()
weather_station_a = WeatherStation(sensor_a)
temperature_a = weather_station_a.get_temperature()
print(f"Temperature from SensorA: {temperature_a}")

sensor_b = SensorB()
weather_station_b = WeatherStation(sensor_b)
temperature_b = weather_station_b.get_temperature()
print(f"Temperature from SensorB: {temperature_b}")
