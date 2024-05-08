echo "[INFO] Initializing environment and server, please ensure a .env file is configured in ./api/"
source venv/scripts/activate
export ENV_FILE=.env
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver