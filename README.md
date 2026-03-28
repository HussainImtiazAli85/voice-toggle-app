# Toggle App

A simple web-based toggle app where you can toggle 12 boxes on and off with beautiful animations.

## Features

✨ 12 interactive toggle boxes
✨ Click any box to toggle ON/OFF
✨ Real-time counter showing how many boxes are ON
✨ "All ON" button to enable all boxes at once
✨ "Reset All" button to turn off all boxes
✨ Beautiful gradient UI with smooth animations
✨ Flask backend with API endpoints

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to the project folder:**
   ```bash
   cd toogle-app
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   
   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your web browser and visit:**
   ```
   http://localhost:5000
   ```

3. **Start toggling!** Click any box to toggle it on/off

## How to Use

- **Toggle a box:** Click on any box to turn it ON (blue) or OFF (gray)
- **All ON:** Click the "All ON" button to enable all boxes
- **Reset:** Click the "Reset All" button to turn off all boxes
- **Counter:** The display at the bottom shows how many boxes are currently ON

## Project Structure

```
toogle-app/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    └── index.html        # HTML/CSS/JavaScript frontend
```

## API Endpoints

- `GET /` - Render the main page
- `POST /api/toggle` - Toggle a specific box (sends `box_id` in JSON)
- `GET /api/states` - Get the current state of all boxes
- `POST /api/reset` - Reset all boxes to OFF

## Troubleshooting

**Port 5000 already in use:**
Edit `app.py` and change `port=5000` to another port number (e.g., `port=5001`)

**ModuleNotFoundError: No module named 'flask':**
Make sure you've activated the virtual environment and installed requirements:
```bash
pip install -r requirements.txt
```

## License

Free to use and modify!
