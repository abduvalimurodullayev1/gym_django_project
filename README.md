Features
Contact Form
Implement a contact form using Django forms to allow users to send messages.
Blog Listing
Display a paginated list of blog posts on the /blog/ page.
Blog Details View
View detailed information about each blog post, including comments, on /blog/<post-slug>/.
Admin Interface for Adding Blogs
Admin users can log in and add new blog posts through the Django admin interface (/admin/).
Comments Functionality
Users can leave comments on blog posts, which are displayed on the respective post detail page.
Installation
To run this project locally, follow these steps:

Clone Repository:

bash
Copy code
git clone https://github.com/abduvalimurodullayev1/gym_django_project.git
cd your-repository
Install Requirements:

Copy code
pip install -r requirements.txt
Apply Migrations:

Copy code
python manage.py migrate
Create Superuser (Optional):

Copy code
python manage.py createsuperuser
Run Server:

Copy code
python manage.py runserver
Access Application:
Open your web browser and go to http://localhost:8000/

Usage
Homepage: Visit / to see the homepage with basic information.
Blog: Navigate to /blog/ to view all blog posts with pagination.
Single Post: Click on a post title to view its details and comments at /blog/<post-slug>/.
About: Access /about/ for information about the project.
Contact: Use /contact/ to send messages via the contact form.
Admin Interface
Access the Django admin interface at /admin/ to add, edit, or delete blog posts. Log in using the superuser credentials created during installation.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

