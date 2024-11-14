
# SCA Project

This is a Django-based API for managing cats and missions, where you can create, update, and delete cats and missions, as well as retrieve specific cat and mission data.

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create a virtual environment

For Windows:

```bash
python -m venv venv
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on the provided `env.example` and populate it with the necessary configuration.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Cats Endpoints

1. **List Cats**  
   `GET /api/cats/`  
   Retrieves a list of all cats.

2. **Get Cat by ID**  
   `GET /api/cats/{id}/`  
   Retrieves a specific cat by ID.

3. **Create Cat**  
   `POST /api/cats/`  
   Creates a new cat.  
   Example request body:

   ```json
   {
       "name": "Whiskers1",
       "years_of_experience": 5,
       "breed": "siamese",
       "salary": "2500.00"
   }
   ```

4. **Update Cat**  
   `PATCH /api/cats/{id}/`  
   Updates an existing cat.  
   Example request body:

   ```json
   {
       "name": "Whiskers1",
       "years_of_experience": 10,
       "breed": "siamese",
       "salary": "2500.00"
   }
   ```

5. **Delete Cat**  
   `DELETE /api/cats/{id}/`  
   Deletes a specific cat.

### Missions Endpoints

1. **Create Mission**  
   `POST /api/missions/`  
   Creates a new mission.  
   Example request body:

   ```json
   {
       "cat": 4,
       "complete": true,
       "targets": [
           {
               "name": "target1",
               "country": "UA",
               "notes": "test note 1",
               "complete": false
           },
           {
               "name": "target2",
               "country": "GB",
               "notes": "test note 2",
               "complete": false
           }
       ]
   }
   ```

2. **Get Mission**  
   `GET /api/missions/`  
   Retrieves a list of all missions.

3. **Get Mission by ID**  
   `GET /api/missions/{id}/`  
   Retrieves a specific mission by ID.

4. **Update Mission**  
   `PATCH /api/missions/{id}/`  
   Updates an existing mission.  
   Example request body:

   ```json
   {
       "id": 13,
       "cat": 4,
       "complete": true,
       "targets": [
           {
               "id": 7,
               "name": "target6",
               "country": "UA",
               "notes": "test note 6",
               "complete": false,
               "mission": 13
           },
           {
               "id": 8,
               "name": "target7",
               "country": "GB",
               "notes": "test note 7",
               "complete": false,
               "mission": 13
           }
       ]
   }
   ```

5. **Delete Mission**  
   `DELETE /api/missions/{id}/`  
   Deletes a specific mission.

## Requirements

- Python 3.8+
- Django 5.1.3
- psycopg2-binary 2.9.8
- djangorestframework 3.14.0
- python-dotenv 1.0.1

## Environment Variables

Create a `.env` file based on the `env.example` file provided. This file should contain necessary environment variables, such as database credentials and other settings.

