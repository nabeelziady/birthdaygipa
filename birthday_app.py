import streamlit as st
import datetime
import time
from datetime import datetime as dt
import math

# Set page config
st.set_page_config(
    page_title="🎂 Happy Birthday! 🎂",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with pink theme
pink_theme = """
<style>
    :root {
        --primary-pink: #ff69b4;
        --light-pink: #ffb6d9;
        --dark-pink: #ff1493;
        --very-light-pink: #ffe4f0;
    }
    
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background: linear-gradient(135deg, #ffe4f0 0%, #ffb6d9 50%, #ffc0cb 100%);
        font-family: 'Arial', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #ffe4f0 0%, #ffb6d9 50%, #ffc0cb 100%);
    }
    
    .main-title {
        text-align: center;
        color: #ff1493;
        font-size: 3.5em;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(255, 105, 180, 0.3);
        margin: 20px 0;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .countdown-container {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4f0 100%);
        border: 3px solid #ff1493;
        border-radius: 20px;
        padding: 30px;
        margin: 20px auto;
        max-width: 800px;
        box-shadow: 0 10px 40px rgba(255, 105, 180, 0.3);
        text-align: center;
    }
    
    .countdown-title {
        color: #ff1493;
        font-size: 1.8em;
        font-weight: bold;
        margin-bottom: 15px;
    }
    
    .countdown-time {
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
        margin: 20px 0;
    }
    
    .time-unit {
        background: #ff69b4;
        color: white;
        padding: 20px;
        border-radius: 15px;
        min-width: 80px;
        box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
    }
    
    .time-number {
        font-size: 2em;
        font-weight: bold;
    }
    
    .time-label {
        font-size: 0.9em;
        margin-top: 5px;
    }
    
    .feature-card {
        background: white;
        border-left: 5px solid #ff69b4;
        padding: 20px;
        margin: 15px 0;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(255, 105, 180, 0.2);
    }
    
    .feature-title {
        color: #ff1493;
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .heart {
        color: #ff1493;
        animation: heartbeat 1.2s infinite;
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
    
    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        pointer-events: none;
        z-index: 9999;
    }
    
    .section-header {
        color: #ff1493;
        font-size: 2em;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 20px;
        text-align: center;
        padding: 10px;
        border-bottom: 3px solid #ff69b4;
    }
</style>
"""

st.markdown(pink_theme, unsafe_allow_html=True)

# Initialize session state
if 'confetti_active' not in st.session_state:
    st.session_state.confetti_active = False

# Main Title with animation
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="main-title">
        🎉 Happy Birthday 🎉<br>
        <span style="font-size: 0.7em;">To My Love ❤️</span>
    </div>
    """, unsafe_allow_html=True)

# Countdown Timer
st.markdown('<div class="countdown-title">⏰ Countdown to Your Special Day ⏰</div>', unsafe_allow_html=True)

# Calculate countdown
target_date = dt(2026, 1, 8, 0, 0, 0)
now = dt.now()
time_diff = target_date - now

days = time_diff.days
hours = time_diff.seconds // 3600
minutes = (time_diff.seconds % 3600) // 60
seconds = time_diff.seconds % 60

# Create countdown display
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

# Auto-refresh the page every second
st.markdown("""
<script>
    setTimeout(function() {
        window.location.reload();
    }, 1000);
</script>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section: Special Features
st.markdown('<div class="section-header">✨ Celebrate With Me ✨</div>', unsafe_allow_html=True)

# Features Grid
feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🎂 Special Wishes</div>
        <p>Leave your heartfelt message and birthday wishes that will be displayed on the celebration wall!</p>
    </div>
    """, unsafe_allow_html=True)

with feature2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🎵 Love Songs</div>
        <p>Listen to a curated playlist of romantic songs to celebrate this special day together!</p>
    </div>
    """, unsafe_allow_html=True)

with feature3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📸 Memory Gallery</div>
        <p>Share and view beautiful memories and moments we've shared together!</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section: Birthday Wishes Wall
st.markdown('<div class="section-header">💌 Birthday Wishes Wall 💌</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    wish_message = st.text_area(
        "✍️ Write your birthday wish:",
        placeholder="Type your heartfelt message here...",
        height=100,
        key="wish_input"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    submit_wish = st.button("💖 Send Wish", use_container_width=True, key="submit_wish")

if submit_wish and wish_message:
    st.success("🎉 Your wish has been sent with love! 💕")
    st.balloons()

# Display wishes
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="background: white; padding: 20px; border-radius: 10px; border-left: 5px solid #ff69b4;">
    <h3 style="color: #ff1493;">Recent Wishes:</h3>
    <p style="color: #666; font-style: italic;">💕 Happy birthday to my wonderful love! May this day bring you all the happiness you deserve!</p>
    <hr style="border: 1px solid #ffb6d9;">
    <p style="color: #666; font-style: italic;">❤️ Wishing you a year filled with love, joy, and beautiful moments together!</p>
    <hr style="border: 1px solid #ffb6d9;">
    <p style="color: #666; font-style: italic;">🎂 To my special someone - may your day be as beautiful as you are!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section: Fun Activities
st.markdown('<div class="section-header">🎉 Fun Activities 🎉</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💝 Surprise Box", "🎨 Love Meter", "🎪 Fun Facts"])

with tab1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffb6d9 0%, #ffc0cb 100%); 
                padding: 30px; border-radius: 15px; text-align: center;">
        <h2 style="color: #ff1493;">Click the button to reveal your surprise! 🎁</h2>
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
        <div style="background: white; padding: 30px; border-radius: 15px; 
                    border: 3px solid #ff69b4; text-align: center;">
            <h3 style="color: #ff1493; font-size: 1.5em;">{surprise}</h3>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

with tab2:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h3 style="color: #ff1493;">How much do I love you? 💗</h3>
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
    <div style="text-align: center; padding: 20px;">
        <h2 style="color: {color}; font-size: 3em;">{emoji}</h2>
        <h1 style="color: {color};">{"❤️ " * (love_level // 10)}</h1>
        <p style="color: #ff1493; font-size: 1.5em; font-weight: bold;">
            Love Level: <span style="color: {color};">{love_level}%</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div style="padding: 20px;">
        <h3 style="color: #ff1493;">Fun Love Facts! 💝</h3>
        
        <div style="background: #fff0f5; padding: 15px; margin: 10px 0; border-radius: 10px; border-left: 5px solid #ff69b4;">
            <p><strong>💡 Fact #1:</strong> When you're in love, your brain releases the same chemicals as when you're happy - dopamine and serotonin!</p>
        </div>
        
        <div style="background: #fff0f5; padding: 15px; margin: 10px 0; border-radius: 10px; border-left: 5px solid #ff69b4;">
            <p><strong>💡 Fact #2:</strong> Making eye contact for 10 minutes can create a feeling of intense love and connection!</p>
        </div>
        
        <div style="background: #fff0f5; padding: 15px; margin: 10px 0; border-radius: 10px; border-left: 5px solid #ff69b4;">
            <p><strong>💡 Fact #3:</strong> Holding hands reduces pain and stress. It literally heals! 💕</p>
        </div>
        
        <div style="background: #fff0f5; padding: 15px; margin: 10px 0; border-radius: 10px; border-left: 5px solid #ff69b4;">
            <p><strong>💡 Fact #4:</strong> The heart emoji ❤️ is the most used emoji in the world!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 30px; color: #ff1493; font-size: 1.2em;">
    <p style="font-weight: bold;">With all my love ❤️</p>
    <p>Made with 💕 for your special day</p>
    <p style="font-size: 0.9em; color: #ff69b4;">January 8, 2026 🎂</p>
</div>
""", unsafe_allow_html=True)
