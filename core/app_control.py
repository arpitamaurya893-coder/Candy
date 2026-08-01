import os
import subprocess
import webbrowser

from config.app_paths import APP_PATHS


class AppControl:

    def execute(self, command):

        command = command.lower()

        # ---------- Browser ----------
        if any(x in command for x in [
            "open browser",
            "browser kholo",
            "open chrome",
            "chrome kholo",
            "open internet",
            "internet kholo"
        ]):

            chrome_path = APP_PATHS.get("chrome")

            if os.path.exists(chrome_path):
                subprocess.Popen(chrome_path)
            else:
                webbrowser.open("https://www.google.com")

            return "Opening Chrome Boss."

        # ---------- Google ----------
        if any(x in command for x in [
            "open google",
            "google kholo",
            "google chalao"
        ]):

            webbrowser.open("https://www.google.com")
            return "Opening Google Boss."

        # ---------- YouTube ----------
        if any(x in command for x in [
            "open youtube",
            "youtube kholo",
            "mujhe youtube chahiye"
        ]):

            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube Boss."

        # ---------- Notepad ----------
        if any(x in command for x in [
            "open notepad",
            "notepad kholo"
        ]):

            subprocess.Popen("notepad")
            return "Opening Notepad Boss."

        # ---------- Calculator ----------
        if any(x in command for x in [
            "open calculator",
            "calculator kholo",
            "open calc"
        ]):

            subprocess.Popen("calc")
            return "Opening Calculator Boss."

        # ---------- File Explorer ----------
        if any(x in command for x in [
            "open file explorer",
            "file explorer kholo",
            "open explorer"
        ]):

            subprocess.Popen("explorer")
            return "Opening File Explorer Boss."

        # ---------- Camera ----------
        if any(x in command for x in [
            "open camera",
            "camera kholo"
        ]):

            os.system("start microsoft.windows.camera:")
            return "Opening Camera Boss."

        # ---------- VS Code ----------
        if any(x in command for x in [
            "open vs code",
            "open visual studio code",
            "vs code kholo"
        ]):

            path = APP_PATHS.get("vscode")

            if os.path.exists(path):
                subprocess.Popen(path)
                return "Opening VS Code Boss."

            return "VS Code path not found."

        # ---------- Spotify ----------
        if any(x in command for x in [
            "open spotify",
            "spotify kholo"
        ]):

            path = APP_PATHS.get("spotify")

            if os.path.exists(path):
                subprocess.Popen(path)
                return "Opening Spotify Boss."

            return "Spotify path not found."

        return None