import sys
import requests
import creds
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt



class WeatherApp(QWidget):  
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_Input = QLineEdit(self)
        self.get_weather_button= QPushButton("Get Weather", self)
        self.temperature_label=QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label= QLabel(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle(" Weather App ")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_Input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_Input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_Input.setObjectName("city_Input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                           font-family: calibri;
                           }
            QLabel#city_label{
                           font-size: 40px;
                           font-style: Italic;
                           }             
            QLineEdit#city_Input{
                           font-size:40px;
                           }         
            QPushButton#get_weather_button{
                           font-size:30px;
                           font-weight: bold;
                           }   
            QLabel#temperature_label{
                           font-size:80px;
                           }
            QLabel#emoji_label{
                           font-family: 'Segoe UI Emoji', 'Apple Color Emoji', 'Noto Color Emoji', 'Segoe UI', sans-serif;
                            
                           font-size:120px;
                           }
            QLabel#description_label{
                           font-size:60px;
                           }
            
                           
                           """)
        self.get_weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        
        city= self.city_Input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={creds.api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            print(data)

            if data['cod']== 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden\nAccess denied")
                case 404:
                    self.display_error("Not Found\nCity Not Found")
                case 500:
                    self.display_error("Internal Server Error\nPlease try again later")
                case 502:
                   self.display_errort("Bad Gateway\nInvalid response from the server")
                case 503:
                   self.display_errort("Service Unavailable\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe Request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirections\nCheck the URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error (f"Request Error:\n{req_error}")
        

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size:30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()


    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size:75px;")
        temperature_k=data["main"]["temp"]
        temperature_c=temperature_k - 273.15
        temperature_f=(temperature_k *9/5 -459.67)
        weather_id=data["weather"][0]["id"]
        weather_description=data["weather"][0]["description"]
        
        
        self.description_label.setText(weather_description)
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.temperature_label.setText(f"{temperature_c:.0f}°C")
    @staticmethod
    def get_weather_emoji(weather_id):
        if weather_id >=200 and weather_id <=232:
            return "⛈"
        elif weather_id >=300 and weather_id <=321:
            return "🌦"
        elif weather_id >=500 and weather_id <=531:
            return  "🌧"
        elif weather_id >=600 and weather_id <=622:
            return "❄"
        elif weather_id >=701 and weather_id <=741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌬️"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif weather_id >= 801 and weather_id <=804:
            return "☁"


if __name__ == "__main__":
    app=QApplication(sys.argv)
    weather_app= WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())