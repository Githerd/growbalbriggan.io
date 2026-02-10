// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'absolute';
            navLinks.style.top = '100%';
            navLinks.style.left = '0';
            navLinks.style.right = '0';
            navLinks.style.backgroundColor = 'white';
            navLinks.style.padding = '1rem';
            navLinks.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
            navLinks.style.gap = '1rem';
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
    
    // Load seasonal tips based on current month
    function loadSeasonalTips() {
        const months = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ];
        const currentMonth = months[new Date().getMonth()];
        
        // Determine season based on month
        let season;
        if ([11, 0, 1].includes(new Date().getMonth())) season = 'winter';
        else if ([2, 3, 4].includes(new Date().getMonth())) season = 'spring';
        else if ([5, 6, 7].includes(new Date().getMonth())) season = 'summer';
        else season = 'autumn';
        
        // Update seasonal display if element exists
        const seasonDisplay = document.getElementById('current-season');
        if (seasonDisplay) {
            seasonDisplay.textContent = season.charAt(0).toUpperCase() + season.slice(1);
        }
    }
    
    loadSeasonalTips();
    
    // Contact form handling
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Simple validation
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();
            
            if (!name || !email || !message) {
                alert('Please fill in all fields');
                return;
            }
            
            if (!validateEmail(email)) {
                alert('Please enter a valid email address');
                return;
            }
            
            // Submit form
            this.submit();
        });
    }
    
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    // Plant filter functionality
    const plantFilters = document.querySelectorAll('.plant-filter');
    if (plantFilters.length > 0) {
        plantFilters.forEach(filter => {
            filter.addEventListener('click', function() {
                const type = this.dataset.type;
                filterPlants(type);
                
                // Update active filter
                plantFilters.forEach(f => f.classList.remove('active'));
                this.classList.add('active');
            });
        });
    }
    
    function filterPlants(type) {
        const plantCards = document.querySelectorAll('.plant-card');
        plantCards.forEach(card => {
            if (type === 'all' || card.dataset.type === type) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }
});

// API Functions
async function fetchGardeningTips() {
    try {
        const response = await fetch('/api/tips');
        const tips = await response.json();
        return tips;
    } catch (error) {
        console.error('Error fetching tips:', error);
        return [];
    }
}

async function fetchSeasonalTips(season) {
    try {
        const response = await fetch(`/api/tips/${season}`);
        const tips = await response.json();
        return tips;
    } catch (error) {
        console.error('Error fetching seasonal tips:', error);
        return [];
    }
}
