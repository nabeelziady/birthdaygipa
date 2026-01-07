# Birthday Celebration Web App 🎂💕

A beautiful, interactive web application to celebrate your loved one's birthday with a pink-themed design and exciting features!

## Features ✨

- **Real-time Countdown**: Live countdown timer to January 8, 2026 at 00:00
- **Birthday Wishes Wall**: Leave heartfelt messages and birthday wishes
- **Surprise Box**: Reveal random sweet messages and surprises
- **Love Meter**: Express your love level interactively
- **Fun Facts**: Discover interesting love and happiness facts
- **Beautiful Pink Theme**: Elegant gradient design with smooth animations
- **Mobile Responsive**: Works great on all devices

## Setup & Installation 🚀

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/birthday-celebration.git
cd birthday-celebration
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Running the App 🎉

### Local Development
```bash
streamlit run birthday_app.py
```

The app will open in your browser at `http://localhost:8501`

### Deploy on Streamlit Cloud

1. **Push to GitHub**
   - Make sure your repository is on GitHub
   - Include `birthday_app.py` and `requirements.txt`

2. **Deploy on Streamlit Cloud**
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Connect your GitHub account
   - Select your repository and branch
   - Set the main file as `birthday_app.py`
   - Click Deploy!

3. **Your app will be live at**: `https://share.streamlit.io/yourusername/birthday-celebration/main/birthday_app.py`

## File Structure 📁

```
birthday-celebration/
├── birthday_app.py      # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Customization 🎨

You can customize the app by editing `birthday_app.py`:

- **Change the countdown date**: Modify the `target_date` variable
- **Add more surprises**: Edit the `surprises` list in the Surprise Box section
- **Change colors**: Modify the hex color codes in the CSS (e.g., `#ff69b4` for pink)
- **Add personal messages**: Update the default wishes in the Wishes Wall section

## Technologies Used 🛠️

- **Streamlit**: Web framework for Python
- **HTML/CSS**: Custom styling and animations
- **Python**: Backend logic

## Tips for GitHub Upload 📤

1. Create a `.gitignore` file to exclude unnecessary files
2. Write a clear README.md
3. Commit and push regularly
4. Tag important releases with version numbers

## License 📄

This project is open source and available under the MIT License.

## Created with ❤️

Made with love for celebrating special moments together! 💕

---

**Deployed**: January 2026
**Special Date**: January 8, 2026 🎂
