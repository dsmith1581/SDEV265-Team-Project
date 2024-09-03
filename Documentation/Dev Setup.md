# Microsoft Windows
Install the latest Python 3.11.x release. Newer releases are not currently supported by Python Arcade.

Once installed, run `pip install -r requirements.txt` in the root directory of the project.

# Building Release
In the root directory run the following command to package the application: `pyinstaller --onefile --add-data "audio/*;audio" --add-data "graphics/*;graphics" main.py`. It may take a minute for this to complete.

Note: The build artifacts will be ./dist/main.exe
