
class Temperature:
    """Stores a representation of a temperature in Kelvin, Celsius,
    and Fahrenheit."""

    def __init__(self, kelvin: float, celsius: float, fahrenheit: float):
        """Creates a Temperature object.
        
        Args:
            kelvin: The temperature in units of Kelvin.
            celsius: The temperature in units of Celsius.
            fahrenheit: The temperature in units of Fahrenheit.
        """
        self.kelvin = kelvin
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def get_kelvin(self) -> float:
        """Returns the Kelvin representation of this Temperature object."""
        return self.kelvin

    def get_celsius(self) -> float:
        """Returns the Celsius representation of this Temperature object."""
        return self.celsius

    def get_fahrenheit(self) -> float:
        """Returns the Fahrenheit representation of this Temperature object."""
        return self.fahrenheit

class Thermometer:
    """Thermometer object that can placed at a location defined by a latitude
    and longitude then used to get the current temperature at the location."""

    def __init__(self, lat: float, long: float):
        """Creates a Thermometer object for the provided latitude and longitude.

        Args:
            lat: The latitude of the thermometer.
            long: The longitude of the thermometer.
        """
        self.lat = lat
        self.long = long

    def current_temp() -> Temperature:
        """Returns the current temperature at the thermometer's postition.

        Returns:
            A Temperature object representing the current temperature at the
            thermometer in Kelvin, Celsius, and Fahrenheit.
        """
        return None