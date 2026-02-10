from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load gardening tips from JSON
def load_gardening_tips():
    with open('data/tips.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_plants_data():
    with open('data/plants.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    tips = load_gardening_tips()
    plants = load_plants_data()
    return render_template('index.html', tips=tips[:3], plants=plants[:4])

@app.route('/tips')
def tips_page():
    tips = load_gardening_tips()
    return render_template('tips.html', tips=tips)

@app.route('/plants')
def plants_page():
    plants = load_plants_data()
    return render_template('plants.html', plants=plants)

@app.route('/seasonal')
def seasonal_page():
    tips = load_gardening_tips()
    seasonal_tips = [tip for tip in tips if tip.get('seasonal')]
    return render_template('seasonal.html', tips=seasonal_tips)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # In a real application, you would save this to a database
        print(f"Contact form submitted: {name}, {email}, {message}")
        
        return render_template('contact.html', success=True)
    
    return render_template('contact.html', success=False)

@app.route('/api/tips')
def api_tips():
    tips = load_gardening_tips()
    return jsonify(tips)

@app.route('/api/tips/<season>')
def api_seasonal_tips(season):
    tips = load_gardening_tips()
    seasonal_tips = [tip for tip in tips if tip.get('season', '').lower() == season.lower()]
    return jsonify(seasonal_tips)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
