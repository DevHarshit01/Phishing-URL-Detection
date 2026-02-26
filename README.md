# Phishing URL Detection

The Phishing URL Detection System is a machine-learning–based security tool designed to identify malicious or fraudulent URLs that attempt to steal sensitive user information. By analyzing key features of URLs—such as domain structure, HTTPS usage, suspicious patterns, and website behavior—the system classifies links as legitimate or phishing.

## Features
- Detect phishing URLs with high accuracy.
- Utilizes machine learning models for classification.
- Easy-to-use interface for URL analysis.
- Feature extraction from URLs for deep analysis.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Phishing-URL-Detection.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Phishing-URL-Detection
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Configure your environment variables in a `.env` file (see `.env.example`).
2. Run the application:
   ```bash
   python app.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000`.
4. Enter the URL you want to analyze and view the results.

## Model
The project uses a pre-trained machine learning model stored in the `pickle/` directory. 

## License
This project is licensed under the MIT License. See the LICENSE file for details.
