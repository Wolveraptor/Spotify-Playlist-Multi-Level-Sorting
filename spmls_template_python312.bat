C:\Users\ssimon\AppData\Local\Programs\Python\Python312\python.exe -m venv spmls && ^
spmls\Scripts\activate.bat && ^
C:\Users\ssimon\AppData\Local\Programs\Python\Python312\python.exe -m pip install --upgrade pip && ^
C:\Users\ssimon\AppData\Local\Programs\Python\Python312\python.exe -m pip install -r requirements.txt && ^
C:\Users\ssimon\AppData\Local\Programs\Python\Python312\python.exe spotify_playlist_multi-level_sorting.py Spotify_Client_ID Spotify_Client_Secret && ^
spmls\Scripts\deactivate.bat && ^
rmdir spmls /s /q && ^
rmdir .\.cache /s /q && ^
rmdir .\Modules\__pycache__