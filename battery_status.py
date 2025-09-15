import psutil
import time
import pyttsx3

def speak(message: str):
    engine = pyttsx3.init("sapi5")   # reinitialize each time
    print("🔊 Speaking:", message)  # Debug log
    engine.say(message)
    engine.runAndWait()
    engine.stop()  # release resources

def check_battery():
    while True:
        battery = psutil.sensors_battery()
        if battery is None:
            print("Battery information not available.")
            break

        percent = battery.percent
        charging = battery.power_plugged

        if percent < 25 and not charging:
            alert_msg = f"Warning! Battery low: {percent} percent. Please plug in the charger."
            speak(alert_msg)

        elif percent > 95 and charging:
            alert_msg = f"Battery charged {percent} percent. Please unplug the charger."
            speak(alert_msg)

        else:
            print(f"Battery: {percent}% | {'Charging' if charging else 'Not Charging'}")

        time.sleep(120)  # repeat every 2 minutes

if __name__ == "__main__":
    check_battery()
