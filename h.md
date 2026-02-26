#  Host the app on local network like- (http://127.0.0.1:5000)

# Option A — Activate the conda env and run app.py (recommended):

cd "C:\Users\harsh\OneDrive\Desktop\miner project\Phishing-URL-Detection"
python app.py

# Option B — Run directly with the conda env's Python (no activation needed):
 
& "C:\Users\harsh\miniconda3\envs\phish-py310\python.exe" "C:\Users\harsh\OneDrive\Desktop\miner project\Phishing-URL-Detection\app.py" 

# Option C — Use flask run and explicitly bind to 127.0.0.1:

cd "C:\Users\harsh\OneDrive\Desktop\miner project\Phishing-URL-Detection"
$env:FLASK_APP='app.py'
& "C:\Users\harsh\miniconda3\envs\phish-py310\python.exe" -m flask run --host=127.0.0.1 --port=5000



# Host the app on LAN local area network like- (http://192.168.1.4:5000)

cd "C:\Users\harsh\OneDrive\Desktop\miner project\Phishing-URL-Detection"
$env:FLASK_APP='app.py'
& "C:\Users\harsh\miniconda3\envs\phish-py310\python.exe" -m flask run --host=0.0.0.0 --port=5000

