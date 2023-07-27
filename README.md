# Django NewsPress

Django NewsPress is a web application built with Django framework that allows users to read and publish news articles. It provides features such as user registration, authentication, article creation, editing, and more.

## Features

- User Registration: Users can create an account to access additional features.
- User Authentication: Secure login and logout functionality for registered users.
- Article Management: Create, edit, and delete news articles.
- User Profiles: Users can view and update their profile information.
- Responsive Design: The app is built with HTML, CSS, and Bootstrap for a mobile-friendly experience.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/h3itham/DjangoNewsPress
   ```
2. Create a virtual environment:

   ```
   python -m venv env 
   ```

   3. Activate the virtual environment:

      - For Windows:

        ```bash
        .\env\Scripts\activate
        ```
      - For macOS/Linux:

        ```bash
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

      ```
      python manage.py runserver
      ```
   7. Open your web browser and visit `http://localhost:8000` to access the application.

## Usage

- Register a new account or log in with existing credentials.
- Browse the articles on the homepage.
- Click on an article to view its details.
- Authenticated users can create, edit, and delete their own articles.
- Update your profile information by clicking on your username in the navigation bar.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

