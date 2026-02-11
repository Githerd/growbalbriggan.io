#!/usr/bin/env python3
import os
import json

def setup_project():
    """Create necessary directories and default data files"""
    
    print("🚀 Setting up GrowBalbriggan project...\n")
    
    # Create directories
    directories = [
        'data',
        'static/images',
        'static/css',
        'static/js',
        'templates'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    # Create placeholder images
    print("\n📁 Creating placeholder images...")
    placeholder_images = [
        'balbriggan-coast.jpg',
        'seasonal-bg.jpg',
        'community-bg.jpg',
        'balbriggan-map.svg',
        'growbalbriggan-logo.png',
        'apple-touch-icon.png',
        'favicon.ico'
    ]
    
    for image in placeholder_images:
        path = os.path.join('static/images', image)
        
        if not os.path.exists(path):
            if image.endswith('.svg'):
                # Create simple SVG placeholder
                with open(path, 'w') as f:
                    f.write(f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300">
                    <rect width="400" height="300" fill="#00c853"/>
                    <text x="200" y="150" text-anchor="middle" fill="white" font-family="Arial" font-size="20">
                    {image.replace('.svg', '').replace('-', ' ').title()}</text>
                    <text x="200" y="180" text-anchor="middle" fill="white" font-family="Arial" font-size="14">
                    (Placeholder Image)</text>
                    </svg>''')
            elif image.endswith('.ico'):
                # Create minimal ICO file (would be replaced with actual icon)
                with open(path, 'wb') as f:
                    # Minimal ICO header
                    f.write(b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00(\x01\x00\x00')
            else:
                # Create text file explaining it's a placeholder
                with open(path + '.txt', 'w') as f:
                    f.write(f"Placeholder for {image}\n")
                    f.write(f"Replace with actual image file\n")
                # Create the actual file as empty
                with open(path, 'wb') as f:
                    pass
            print(f"✅ Created placeholder: {image}")
    
    # Create default data files
    print("\n📊 Creating default data files...")
    
    # Tips data
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
            },
            {
                "id": 4,
                "title": "Balbriggan Soil",
                "description": "Our coastal soil benefits from added compost for better drainage",
                "season": "Spring",
                "emoji": "🌱",
                "icon": "fas fa-mountain",
                "seasonal": True
            },
            {
                "id": 5,
                "title": "Winter Protection",
                "description": "Our mild coastal climate means you can grow winter vegetables",
                "season": "Winter",
                "emoji": "❄️",
                "icon": "fas fa-snowflake",
                "seasonal": True
            },
            {
                "id": 6,
                "title": "Community Help",
                "description": "Join our WhatsApp group for instant gardening advice",
                "season": "All Year",
                "emoji": "👥",
                "icon": "fas fa-users",
                "seasonal": False
            }
        ]
        
        with open('data/tips.json', 'w', encoding='utf-8') as f:
            json.dump(tips_data, f, indent=2)
        print("✅ Created default tips.json")
    
    # Plants data
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
            },
            {
                "id": 5,
                "name": "Balbriggan Blooms",
                "description": "Fuchsia & hydrangeas love our damp climate.",
                "sun": "Partial Shade",
                "planting_time": "Spring",
                "emoji": "🌸",
                "difficulty": "easy",
                "type": "flower"
            },
            {
                "id": 6,
                "name": "Salad Heaven",
                "description": "Lettuce, spinach & rocket grow fast here!",
                "sun": "3-4 hours",
                "planting_time": "March-September",
                "emoji": "🥗",
                "difficulty": "easy",
                "type": "vegetable"
            }
        ]
        
        with open('data/plants.json', 'w', encoding='utf-8') as f:
            json.dump(plants_data, f, indent=2)
        print("✅ Created default plants.json")
    
    # Videos data
    if not os.path.exists('data/videos.json'):
        videos_data = [
            {
                "id": 1,
                "title": "Getting Started with Balcony Gardening",
                "description": "Learn how to grow vegetables, herbs, and flowers in small spaces perfect for Balbriggan apartments",
                "date": "2024-03-15",
                "duration": "25:30",
                "youtube_id": "dQw4w9WgXcQ",
                "instructor": "Sarah O'Connor",
                "difficulty": "beginner",
                "tags": ["balcony", "containers", "beginners", "small-space"],
                "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg"
            },
            {
                "id": 2,
                "title": "Preparing Balbriggan Soil for Spring",
                "description": "Understanding our unique coastal soil and how to prepare it for optimal planting",
                "date": "2024-03-08",
                "duration": "18:45",
                "youtube_id": "abcdefghijk",
                "instructor": "Mike Chen",
                "difficulty": "beginner",
                "tags": ["soil", "preparation", "spring", "coastal"],
                "thumbnail": "https://img.youtube.com/vi/abcdefghijk/hqdefault.jpg"
            },
            {
                "id": 3,
                "title": "Tomato Growing Masterclass",
                "description": "How to grow delicious tomatoes in Balbriggan's climate - greenhouse and outdoor methods",
                "date": "2024-03-01",
                "duration": "32:15",
                "youtube_id": "lmnopqrstuv",
                "instructor": "Aoife Murphy",
                "difficulty": "intermediate",
                "tags": ["tomatoes", "vegetables", "greenhouse", "summer"],
                "thumbnail": "https://img.youtube.com/vi/lmnopqrstuv/hqdefault.jpg"
            }
        ]
        
        with open('data/videos.json', 'w', encoding='utf-8') as f:
            json.dump(videos_data, f, indent=2)
        print("✅ Created default videos.json")
    
    # Create CSS file if it doesn't exist
    if not os.path.exists('static/css/style.css'):
        with open('static/css/style.css', 'w') as f:
            f.write('''/* GrowBalbriggan - Modern, Youthful Gardening Theme */
:root {
    /* Vibrant Color Palette - Enhanced for better contrast */
    --primary-green: #00a046;
    --secondary-green: #52c41a;
    --accent-teal: #00a88a;
    --sunny-yellow: #ffc107;
    --soil-brown: #795548;
    --blossom-pink: #e91e63;
    --sky-blue: #2196f3;
    --white: #ffffff;
    --off-white: #f8f9fa;
    --light-gray: #f0f0f0;
    --text-dark: #1b5e20;
    --text-light: #2e7d32;
    --text-on-green: #ffffff;
    --text-on-yellow: #212121;
    --text-on-pink: #ffffff;
    
    /* Fun Gradients */
    --gradient-sunrise: linear-gradient(135deg, #ffc107, #00a046);
    --gradient-ocean: linear-gradient(135deg, #00a88a, #1976d2);
    --gradient-blossom: linear-gradient(135deg, #e91e63, #ffc107);
    --gradient-dark: linear-gradient(135deg, #006400, #004d00);
    
    /* Shadows & Effects */
    --shadow-light: 0 4px 20px rgba(0, 0, 0, 0.1);
    --shadow-medium: 0 8px 30px rgba(0, 0, 0, 0.15);
    --shadow-heavy: 0 12px 40px rgba(0, 0, 0, 0.2);
    --border-radius: 16px;
    --border-radius-round: 50px;
}

body {
    font-family: 'Nunito', sans-serif;
    line-height: 1.7;
    color: var(--text-dark);
    background-color: var(--off-white);
    margin: 0;
    padding: 0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

h1, h2, h3 {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
}

.btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 1rem 2rem;
    background: var(--gradient-sunrise);
    color: var(--text-on-yellow);
    text-decoration: none;
    border-radius: var(--border-radius-round);
    font-weight: 700;
    border: none;
    cursor: pointer;
    transition: all 0.3s;
}

.btn:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-heavy);
}

/* Add more styles as needed... */''')
        print("✅ Created default style.css")
    
    # Create JS file if it doesn't exist
    if not os.path.exists('static/js/script.js'):
        with open('static/js/script.js', 'w') as f:
            f.write('''// GrowBalbriggan JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', function() {
            mobileMenu.style.display = mobileMenu.style.display === 'flex' ? 'none' : 'flex';
        });
    }
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // Newsletter form handling
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            if (email) {
                alert('🎉 Thanks for subscribing! You\'ll receive gardening tips soon!');
                this.reset();
            }
        });
    }
    
    console.log('🌱 GrowBalbriggan website loaded successfully!');
});''')
        print("✅ Created default script.js")
    
    print("\n" + "="*50)
    print("✅ SETUP COMPLETE!")
    print("="*50)
    print("\n📋 Next steps:")
    print("1. Run the app locally: python app.py")
    print("2. Visit http://localhost:5000")
    print("3. Replace placeholder images in static/images/")
    print("4. Customize templates in templates/")
    print("5. Add your actual data to data/ files")
    print("\n🌱 Happy gardening from Balbriggan!")

if __name__ == '__main__':
    setup_project()
