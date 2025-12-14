# Tech Stack
1. [x] Framework: Flask
2. [x] Package Management: Poetry
3. [x] Database: PostgreSQL
4. [x] ORM/Migration: SQLAlchemy / Flask-Migrate
5. [x] Architecture: Application Factory & Modular Blueprints (Domains)

# Usage

### Requirements
1. Python 3.12+
2. Poetry

## Database Migrations (Schema Changes)
When you make changes to your SQLAlchemy models, use the following commands; \
- If you haven't migrations file -> `flask db init`
- Create Migration File ->
`flask db migrate -m "Added new models"`\
- Apply Migrations -> `flask db upgrade`

## With Docker

### Build a image
docker compose build

### Up the image
docker compose up

## Without docker

### Create Tables
This command initializes the database schema based on your current SQLAlchemy models.\
`flask init-db`

### Run the App
Start the development server using the Flask CLI. The application will be accessible at \
`flask run`