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
│   └── step_02_create_app_and_settings/
├── student_api/
└── students/
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
- [ ] Step 3: Create model and run migrations
- [ ] Step 4: Create serializer and API view
- [ ] Step 5: Configure URLs and test API endpoint
- [ ] Step 6: Final testing and screenshots
- [ ] Step 7: Final packaging
