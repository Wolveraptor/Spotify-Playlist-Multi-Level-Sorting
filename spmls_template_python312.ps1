Invoke-Command -ScriptBlock { python.exe -m venv spmls }
Invoke-Command -ScriptBlock { .\spmls\Scripts\Activate.ps1 }
Invoke-Command -ScriptBlock { python.exe -m pip install --upgrade pip }
Invoke-Command -ScriptBlock { python.exe -m pip install -r requirements.txt }
Invoke-Command -ScriptBlock { python.exe spotify_playlist_multi-level_sorting.py Spotify_Client_ID Spotify_Client_Secret }
Invoke-Command -ScriptBlock { Remove-Item -Path "spmls" -Recurse -Force }
Invoke-Command -ScriptBlock { Remove-Item -Path ".cache" -Recurse -Force }
Invoke-Command -ScriptBlock { Remove-Item -Path ".\Modules\__pycache__" -Recurse -Force }
Invoke-Command -ScriptBlock { deactivate }