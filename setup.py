#!/usr/bin/env python3
import os
import json

def setup_project():
    """Create necessary directories and default data files"""
    
    # Create directories
    directories = ['data', 'static/images', 'templates']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Create default data files if they don't exist
    if not os.path.exists('data/tips.json'):
        tips_data = [
            {
                "id": 1,
                "title": "Start Small",
                "description": "Begin with herbs in containers on your balcony or windowsill",
                "season": "All Year",
                "emoji": "🌱",
                "icon": "fas fa-seedling",
                "seasonal": False
            },
            {
                "id": 2,
                "title": "Use Coastal Winds",
                "description": "Balbriggan's sea breeze helps prevent plant diseases",
                "season": "Summer",
                "emoji": "🌊",
                "icon": "fas fa-wind",
                "seasonal": True
            },
            {
                "id": 3,
                "title": "Saturday Market",
                "description": "Visit Balbriggan Farmers Market for local plants and advice",
                "season": "All Year",
                "emoji": "🛒",
                "icon": "fas fa-shopping-basket",
                "seasonal": False
            }
        ]
        
        with open('data/tips.json', 'w', encoding='utf-8') as f:
            json.dump(tips_data, f, indent=2)
        print("Created default tips.json")
    
    if not os.path.exists('data/plants.json'):
        plants_data = [
            {
                "id": 1,
                "name": "Sea Kale",
                "description": "Loves our coastal breeze! Edible and beautiful.",
                "sun": "Full Sun",
                "planting_time": "Spring",
                "emoji": "🌊",
                "difficulty": "easy",
                "type": "vegetable"
            },
            {
                "id": 2,
                "name": "Balbriggan Berries",
                "description": "Strawberries & raspberries thrive in our microclimate.",
                "sun": "6+ hours",
                "planting_time": "March-May",
                "emoji": "🍓",
                "difficulty": "medium",
                "type": "fruit"
            },
            {
                "id": 3,
                "name": "Coastal Herbs",
                "description": "Rosemary, thyme & sage love the seaside air.",
                "sun": "Full Sun",
                "planting_time": "April-June",
                "emoji": "🌿",
                "difficulty": "easy",
                "type": "herb"
            },
            {
                "id": 4,
                "name": "Dublin Potatoes",
                "description": "Classic Irish staple - grows perfectly here!",
                "sun": "Partial Sun",
                "planting_time": "St. Patrick's Day",
                "emoji": "🥔",
                "difficulty": "easy",
                "type": "vegetable"
            }
        ]
        
        with open('data/plants.json', 'w', encoding='utf-8') as f:
            json.dump(plants_data, f, indent=2)
        print("Created default plants.json")
    
    print("\n✅ Setup complete! You can now run:")
    print("  python app.py")
    print("\nOr deploy to Render with:")
    print("  git push origin main")

if __name__ == '__main__':
    setup_project()
