# JITIBU Hospital Management System

![JITIBU Logo](https://via.placeholder.com/150x50?text=JITIBU)

## Overview

JITIBU is a comprehensive hospital management system built with Django. It streamlines operations for healthcare facilities by managing patient records, appointment scheduling, inventory, billing, and more in a single integrated platform.

Developed by Steve Ongera and Linda Mputhia, JITIBU aims to enhance healthcare delivery through efficient digital solutions.

## Features

### Patient Management
- Patient registration and profile management
- Medical history tracking
- Digital health records
- Patient appointment history
- Insurance information management

### Appointment System
- Scheduling and managing appointments
- Automated reminders via email and SMS
- Calendar view for doctors and staff
- Waitlist management
- Rescheduling capabilities

### Staff Management
- Doctor and nurse profiles
- Staff scheduling
- Attendance tracking
- Performance analytics
- Leave management

### Billing and Finance
- Automated billing
- Invoice generation
- Payment tracking
- Insurance claims processing
- Financial reporting

### Pharmacy and Inventory
- Medicine inventory management
- Prescription management
- Low stock alerts
- Expiry tracking
- Purchase order management

### Laboratory Management
- Test orders and results tracking
- Sample management
- Integration with diagnostic equipment
- Results reporting

### Reporting and Analytics
- Customizable dashboards
- Patient statistics
- Financial reports
- Resource utilization analytics
- Operational efficiency metrics

### Security Features
- Role-based access control
- Data encryption
- Audit trails
- Compliance with healthcare data regulations

## Technology Stack

- **Backend Framework**: Django 4.2
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **API**: Django REST Framework
- **Authentication**: Django Authentication System with JWT
- **Deployment**: Docker, Nginx
- **CI/CD**: GitHub Actions
- **Cloud Services**: AWS (S3 for storage)

## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL 13+
- pip
- virtualenv (recommended)
- Git

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/steveongera/jitibu.git
cd jitibu
```

2. **Create and activate virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root with the following variables:

```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://username:password@localhost:5432/jitibu
EMAIL_HOST=smtp.yourprovider.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your_s3_bucket_name
```

5. **Apply migrations**

```bash
python manage.py migrate
```

6. **Create a superuser**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

8. **Access the application**

Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

```
jitibu/
├── accounts/            # User authentication and profiles
├── appointments/        # Appointment scheduling system
├── billing/             # Billing and financial operations
├── core/                # Core application settings
├── dashboard/           # Admin and user dashboards
├── inventory/           # Pharmacy and equipment inventory
├── laboratory/          # Lab tests and results
├── patients/            # Patient record management
├── reports/             # Reporting and analytics
├── staff/               # Staff management
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── .env                 # Environment variables
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

## Configuration

### Setting Up Email Notifications

To enable email notifications for appointments, staff communications, and system alerts:

1. Configure email settings in the `.env` file
2. Set up background tasks (using Celery):

```bash
# Install Celery and Redis
pip install celery redis

# Start the Redis server
docker run -d -p 6379:6379 redis

# Start Celery worker
celery -A jitibu worker -l info
```

### Configuring SMS Notifications

1. Sign up for a service like Twilio or Africa's Talking
2. Add your API credentials to the `.env` file
3. Configure the SMS service in `settings.py`

## Usage

### Admin Dashboard

The admin dashboard is accessible at `/admin/` after logging in with superuser credentials. From here, you can:

- Manage users and staff
- Configure system settings
- View and generate reports
- Manage hospital departments

### User Roles

1. **Admin**: Full system access
2. **Doctor**: Access to patient records, appointments, prescriptions
3. **Nurse**: Limited patient record access, vitals recording
4. **Receptionist**: Appointment scheduling, patient registration
5. **Pharmacist**: Medication dispensing, inventory management
6. **Lab Technician**: Test orders and results management
7. **Billing Staff**: Invoice generation, payment processing

## API Documentation

JITIBU provides a comprehensive API for integration with other healthcare systems. API documentation is available at `/api/docs/` when the server is running.

### Sample API Endpoints

```
GET /api/patients/ - List all patients
POST /api/appointments/ - Create a new appointment
GET /api/doctors/ - List all doctors
```

## Testing

To run tests:

```bash
python manage.py test
```

For coverage report:

```bash
coverage run --source='.' manage.py test
coverage report
```

## Deployment

### Using Docker

1. Build the Docker image:

```bash
docker build -t jitibu .
```

2. Run the container:

```bash
docker run -p 8000:8000 jitibu
```

### Deployment to Production

For a production environment, we recommend:

1. Using Gunicorn as the WSGI server
2. Nginx as a reverse proxy
3. PostgreSQL on a dedicated server
4. Redis for caching and as a Celery broker
5. Regular backups of the database

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- Mobile application integration
- Telemedicine module
- AI-powered diagnosis suggestions
- Advanced analytics dashboard
- Multi-hospital support
- Patient portal enhancements

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Steve Ongera - steve.ongera@example.com
Linda Mputhia - linda.mputhia@example.com

Project Link: [https://github.com/steveongera/jitibu](https://github.com/steveongera/jitibu)

## Acknowledgements

- Django Project
- Bootstrap
- Chart.js
- DataTables
- All our contributors and healthcare professionals who provided domain expertise