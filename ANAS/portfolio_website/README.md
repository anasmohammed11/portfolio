# Portfolio Website - M Anas Mohammed

A modern, unique portfolio website built with Python Flask featuring a cyberpunk-inspired design with animated backgrounds, code-themed visuals, and smooth transitions.

## Features

✨ **Unique Design Elements:**
- Animated gradient background with floating effects
- Code window visual with syntax highlighting
- Cyberpunk color scheme (cyan & orange accents on dark navy)
- Smooth scroll animations and hover effects
- Responsive design for all devices

🎨 **Sections:**
- Hero section with animated code display
- Technical skills showcase
- Professional experience timeline
- Featured projects gallery
- Certifications & achievements
- Contact information with social links

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install Flask==3.0.0 Werkzeug==3.0.1
```

### Step 2: Add Your Resume PDF

Place your resume PDF file in the `static` folder with the name:
```
static/ANAS_MOHAMMED_RES.pdf
```

### Step 3: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Project Structure

```
portfolio/
├── app.py                 # Flask application (main file)
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Portfolio HTML template
├── static/
│   └── ANAS_MOHAMMED_RES.pdf  # Your resume PDF
└── README.md             # This file
```

## Customization

### Update Portfolio Data

Edit `app.py` and modify the `PORTFOLIO_DATA` dictionary to update:
- Personal information
- Skills
- Experience
- Projects
- Certifications

### Modify Design

Edit `templates/index.html` to customize:
- Colors (CSS variables in `:root`)
- Fonts (Google Fonts links)
- Animations
- Layout

### CSS Variables

```css
--primary: #0A0E27;        /* Dark navy background */
--secondary: #1A1F3A;      /* Card backgrounds */
--accent: #00F0FF;         /* Cyan accent */
--accent-secondary: #FF6B35; /* Orange accent */
--text: #E8E9ED;           /* Light text */
--text-muted: #9CA3AF;     /* Muted text */
```

## Design Highlights

- **Typography:** Bebas Neue for headers (bold, impactful) + Manrope for body (clean, modern)
- **Color Palette:** Dark cyberpunk theme with electric cyan and warm orange accents
- **Animations:** CSS-based floating background, slide-in effects, hover transformations
- **Layout:** Asymmetric grid layouts with generous spacing and card-based design

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Deployment

### Option 1: Render / Railway / Heroku
1. Create a `Procfile`:
   ```
   web: python app.py
   ```
2. Push to Git repository
3. Connect to deployment platform

### Option 2: PythonAnywhere
1. Upload all files
2. Set up virtual environment
3. Configure WSGI file

### Option 3: Docker
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## License

This portfolio template is free to use and modify for personal projects.

## Contact

**M Anas Mohammed**
- Email: anasmohammed0327@gmail.com
- Phone: 9345868745
- LinkedIn: [anas-mohammed-m](https://www.linkedin.com/in/anas-mohammed-m-055961318)
- GitHub: [anasmohammed11](https://github.com/anasmohammed11)

---

Built with ❤️ using Python Flask
