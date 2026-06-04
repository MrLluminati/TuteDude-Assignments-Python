# Assignment 9: Module 19 - REST API Using Django

This assignment is being implemented fresh in a beginner-friendly, step-wise manner.

## Portal task

Assignment 9 - Implementation of REST API USING DJANGO - Module 19.

## Numbering note

The available source PDF appears to use older numbering, but the portal shows this work as Assignment 9 under Module 19. This folder therefore follows the portal naming: `assignment_09_module_19_django_rest_api`.

## Project goal

Build a simple Django REST API project and test it locally.

The implementation will cover creating a Django project, creating a Django app, adding Django REST Framework, creating a model, creating a serializer, creating API endpoints, running migrations, testing the API, taking screenshots, and packaging the final project.

## Dependency note

The source assignment document mentioned `django-filter==2.4.0`. During implementation, that old version caused an import compatibility error with the installed Django version. Therefore, `django-filter` was upgraded to a compatible current version and the requirements file was updated accordingly.

Current `requirements.txt` contains:

```text
Django
djangorestframework
django-filter
```

## Current structure

```text
assignment_09_module_19_django_rest_api/
├── manage.py
├── requirements.txt
├── README.md
├── screenshot_proofs/
│   ├── step_01_project_setup/
│   ├── step_02_create_app_and_settings/
│   ├── step_03_model_and_migration/
│   └── step_04_serializer_and_api_view/
├── student_api/
└── students/
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── models.py
    ├── serializers.py
    └── views.py
```

## Step 1 - Django project setup

The initial Django project was created successfully. The development server was tested locally and the default Django success page opened in the browser.

Screenshot proofs:

- `screenshot_proofs/step_01_project_setup/step_01_a_project_files_and_runserver_start.png`
- `screenshot_proofs/step_01_project_setup/step_01_b_runserver_terminal_success.png`
- `screenshot_proofs/step_01_project_setup/step_01_c_django_default_page_browser.png`

## Step 2 - Create app and update settings

A Django app named `students` was created using `python manage.py startapp students`.

The project settings were updated to include:

- `rest_framework`
- `django_filters`
- `students`

After fixing the django-filter compatibility issue, `python manage.py check` ran successfully and returned no issues.

Screenshot proofs:

- `screenshot_proofs/step_02_create_app_and_settings/step_02_a_students_app_created_terminal_and_files.png`
- `screenshot_proofs/step_02_create_app_and_settings/step_02_b_settings_py_installed_apps_code.png`
- `screenshot_proofs/step_02_create_app_and_settings/step_02_c_django_filter_fix_and_manage_py_check.png`

## Step 3 - Create Student model and run migrations

A simple `Student` model was created in `students/models.py`.

The model fields are:

- `name`: stores the student name as text.
- `age`: stores the student age as an integer.
- `course`: stores the course name as text.

The model also includes a `__str__` method so that each student object displays by its name.

Migrations were created using `python .\manage.py makemigrations`, which created `students/migrations/0001_initial.py`.

Migrations were applied using `python .\manage.py migrate`. Django's default migrations and the new `students.0001_initial` migration were applied successfully.

Note: running migrations creates a local `db.sqlite3` file. This file is not committed because it is a local generated database file.

Screenshot proofs:

- `screenshot_proofs/step_03_model_and_migration/step_03_a_student_model_code.png`
- `screenshot_proofs/step_03_model_and_migration/step_03_b_makemigrations_terminal.png`
- `screenshot_proofs/step_03_model_and_migration/step_03_c_migrate_terminal.png`
- `screenshot_proofs/step_03_model_and_migration/step_03_d_migration_file_created.png`

## Step 4 - Create serializer and API view

A serializer file was created at:

```text
students/serializers.py
```

The `StudentSerializer` class was created using Django REST Framework's `ModelSerializer`. It converts `Student` model objects into JSON data for API responses.

The `students/views.py` file was updated with a simple API view named `student_list`.

The view:

- accepts GET requests;
- reads all student records using `Student.objects.all()`;
- converts the records into JSON using `StudentSerializer`;
- returns the serialized data as a REST API response.

The project check command ran successfully after these changes.

Screenshot proofs:

- `screenshot_proofs/step_04_serializer_and_api_view/step_04_a_serializers_py_code.png`
- `screenshot_proofs/step_04_serializer_and_api_view/step_04_b_views_py_api_view_code.png`
- `screenshot_proofs/step_04_serializer_and_api_view/step_04_c_manage_py_check_no_issues.png`

## Screenshot proof plan

Screenshot proof folders:

```text
step_01_project_setup/
step_02_create_app_and_settings/
step_03_model_and_migration/
step_04_serializer_and_api_view/
step_05_urls_and_api_testing/
step_06_final_testing/
```

## Progress checklist

- [x] Step 0: Rename workspace from old scaffold to portal Assignment 9 naming
- [x] Step 1: Create Django project and install dependencies
- [x] Step 2: Create app and update settings
- [x] Step 3: Create model and run migrations
- [x] Step 4: Create serializer and API view
- [ ] Step 5: Configure URLs and test API endpoint
- [ ] Step 6: Final testing and screenshots
- [ ] Step 7: Final packaging
