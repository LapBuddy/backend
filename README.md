# backend
Backend API for the LapBuddy application

## Run it Locally
Let's get the backend running on your local machine.

Only do these steps if this is your first time setting up the application:
- in ~/api, run `python -m venv venv` to create a virtual environment
- in ~/api, run `source venv/Scripts/activate` to start up the virtual environment
- Now, you can download the required dependencies to the environment: `pip install -r requirements.txt`
- You need to create a `.env` file in ~/api, it needs to have one thing: `SECRET_KEY=SuperSecretKey`, make this something super secret  
- Next, apply the project's existing migrations: `python manage.py migrate`
- Next, create a super user (used for cool admin stuff) `python manage.py createsuperuser`, remember those credentials as they're needed to inspect any protected endpoints
- Then you can just run `./init.sh` to boot up the backend

If this isn't the first time you're running the backend, just run the init script.