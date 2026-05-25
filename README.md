# Django Unit Testing

Small Django REST Framework practice project for testing a simple `Book` API.

## Project Layout

```text
Django-Unit-Testing/
├── README.md
└── UnitTesting/
    ├── manage.py
    ├── db.sqlite3
    ├── UnitTesting/
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    └── apitesting/
        ├── models.py
        ├── serializers.py
        ├── tests.py
        ├── urls.py
        └── views.py
```

## Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite

## Current Model

`Book` fields:

- `name`
- `author_name`
- `publish_date`

## API Routes

Configured routes in `apitesting/urls.py`:

- `GET /api/book_list_create/`
- `POST /api/book_list_create/`
- `GET|PUT|DELETE /api/book_get_update_delete/`

Note: the detail route is currently defined without a `pk` path parameter.

## Setup

Create and activate a virtual environment, then install Django and DRF:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install django djangorestframework
```

Run migrations:

```bash
cd UnitTesting
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## Running Tests

From the `UnitTesting/` directory:

```bash
python manage.py test
```

## Review Notes

Current issues found during review:

1. `BookDetailView` is referenced in [UnitTesting/apitesting/urls.py](/Users/apple/Documents/Personal_Code/Django-Unit-Testing/UnitTesting/apitesting/urls.py:8) but is not implemented in [UnitTesting/apitesting/views.py](/Users/apple/Documents/Personal_Code/Django-Unit-Testing/UnitTesting/apitesting/views.py:1), which will cause an import/load failure.
2. The detail URL does not accept a `pk`, but the tests reverse `book-detail` with `kwargs={'pk': ...}` in [UnitTesting/apitesting/tests.py](/Users/apple/Documents/Personal_Code/Django-Unit-Testing/UnitTesting/apitesting/tests.py:49).
3. `BookDetailViewTests` uses `title` and `author` fields in [UnitTesting/apitesting/tests.py](/Users/apple/Documents/Personal_Code/Django-Unit-Testing/UnitTesting/apitesting/tests.py:45), but the model defines `name` and `author_name` in [UnitTesting/apitesting/models.py](/Users/apple/Documents/Personal_Code/Django-Unit-Testing/UnitTesting/apitesting/models.py:5).
4. `test_create_book` contains an invalid assertion expression in [UnitTesting/apitesting/tests.py](/Users/apple/Documents/Personal_Code/Django-Unit-Testing/UnitTesting/apitesting/tests.py:35).
5. I could not execute the test suite in this environment because Django is not installed locally yet.

## Suggested Next Step

Implement `BookDetailView`, align the detail route with a `pk`, and update the tests so they use the actual `Book` model fields consistently.
