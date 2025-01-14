python.exe -m venv spmls && ^
spmls\Scripts\activate.bat && ^
python.exe -m pip install --upgrade pip && ^
python.exe -m pip install -r requirements.txt && ^
python.exe spotify_playlist_multi-level_sorting.py Spotify_Client_ID Spotify_Client_Secret && ^
spmls\Scripts\deactivate.bat && ^
rmdir spmls /s /q