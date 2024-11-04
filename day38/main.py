import requests
from datetime import datetime
import os

today = datetime.today().strftime("%d/%m/%Y")
time_now = str(datetime.now().time()).split(".",1)[0]

APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
GENDER = "female"
WEIGHT_KG = "79"
HEIGHT_CM = "158"
AGE = "24"

user_input = input("What type of exercise did you do today?")

exercise_params = {
    "query": user_input,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]
excercise_result = requests.post(url=API_ENDPOINT,json=exercise_params,headers=headers)
result = excercise_result.json()['exercises']
for excercise in result:
    to_add = { "workout": {
        "date": today,
        "time": time_now,
        "exercise":result["user_input"],
        "duration": result["duration_min"],
        "calories": result["nf_calories"]
    }
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=to_add,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"],
        )
    )
# post_row = requests.post(url="https://api.sheety.co/e3dd3050aa80bb776bbb5027b799b5de/workoutTracking/workouts",json=to_add)
