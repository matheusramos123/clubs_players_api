⚽ Clubs Players API

A simple API to manage players and clubs using FastAPI, SQLAlchemy (ORM), and MySQL (async). Perfect for learning database relationships and API development in Python.

🚀 Features

Add, update, delete, and list players

Add, update, delete, and list clubs

Asynchronous database access with SQLAlchemy + aiomysql

Clean API structure using FastAPI routers and Pydantic schemas

🛠️ Tech Stack

Python 3.11+

FastAPI

SQLAlchemy (ORM)

aiomysql

Pydantic

dotenv

📁 Project Structure
clubs_players_api/
│
├─ api/
│  └─ v1/
│     ├─ endpoints/
│     │  ├─ jogador.py      # Players endpoints
│     │  └─ times.py        # Clubs endpoints
│     └─ api.py             # Router aggregation
│
├─ core/
│  ├─ configs.py            # Settings and DB base model
│  └─ database.py           # Async DB session
│
├─ models/
│  ├─ jogadores.py
│  └─ times.py
│
├─ schemas/
│  ├─ jogadores_schema.py
│  └─ times_schema.py
│
├─ main.py                  # FastAPI app
├─ create_tables.py         # DB table creation
├─ requirements.txt
└─ .env                     # Environment variables (not tracked)

⚡ Installation
# Clone the repository
git clone https://github.com/matheusramos123/clubs_players_api.git

# Navigate to the project folder
cd clubs_players_api

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

🗄️ Database Setup

Create a .env file:

DATABASE_URL=mysql+aiomysql://user:password@localhost/db_name


Create tables:

python create_tables.py

🏃 Running the API
# Run the FastAPI server
python main.py


Access the interactive API docs at:

http://localhost:8080/api/v1/docs

🔗 Endpoints
Players (/api/v1/jogador)

POST /jogador – Create a player

GET /jogador – List all players

GET /jogador/{id} – Get player by ID

PUT /jogador/{id} – Update player

DELETE /jogador/{id} – Delete player

Clubs (/api/v1/times)

POST /times – Create a club

GET /times – List all clubs

GET /times/{id} – Get club by ID

PUT /times/{id} – Update club

DELETE /times/{id} – Delete club
