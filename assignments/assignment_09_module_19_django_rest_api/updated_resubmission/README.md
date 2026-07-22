# Assignment 9 - Django REST API

Student: Abhijeet Kumar
Project: Blog Post Management API
Technology: Django REST Framework

## Project Description

This project is a REST API for managing blog posts. Users must log in before accessing the API. Each user can create, view, update and delete only their own posts.

## Main Features

- Authenticated blog post CRUD operations
- Session authentication
- Token authentication
- Owner-based post access
- Pagination with five posts per page
- Search by post title and content
- Ordering by post ID
- Filtering by creation date
- SQLite database
- Django REST Framework browsable API
- Automated API tests

## Project Structure

- blog/ - Django project configuration
- helloworld/ - Blog API application
- helloworld/models.py - Post database model
- helloworld/serializers.py - Post serializer
- helloworld/views.py - API views
- helloworld/permissions.py - Owner permission
- helloworld/filters.py - Creation-date filters
- helloworld/tests.py - Automated API tests
- db.sqlite3 - SQLite database
- manage.py - Django management file

## Installation

Run these commands from the updated_resubmission folder:

    python -m pip install -r requirements.txt
    cd blog
    python manage.py migrate

## Running the Project

From the blog folder, run:

    python manage.py runserver

Open:

    http://127.0.0.1:8000/api/posts/

Stop the development server by pressing Ctrl + C in the terminal where it is running.

## API Endpoints

- /api/posts/ - List and create posts
- /api/posts/<id>/ - Retrieve, update and delete a post
- /api-auth/login/ - Session authentication login
- /api-auth/logout/ - Session authentication logout
- /api/token/ - Obtain an authentication token

## Query Parameters

Search:

    /api/posts/?search=Filtering

Ordering:

    /api/posts/?ordering=id
    /api/posts/?ordering=-id

Creation-date filtering:

    /api/posts/?created_after=2026-07-19
    /api/posts/?created_before=2026-07-21

Pagination:

    /api/posts/?page=2

## Demo Users

These accounts are provided only for local assignment testing.

First user:

    Username: abhijeet
    Password: BlogApi@2026

Second user:

    Username: otheruser
    Password: OtherUser@2026

## Automated Tests

From the blog folder, run:

    python manage.py test

The automated tests verify authentication, CRUD operations, owner isolation, pagination, filtering, search, ordering and token authentication.
