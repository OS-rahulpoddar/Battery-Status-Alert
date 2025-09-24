## Getting Started
To get this running locally, please follow the below steps:
1. Install python.
2. Install the dependencies of this project by runnig the following commands:
    - `pip install psutil`
    - `pip install pyttsx3`
3. Test it via running locally:
    - `python battery_status.py`

## Run this as background app. during the windows/system start
To get this running as background app. during the windows/system start, please follow the below steps:
1. Convert this into an executable file.
2. To do that, Install PyInstaller
    - `pip install pyinstaller`
3. Run the PyInstaller Command
    - `pyinstaller --onefile your_script_name.py`
4. Find Your Executable inside the `dist` folder.
5. In case u want this battery_status.exe to run every time you start your windows, then navigate to the Startup folder: Type `shell:startup` into the Run dialog box and press `Enter`. This will open the Startup folder for your current user account.
6. Drag and drop this `exe` into the Startup folder window you opened.

That's it! The next time you log in, the program will automatically start.