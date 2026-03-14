# Django REST Framework API Project

## Project Overview

This project is a simple API built using **Python, Django, and Django REST Framework**.
It demonstrates how to build RESTful APIs using serializers, viewsets, filtering, and pagination.

The goal of this project is to understand the basic structure of API development using Django REST Framework.

---

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite Database

---

## Features

* REST API endpoints
* Standardized serializers
* Filtering support
* Pagination using PageNumberPagination
* ViewSets and ModelViewSets
* Generic API views
* Mixins for reusable logic

---

## Project Concepts

### 1. Serializers

Serializers convert Django model objects into JSON format so they can be sent in API responses.
They also validate incoming request data before saving it to the database.

Example:

```
Model -> Serializer -> JSON Response
```

---

### 2. Filtering

Filtering allows users to retrieve specific data using query parameters.



---

### 3. Pagination

Pagination is used when the dataset is large.
Instead of returning all records, the API returns results in smaller pages.

This project uses **PageNumberPagination**.



**LIMIT**
Controls how many items appear in a single page.

**OFFSET**
Controls where the result set should start.

---

### 4. ViewSets

ViewSets combine multiple API operations in one class.

Example operations:

* List data
* Create data
* Update data
* Delete data

Instead of writing separate views, ViewSets handle these operations automatically.

---

### 5. ModelViewSet

ModelViewSet is a powerful class that automatically provides CRUD operations.

It supports:

* GET (retrieve data)
* POST (create data)
* PUT/PATCH (update data)
* DELETE (remove data)

This reduces a lot of repetitive code.

---

### 6. Mixins

Mixins provide reusable functionality that can be combined with generic views.

Common mixins include:

* CreateModelMixin
* ListModelMixin
* RetrieveModelMixin
* UpdateModelMixin
* DestroyModelMixin

These mixins allow developers to build flexible API views.

---

### 7. Generic Views

Generic views simplify common API operations such as creating, updating, and retrieving data.

Examples:

* ListAPIView
* CreateAPIView
* RetrieveAPIView
* UpdateAPIView
* DestroyAPIView

They reduce the amount of code needed to build APIs.

---





## Learning Outcome

This project helps developers understand:

* REST API development
* Django REST Framework architecture
* Serialization and data validation
* Pagination and filtering
* API view patterns

---

## Author

Developed by Aswini.
