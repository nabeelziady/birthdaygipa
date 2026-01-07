import streamlit as st
import datetime
from datetime import datetime as dt
import json
import os
import pytz

# Set page config - HARUS DI AWAL
st.set_page_config(
    page_title="🎂 Happy Birthday! 🎂",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Database file path
DB_FILE = "wishes_database.json"

# Function to load wishes from database
def load_wishes():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

# Function to save wishes to database
def save_wishes(wishes):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(wishes, f, ensure_ascii=False, indent=2)

# Initialize session state with wishes from database
if 'wishes' not in st.session_state:
    st.session_state.wishes = load_wishes()

# Custom CSS with coquette pink theme
pink_theme = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lora:ital@0;1&display=swap');
    
    :root {
        --primary-pink: #ff69b4;
        --light-pink: #ffb6d9;
        --dark-pink: #ff1493;
        --very-light-pink: #ffe4f0;
        --cream: #fff9f5;
        --rose: #ffc0cb;
    }
    
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background: linear-gradient(135deg, #fff9f5 0%, #ffe4f0 50%, #ffc0cb 100%);
        font-family: 'Lora', serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #fff9f5 0%, #ffe4f0 50%, #ffc0cb 100%);
    }
    
    .main-title {
        text-align: center;
        color: #d4006d;
        font-family: 'Playfair Display', serif;
        font-size: 4em;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(255, 105, 180, 0.2);
        margin: 30px 0;
        letter-spacing: 1px;
    }
    
    .countdown-title {
        color: #d4006d;
        font-family: 'Playfair Display', serif;
        font-size: 2.2em;
        font-weight: 700;
        margin-bottom: 25px;
        text-align: center;
        letter-spacing: 0.5px;
    }
    
    .time-unit {
        background: linear-gradient(135deg, #ff69b4 0%, #ff85c0 100%);
        color: white;
        padding: 25px;
        border-radius: 25px;
        min-width: 100px;
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(10px);
    }
    
    .time-number {
        font-size: 2.5em;
        font-weight: 700;
        font-family: 'Playfair Display', serif;
    }
    
    .time-label {
        font-size: 1em;
        margin-top: 8px;
        font-weight: 500;
        letter-spacing: 1px;
    }
    
    .section-header {
        color: #d4006d;
        font-family: 'Playfair Display', serif;
        font-size: 2.5em;
        font-weight: 700;
        margin-top: 40px;
        margin-bottom: 25px;
        text-align: center;
        padding: 15px;
        border-bottom: 3px solid #ff69b4;
        letter-spacing: 0.5px;
    }
    
    .special-box {
        background: linear-gradient(135deg, rgba(255, 192, 203, 0.3) 0%, rgba(255, 182, 193, 0.3) 100%);
        border: 2px dashed #ff69b4;
        border-radius: 25px;
        padding: 70px 40px;
        text-align: center;
        min-height: 280px;
        margin-bottom: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        backdrop-filter: blur(5px);
    }
    
    .special-box h2 {
        color: #ff69b4;
        font-family: 'Playfair Display', serif;
        font-size: 2em;
        font-weight: 700;
    }
    
    .wish-input-section {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 105, 180, 0.2);
    }
    
    .wish-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 240, 245, 0.9) 100%);
        padding: 20px;
        margin: 12px 0;
        border-radius: 15px;
        border-left: 4px solid #ff69b4;
        box-shadow: 0 5px 15px rgba(255, 105, 180, 0.15);
        backdrop-filter: blur(10px);
    }
    
    .wish-card p {
        color: #333;
        font-style: italic;
        font-size: 1.05em;
    }
    
    .tab-container {
        background: rgba(255, 255, 255, 0.5);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(10px);
    }
    
    button {
        background: linear-gradient(135deg, #ff69b4 0%, #ff85c0 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        font-family: 'Lora', serif !important;
        box-shadow: 0 5px 15px rgba(255, 105, 180, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(255, 105, 180, 0.4) !important;
    }
    
    .footer {
        text-align: center;
        padding: 40px 30px;
        color: #d4006d;
        font-family: 'Playfair Display', serif;
        font-size: 1.3em;
    }
</style>
"""

st.markdown(pink_theme, unsafe_allow_html=True)

# Main Title
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="main-title">
        🎉 Happy Birthday To My Love ❤️ 🎉
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="countdown-title">⏰ Countdown to Your Special Day ⏰</div>', unsafe_allow_html=True)

def get_countdown():
    # Set timezone to WIB (Jakarta)
    wib = pytz.timezone('Asia/Jakarta')
    target_date = wib.localize(dt(2026, 1, 8, 0, 0, 0))
    now = dt.now(wib)
    
    # If birthday has passed, reset to next year
    if now >= target_date:
        target_date = wib.localize(dt(2027, 1, 8, 0, 0, 0))
    
    time_diff = target_date - now
    
    days = time_diff.days
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds % 3600) // 60
    seconds = time_diff.seconds % 60
    
    return days, hours, minutes, seconds

# Display countdown
days, hours, minutes, seconds = get_countdown()

countdown_col1, countdown_col2, countdown_col3, countdown_col4 = st.columns(4)

with countdown_col1:
    st.markdown(f"""
    <div class="time-unit">
        <div class="time-number">{days}</div>
        <div class="time-label">Days</div>
    </div>
    """, unsafe_allow_html=True)

with countdown_col2:
    st.markdown(f"""
    <div class="time-unit">
        <div class="time-number">{hours:02d}</div>
        <div class="time-label">Hours</div>
    </div>
    """, unsafe_allow_html=True)

with countdown_col3:
    st.markdown(f"""
    <div class="time-unit">
        <div class="time-number">{minutes:02d}</div>
        <div class="time-label">Minutes</div>
    </div>
    """, unsafe_allow_html=True)

with countdown_col4:
    st.markdown(f"""
    <div class="time-unit">
        <div class="time-number">{seconds:02d}</div>
        <div class="time-label">Seconds</div>
    </div>
    """, unsafe_allow_html=True)

# Client-side countdown using JavaScript - updates DOM directly
st.markdown("""
<script>
    function updateCountdown() {
        const wibTime = new Date().toLocaleString('en-US', { timeZone: 'Asia/Jakarta' });
        const now = new Date(wibTime);
        let targetDate = new Date('2026-01-08T00:00:00');
        
        const timeDiff = targetDate - now;
        
        if (timeDiff > 0) {
            const days = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((timeDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);
            
            // Update the countdown display
            const timeUnits = document.querySelectorAll('.time-unit');
            if (timeUnits.length >= 4) {
                timeUnits[0].querySelector('.time-number').textContent = days;
                timeUnits[1].querySelector('.time-number').textContent = String(hours).padStart(2, '0');
                timeUnits[2].querySelector('.time-number').textContent = String(minutes).padStart(2, '0');
                timeUnits[3].querySelector('.time-number').textContent = String(seconds).padStart(2, '0');
            }
        }
    }
    
    // Update countdown every second
    setInterval(updateCountdown, 1000);
    // Initial update
    updateCountdown();
</script>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Large empty box for special section
st.markdown("""
<div class="special-box">
    <h2>💐 Special Moment For Us 💐</h2>
</div>
""", unsafe_allow_html=True)

# Section: Birthday Wishes Wall
st.markdown('<div class="section-header">💌 Birthday Wishes Wall 💌</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="wish-input-section">', unsafe_allow_html=True)
    wish_message = st.text_area(
        "✍️ Write your birthday wish:",
        placeholder="Share your love and heartfelt message here...",
        height=100,
        key="wish_input"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    submit_wish = st.button("💖 Send Wish", use_container_width=True, key="submit_wish")

if submit_wish and wish_message:
    # Add wish to session state
    st.session_state.wishes.append(wish_message)
    # Save to database
    save_wishes(st.session_state.wishes)
    st.success("🎉 Your wish has been sent with love! 💕")
    st.balloons()
    # Clear input by rerunning
    st.rerun()

# Display wishes
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="background: rgba(255, 255, 255, 0.6); padding: 20px; border-radius: 15px; border-left: 5px solid #ff69b4; backdrop-filter: blur(10px);">
    <h3 style="color: #d4006d; font-family: 'Playfair Display', serif; font-size: 1.8em;">💌 Recent Wishes</h3>
</div>
""", unsafe_allow_html=True)

# Display submitted wishes
if st.session_state.wishes:
    for wish in reversed(st.session_state.wishes):
        st.markdown(f"""
        <div class="wish-card">
            <p>💕 {wish}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="background: rgba(255, 240, 245, 0.7); padding: 25px; border-radius: 15px; text-align: center; border: 2px dashed #ff69b4; backdrop-filter: blur(5px);">
        <p style="color: #ff69b4; font-style: italic; font-size: 1.1em;">✨ No wishes yet. Be the first to send your love! ✨</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section: Fun Activities
st.markdown('<div class="section-header">🎉 Fun Activities 🎉</div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["💝 Surprise Box", "🎨 Love Meter"])

with tab1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(255, 192, 203, 0.4) 0%, rgba(255, 182, 193, 0.4) 100%); 
                padding: 40px; border-radius: 20px; text-align: center; backdrop-filter: blur(10px);">
        <h2 style="color: #d4006d; font-family: 'Playfair Display', serif; font-size: 2em;">Click to reveal your surprise! 🎁</h2>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🎁 Open Surprise Box", use_container_width=True, key="surprise_btn"):
        surprises = [
            "💕 You make every day special just by being you!",
            "🌹 I love you more with each passing day!",
            "🎂 Thank you for being the best part of my life!",
            "✨ You are my greatest blessing!",
            "🎵 Our love story is my favorite song!",
            "🌟 You complete me perfectly!",
            "💑 Forever with you sounds like a dream come true!"
        ]
        import random
        surprise = random.choice(surprises)
        st.markdown(f"""
        <div style="background: white; padding: 40px; border-radius: 20px; 
                    border: 3px solid #ff69b4; text-align: center; backdrop-filter: blur(10px);">
            <h3 style="color: #d4006d; font-family: 'Playfair Display', serif; font-size: 2em;">{surprise}</h3>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

with tab2:
    st.markdown("""
    <div style="text-align: center; padding: 25px;">
        <h3 style="color: #d4006d; font-family: 'Playfair Display', serif; font-size: 2em;">How much do I love you? 💗</h3>
    </div>
    """, unsafe_allow_html=True)
    
    love_level = st.slider("Move the slider to show your love level:", 0, 100, 100, key="love_meter")
    
    if love_level >= 80:
        color = "#ff1493"
        emoji = "🔥❤️🔥"
    elif love_level >= 60:
        color = "#ff69b4"
        emoji = "💕💕"
    else:
        color = "#ffb6d9"
        emoji = "💖"
    
    st.markdown(f"""
    <div style="text-align: center; padding: 30px; background: rgba(255, 255, 255, 0.5); border-radius: 20px; backdrop-filter: blur(10px);">
        <h2 style="color: {color}; font-size: 3.5em;">{emoji}</h2>
        <h1 style="color: {color}; font-family: 'Playfair Display', serif; margin: 15px 0;">{"❤️ " * (love_level // 10)}</h1>
        <p style="color: #d4006d; font-size: 1.8em; font-weight: bold; font-family: 'Playfair Display', serif;">
            Love Level: <span style="color: {color};">{love_level}%</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p style="font-size: 1.5em; margin-bottom: 10px;">💐 With all my love ❤️ 💐</p>
    <p>Made with 💕 for your special day</p>
    <p style="font-size: 0.95em; color: #ff69b4; margin-top: 10px;">January 8, 2026 🎂</p>
</div>
""", unsafe_allow_html=True)
