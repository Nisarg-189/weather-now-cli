from weather.api import get_weather

def main():

    print("==== Weather App ====")

    lat = float(input("Enter latitude: "))
    lon = float(input("Enter longitude: "))

    weather = get_weather(lat,lon)

    if "error" in weather:
        print("Something went wrong! ", weather["error"])

    else:
        print("---- Current Weather ----")
        print("Temperature: ", weather["temperature"], "°C")
        print("Wind Speed: ", weather["windspeed"], "km/h")
        print("Wind Direction: ", weather["winddirection"], "°")
        print("Time: ", weather["time"] )


if __name__ == "__main__":
    main()
