# Assignment 9: Module 19 - REST API Using Django

This folder now contains both the original submitted version and the corrected resubmission version of Assignment 9.

## Portal task

Assignment 9 - Implementation of REST API USING DJANGO - Module 19.

## Assignment document note

The assignment document available to the learner broadly mentioned implementing a REST API using Django and uploading the compressed project files. It did not expressly mention that the implementation must include `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`, a detail endpoint, or proof of all CRUD operations.

After mentor feedback, the project has been revised to include full CRUD functionality using Django REST Framework class-based generic views.

## Folder structure

```text
assignment_09_module_19_django_rest_api/
├── README.md
├── original_submission/
│   ├── manage.py
│   ├── requirements.txt
│   ├── screenshot_proofs/
│   ├── student_api/
│   └── students/
└── resubmission/
    ├── manage.py
    ├── requirements.txt
    ├── screenshot_proofs/
    ├── student_api/
    └── students/
```

## Folder purpose

### `original_submission/`

This folder preserves the first submitted version of the project.

The original submission included:

- Django project setup.
- `students` app setup.
- `Student` model.
- `StudentSerializer`.
- Function-based GET API view.
- `/api/students/` list endpoint.
- Screenshot proofs for setup and GET endpoint testing.

The original submission was rejected because it did not include complete CRUD operations and did not use the expected class-based generic views.

### `resubmission/`

This folder contains the revised version prepared after mentor feedback.

The resubmission now includes:

- `StudentListCreateView` using `ListCreateAPIView`.
- `StudentDetailView` using `RetrieveUpdateDestroyAPIView`.
- List/create endpoint: `/api/students/`.
- Detail/retrieve/update/delete endpoint: `/api/students/<id>/`.
- Screenshot proofs for create, read, update, and delete operations.

## Resubmission implementation summary

The corrected implementation uses Django REST Framework generic class-based views.

`students/views.py` includes:

```python
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

`students/urls.py` includes:

```python
urlpatterns = [
    path("students/", StudentListCreateView.as_view(), name="student-list-create"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
]
```

## Resubmission API endpoints

```text
GET     /api/students/       List all students
POST    /api/students/       Create a new student
GET     /api/students/<id>/  Retrieve one student
PUT     /api/students/<id>/  Fully update one student
PATCH   /api/students/<id>/  Partially update one student
DELETE  /api/students/<id>/  Delete one student
```

## Resubmission screenshot proofs

```text
resubmission/screenshot_proofs/
├── resubmission_step_00_restructure/
├── resubmission_step_01_class_based_crud_views/
├── resubmission_step_02_list_create_endpoint/
└── resubmission_step_03_detail_update_delete_endpoint/
```

## Resubmission progress checklist

- [x] Step R0: Preserve original submission and create separate resubmission folder
- [x] Step R1: Refactor API views to class-based CRUD views
- [x] Step R2: Test list/create endpoint with actual student records
- [x] Step R3: Test detail endpoint with retrieve, update, and delete operations
- [ ] Step R4: Create final resubmission ZIP
