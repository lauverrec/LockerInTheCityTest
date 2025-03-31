# LockerInTheCityTest

python3 -m venv venv 

ACTIVARLO 

source venv/bin/activate

pip install -r requirements.txt

cd Docker -> docker-compose up

uvicorn main:app --reload

http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc