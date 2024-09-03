"""
Will run a release build of the game

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""
from setuptools import setup, Command
import subprocess

class BuildPyInstallerCommand(Command):
    """Custom command to run PyInstaller."""
    description = "Build executable using PyInstaller"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Run the PyInstaller build command
        subprocess.run([
            "pyinstaller", "--onefile", "--add-data=audio/*;audio", "--add-data=graphics/*;graphics", "--add-data=dev/audio/audio_sources.txt;audio", "--icon=dev/graphics/icon.ico", "--name=Monopoly", "--noconsole", "main.py"
        ], check=True)

setup(
    name="Monopoly",
    version="0.1",
    description="A digital version of the classic board game",
    cmdclass={
        "build_exe": BuildPyInstallerCommand,
    },
)