
# Gesture-Controlled Slides

This project allows you to control Google Slides or other slide presentations using hand gestures detected through a webcam.

## Features
- **Open Hand (5 fingers):** Move to the next slide.
- **Closed Hand (0 fingers):** Go back to the previous slide.

## Requirements
- Python 3.7 or later
- Webcam
- Compatible operating system (Windows, macOS, Linux)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/lucasadsr/gesture-controlled-slides.git
   cd gesture-controlled-slides
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script:
   ```bash
   python main.py
   ```

## Notes
- Press `q` to exit the program.
- Adjust the `action_interval` in the script if you want faster/slower response times.
