# Jobsite

## Overview
The `jobsite` is a web-based application designed to facilitate job postings and job searches. It is built using the Django framework for the backend and incorporates frontend technologies such as HTML, CSS, and JavaScript.

## Key Features
- **User Management:** Includes authentication and authorization features, allowing different access levels for job seekers and employers.
- **Job Postings:** Users can create and manage job listings, providing details such as job title, description, and requirements.
- **Job Search:** Job seekers can browse and search for job opportunities based on various criteria.

## Technical Details
- **Backend:** Implemented using Django, a high-level Python web framework.
- **Frontend:** Built with HTML, CSS, and JavaScript to create a responsive and user-friendly interface.
- **Dependencies:** Managed through a `requirements.txt` file listing necessary Python packages.

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/abdullah-xyz/jobsite.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd jobsite
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source env/bin/activate
     ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   Open a web browser and navigate to `http://localhost:8000`.

## Considerations
- **Database Configuration:** This repository uses sqlite by default, additionally databasse settings can be configured in `settings.py` as per your enviroment.

## Screenshots
![list posting][./Screenshots/listing.png]
![posting details][./Screenshots/details.png]
![create posting][./Screenshots/creation.png]
