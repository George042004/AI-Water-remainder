Set WinScriptHost = CreateObject("WScript.Shell")
' Replace the path below with your actual path to background_tracker.py
WinScriptHost.Run "pythonw.exe ""C:\Users\chitt\background_tracker.py""", 0
Set WinScriptHost = Nothing
