Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run "pythonw.exe ""C:\FULL\PATH\background_tracker.py""", 0
Set WinScriptHost = Nothing
