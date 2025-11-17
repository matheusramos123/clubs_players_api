Clubs Players API

Clubs Players API is a FastAPI project designed to manage football clubs and their players. It uses SQLAlchemy ORM with MySQL/MariaDB as the database backend and follows best practices for API development.

Table of Contents

Features

Technologies

Installation

Configuration

Usage

API Endpoints

License

Features

CRUD operations for clubs (teams) and players.

Players are associated with their respective teams.

Built with FastAPI, SQLAlchemy ORM, and async database sessions.

Environment variables used for secure configuration.

Ready for expansion with additional features.

Technologies

Python 3.11+

FastAPI

SQLAlchemy (async)

Pydantic

MySQL / MariaDB (via aiomysql)

Uvicorn (ASGI server)

Python-dotenv

Installation

Clone the repository:

git clone https://github.com/matheusramos123/clubs_players_api.git
cd clubs_players_api


Create and activate a virtual environment:

python -m venv env
# Windows
env\Scripts\activate
# macOS / Linux
source env/bin/activate


Install dependencies:

pip install -r requirements.txt

Configuration

Create a .env file in the root of the project:

DATABASE_URL=mysql+aiomysql://username:password@localhost:3306/database_name


Replace username, password, and database_name with your database credentials.

Usage

Create database tables:

python create_tables.py


Run the API:

python main.py


Open your browser or API client (e.g., Postman) at:

http://127.0.0.1:8080/api/v1/docs


You can see the interactive Swagger UI documentation there.

API Endpoints
Teams

GET /api/v1/times: List all teams

GET /api/v1/times/{id}: Get team by ID

POST /api/v1/times: Create a new team

PUT /api/v1/times/{id}: Update team info

DELETE /api/v1/times/{id}: Delete a team

Players

GET /api/v1/jogador: List all players

GET /api/v1/jogador/{id}: Get player by ID

POST /api/v1/jogador: Create a new player

PUT /api/v1/jogador/{id}: Update player info

DELETE /api/v1/jogador/{id}: Delete a player
