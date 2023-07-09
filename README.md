# Asset Tracking App

The Asset Tracking App is a Django-based web application that allows companies to track and manage their corporate assets such as phones, tablets, laptops, and other gears assigned to employees.

## Features

- Companies can add and manage their employees.
- Companies can delegate devices to employees for a certain period of time.
- Keep track of device check-out and return dates.
- Log the condition of devices when they are checked out and returned.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/asset-tracking-app.git
```

2. Create a virtual environment:

```bash
cd asset-tracking-app
python -m venv env
```

3. Activate the virtual environment:

```bash
# For Windows
env\Scripts\activate

# For macOS/Linux
source env/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open your web browser and visit `http://localhost:8000` to access the Asset Tracking App.

## Usage

- Register a new company and add employees.
- Assign devices to employees for a specific period.
- Check the device check-out and return dates.
- Log the condition of devices during check-out and return.

## Technologies Used

- Django
- Django REST Framework
- HTML
- CSS
- Bootstrap

## Folder Structure

- `asset_tracking/`: Django project configuration settings.
- `asset_management/`: Django app for asset management.
- `templates/`: HTML templates for rendering frontend.
- `static/`: Static files such as CSS and JavaScript.
- `api/`: API endpoints for asset management.
- `models.py`: Database models for assets, employees, and check-out records.
- `views.py`: Views and API endpoints logic.
- `urls.py`: URL patterns for routing requests.
- `requirements.txt`: Required Python dependencies.

## Contributing

Contributions to the Asset Tracking App are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request with a description of your changes.

Feel free to modify and customize the content according to your project's specific details and requirements.
