from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

# Portfolio data extracted from resume
PORTFOLIO_DATA = {
    'name': 'M Anas Mohammed',
    'title': 'Full Stack Developer',
    'location': 'Pollachi, Tamil Nadu',
    'email': 'anasmohammed0327@gmail.com',
    'phone': '9345868745',
    'linkedin': 'https://www.linkedin.com/in/anas-mohammed-m-055961318',
    'github': 'https://github.com/anasmohammed11',
    
    'about': 'Full Stack Developer and third-year B.Tech Information Technology student with hands-on experience in fullstack web and mobile application development using Flutter, React, JavaScript, Firebase, and MongoDB.',
    
    'skills': {
        'Programming Languages': ['Java', 'JavaScript', 'Python'],
        'Web Technologies': ['HTML', 'CSS', 'React'],
        'Mobile Development': ['Flutter (Dart)'],
        'Databases & Backend': ['Firebase', 'MongoDB'],
        'Tools & Platforms': ['Git', 'GitHub'],
        'Operating Systems': ['Windows', 'Linux']
    },
    
    'experience': [
        {
            'title': 'Full Stack Web Development Intern',
            'company': 'Accent Techno Soft (ATS)',
            'location': 'Tamil Nadu',
            'period': '06/2025 – 07/2025',
            'highlights': [
                'Worked on full-stack web application development using HTML, CSS, and JavaScript',
                'Assisted in frontend and backend integration connecting UI components with backend logic',
                'Debugged application issues and improved functionality through testing',
                'Followed Git-based collaborative workflows in an industry development environment'
            ]
        }
    ],
    
    'education': [
        {
            'degree': 'B.Tech Information Technology',
            'institution': 'Kongunadu College of Engineering and Technology',
            'period': '2023 – 2027',
            'score': 'CGPA - 8.1 '
        },
        {
            'degree': 'Higher Secondary (12th Standard)',
            'institution': 'Swamy Chidbhavananda Matric Higher Secondary School',
            'period': '2022 – 2023',
            'score': 'Percentage - 82%'
        }
    ],
    
    'projects': [
        {
            'name': 'FarmingAssist AI-Powered Mobile App',
            'role': 'Team Lead',
            'tech': 'Flutter, Firebase, APIs',
            'period': '10/2025 – Present',
            'description': [
                'Built a cross-platform full-stack Flutter application for AI-based farming guidance and crop insights',
                'Integrated Google Gemini API for conversational assistance and Open Weather API for weather updates',
                'Implemented secure authentication and data storage using Firebase Authentication and Firestore'
            ]
        },
        {
            'name': 'Generating Electricity from Human Footsteps',
            'role': 'Developer',
            'tech': 'Piezoelectric Sensors, Renewable Energy',
            'period': '08/2025 – 11/2025',
            'description': [
                'Converts energy from human footsteps into electricity using piezoelectric sensors',
                'The generated electricity is stored in batteries or capacitors',
                'Can power small devices like LEDs and mobile chargers'
            ]
        }
    ],
    
    'certifications': [
        'India International Science Festival (IISF) 2025 Hackathon Participant (International Level)',
        'Internship Training Certificate - Full Stack Web Development, Accent Techno Soft',
        'Front End Web Developer Certification - Infosys Springboard (May 2025)',
        'MongoDB Basics for Students - MongoDB University (July 2025)'
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=PORTFOLIO_DATA)

@app.route('/resume')
def resume():
    resume_path = os.path.join(app.static_folder, 'ANAS_MOHAMMED_RES.pdf')
    if os.path.exists(resume_path):
        return send_from_directory('static', 'ANAS_MOHAMMED_RES.pdf')
    else:
        abort(404, description="Resume file not found. Please contact the administrator.")

@app.errorhandler(404)
def not_found_error(error):
    return f"<h1>404 - File Not Found</h1><p>{error.description}</p>", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
