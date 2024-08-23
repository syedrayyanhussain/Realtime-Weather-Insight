# WeatherInsight

WeatherInsight is a desktop application that provides real-time weather updates for any city globally. Designed with PyQt5 and powered by the OpenWeatherMap API, WeatherInsight offers an intuitive interface to check the current weather conditions, including temperature, weather description, and an appropriate weather emoji.

## Features

- **City Search**: Enter any city name to get the latest weather information.
- **Weather Details**: View temperature in Celsius, weather description, and a corresponding weather emoji.
- **Error Handling**: Clear and informative error messages for issues like bad requests or connectivity problems.

## Screenshot


![GUI of weather_app](https://github.com/syedrayyanhussain/Realtime-Weather-Insight/blob/master/GUI_Application.jpg)

## Installation

Follow these steps to get WeatherInsight up and running on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/WeatherInsight.git

2. **Navigate to the Project Directory**:
    cd WeatherInsight

3. **Install Required Packages:**:
    pip install PyQt5 requests python-dotenv

## Usage
1. **Run the Application:**:
   python weather_app.py

2. **Enter City Name**:
   python weather_app.py

## API Key
   To use the OpenWeatherMap API, you need an API key. Replace the OPENWEATHERMAP_API_KEY in your .creds file with your own API key. You can obtain one by signing up at OpenWeatherMap.

## Code Overview
**WeatherApp Class:** Main application class responsible for setting up the UI and managing weather data retrieval and display.

**get_weather Method:** Fetches weather data from OpenWeatherMap and handles various errors.

**display_weather Method:** Updates the UI with weather details including temperature and emoji.

**get_weather_emoji Method:** Returns an emoji based on the weather condition ID.

## Contributing
Anybody is welcome in contributions to improve WeatherInsight! If you have suggestions, bug fixes, or enhancements, please:

**Fork the Repository:** Create your own copy of the repository on GitHub.

**Create a Branch:** Develop your changes on a separate branch.

**Submit a Pull Request:** Propose your changes by submitting a pull request.

**Please ensure your code** adheres to our coding standards and includes relevant tests.

