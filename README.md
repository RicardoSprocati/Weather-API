Weather Minimal API (Docker)

API em FastAPI que consome a OpenWeather, salva no PostgreSQL e expõe:

GET / — página HTML minimalista

POST /weather/ingest?city=Florianopolis,BR — busca e salva

GET /weather — consulta dados salvos

GET /docs — Swagger

1) Pré-requisitos

Docker Desktop instalado e em execução

2) Baixar o projeto
git clone https://github.com/RicardoSprocati/Weather-API.git

cd weather-api

3) Configurar variáveis (.env)
Copy-Item .env.example .env


Edite o arquivo .env e informe:

OPENWEATHER_API_KEY=SUA_CHAVE_AQUI

DATABASE_URL=postgresql+psycopg://postgres:postgres@db:5432/weather

4) Subir com Docker

docker compose up --build

5) acessar 

API: http://localhost:8000