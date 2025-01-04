import os
from datetime import datetime

# Define the base repo folder
repo_folder = "./"

# Function to create a folder for today's practice
def create_daily_folder():
    today_date = datetime.now().strftime('%d_%m_%Y')
    daily_folder = os.path.join(repo_folder, 'daily_practice', today_date)

    # Create the folder for today's practice
    os.makedirs(daily_folder, exist_ok=True)
    print(f"Created folder: {daily_folder}")


# Optionally, create a folder for today's practice
create_daily_folder()
