import datetime
import requests

# Get current date
current_date = datetime.datetime.now()

# Extract day, month, and year
day = current_date.day
month = current_date.month
year = current_date.year

if month < 10:
    month_str = f"0{month}"
else:
    month_str = str(month)

if day < 10:
    day = f"0{day}"
else:
    day = str(day)

# Construct the link using variables
link = f"https://nytimes.com/svc/wordle/v2/{year}-{month_str}-{day}.json"

# Fetch data from the link
response = requests.get(link)

# Check if request was successful
if response.status_code == 200:
    data = response.json()

    # Extract the solution word
    try:
        solution = data['solution']
        print("The wordle answer for today is:", solution)
    except KeyError:
        print("No word data found in the response.")
else:
    print("Failed to fetch Wordle data from the server.")

input(" ")
