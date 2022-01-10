import subprocess


def emulator_resize():
    scpt_launch = """
        tell application "Finder"
            set screen_resolution to bounds of window of desktop
        end tell
        tell application "System Events" to tell process "mGBA"
            set frontmost to true
            set position of window 1 to {(item 3 of screen_resolution) / 3.5, (item 4 of screen_resolution) / 4}
            set size of window 1 to {640, 480}
        end tell
    """
    result = subprocess.run(['osascript', '-e', scpt_launch])
    return result.stdout