Start-Process -FilePath "python.exe" -ArgumentList "-m venv spmls" -NoNewWindow -Wait
.\spmls\Scripts\Activate.ps1
Start-Process -FilePath "python.exe" -ArgumentList "-m pip install --upgrade pip" -NoNewWindow -Wait
Start-Process -FilePath "python.exe" -ArgumentList "-m pip install -r requirements.txt" -NoNewWindow -Wait
Start-Process -FilePath "python.exe" -ArgumentList "spotify_playlist_multi-level_sorting.py Spotify_Client_ID Spotify_Client_Secret" -NoNewWindow -Wait
deactivate
Remove-Item -Path "spmls" -Recurse -Force
Remove-Item -Path ".\.cache" -Recurse -Force