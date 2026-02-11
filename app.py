from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'growbalbriggan-local-dev-2024')

# Balbriggan-specific data
BALBRIGGAN_INFO = {
    "name": "Balbriggan",
    "county": "North County Dublin",
    "climate": "Coastal temperate",
    "soil_type": "Sandy loam near coast, clay inland",
    "growing_season": "March to November",
    "community_garden": "Balbriggan Community Garden",
    "market_day": "Saturdays",
    "coastal_feature": "Beautiful coastline affecting microclimate"
}

def load_gardening_tips():
    try:
        with open('data/tips.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return [
            {
                "id": 1,
                "title": "Start Small",
                "description": "Begin with herbs in containers on your balcony or windowsill",
                "season": "All Year",
                "emoji": "🌱",
                "icon": "fas fa-seedling",
                "seasonal": False
            }
        ]
    except json.JSONDecodeError:
        return []

def load_plants_data():
    try:
        with open('data/plants.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return [
            {
                "id": 1,
                "name": "Sea Kale",
                "description": "Loves our coastal breeze! Edible and beautiful.",
                "sun": "Full Sun",
                "planting_time": "Spring",
                "emoji": "🌊",
                "difficulty": "easy",
                "type": "vegetable"
            }
        ]
    except json.JSONDecodeError:
        return []

def load_video_classes():
    try:
        with open('data/videos.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return [
            {
                "id": 1,
                "title": "Getting Started with Balcony Gardening",
                "description": "Learn how to grow vegetables, herbs, and flowers in small spaces",
                "date": "2024-03-15",
                "duration": "25:30",
                "youtube_id": "dQw4w9WgXcQ",
                "instructor": "Sarah O'Connor",
                "difficulty": "beginner",
                "tags": ["balcony", "containers", "beginners"],
                "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg"
            }
        ]

def load_balbriggan_events():
    return [
        {"date": "Weekly", "event": "Community Garden Volunteering", "emoji": "👨‍🌾", "location": "Town Park"},
        {"date": "Saturdays", "event": "Balbriggan Farmers Market", "emoji": "🛒", "location": "Market Square"},
        {"date": "Monthly", "event": "Seed Swap & Plant Share", "emoji": "🌱", "location": "Community Centre"},
    ]

@app.route('/')
def home():
    # Redirect to videos page as new homepage
    return redirect(url_for('videos_page'))

@app.route('/videos')
def videos_page():
    videos = load_video_classes()
    tips = load_gardening_tips()
    return render_template('videos.html', 
                         videos=videos,
                         tips=tips[:2],
                         balbriggan=BALBRIGGAN_INFO)

@app.route('/tips')
def tips_page():
    tips = load_gardening_tips()
    return render_template('tips.html', tips=tips, balbriggan=BALBRIGGAN_INFO)

@app.route('/plants')
def plants_page():
    plants = load_plants_data()
    return render_template('plants.html', plants=plants, balbriggan=BALBRIGGAN_INFO)

@app.route('/seasonal')
def seasonal_page():
    tips = load_gardening_tips()
    seasonal_tips = [tip for tip in tips if tip.get('seasonal', False)]
    
    current_month = datetime.now().strftime("%B")
    month_emoji = {
        "January": "❄️", "February": "🌨️", "March": "🌱", "April": "🌸",
        "May": "🌻", "June": "☀️", "July": "🏖️", "August": "🌊",
        "September": "🍎", "October": "🎃", "November": "🍂", "December": "🎄"
    }
    
    return render_template('seasonal.html', 
                         tips=seasonal_tips,
                         current_month=current_month,
                         month_emoji=month_emoji.get(current_month, "📅"),
                         balbriggan=BALBRIGGAN_INFO)

@app.route('/community')
def community_page():
    events = load_balbriggan_events()
    return render_template('community.html', events=events, balbriggan=BALBRIGGAN_INFO)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        flash("🎉 Thanks for reaching out! We'll get back to you soon!", "success")
        return redirect(url_for('contact'))
    
    return render_template('contact.html', balbriggan=BALBRIGGAN_INFO)

# New legal pages
@app.route('/privacy')
def privacy_page():
    return render_template('privacy.html', balbriggan=BALBRIGGAN_INFO)

@app.route('/terms')
def terms_page():
    return render_template('terms.html', balbriggan=BALBRIGGAN_INFO)

@app.route('/rules')
def rules_page():
    return render_template('rules.html', balbriggan=BALBRIGGAN_INFO)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if email:
        flash(f"🌱 Welcome to GrowBalbriggan! Check your email for gardening tips!", "success")
    else:
        flash("Please enter a valid email address", "error")
    
    return redirect(request.referrer or url_for('videos_page'))

# API endpoints
@app.route('/api/tips')
def api_tips():
    tips = load_gardening_tips()
    return jsonify(tips)

@app.route('/api/videos')
def api_videos():
    videos = load_video_classes()
    return jsonify(videos)

@app.route('/api/balbriggan-events')
def api_events():
    events = load_balbriggan_events()
    return jsonify(events)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "service": "GrowBalbriggan"})

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', balbriggan=BALBRIGGAN_INFO), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', balbriggan=BALBRIGGAN_INFO), 500

# Create necessary directories on startup
def create_directories():
    directories = ['data', 'static/images', 'static/css', 'static/js', 'templates']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

if __name__ == '__main__':
    create_directories()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
