Vehicle Management Application - How to Run

1. Clone the repository:
   git clone https://github.com/USERNAME/REPO_NAME.git
   cd REPO_NAME

2. Create and activate a virtual environment:
   Windows:
     python -m venv venv
     venv\Scripts\activate

   Mac/Linux:
     python3 -m venv venv
     source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Apply migrations:
   python manage.py migrate

5. Create a super user (admin):
   python manage.py createsuperuser

6. Start the development server:
   python manage.py runserver

7. Open the app in browser:
   http://127.0.0.1:8000/

8. Login to admin panel:
   http://127.0.0.1:8000/admin/

User Roles:
  - Super Admin: Create, Edit, Delete, View
  - Admin: Edit, View
  - User: View only

Notes:
  - Database file will be created automatically.
  - Use virtual environment to avoid conflicts.
