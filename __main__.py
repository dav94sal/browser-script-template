import webbrowser
import time
from data import job_dict, mental_health_dict
from utils import handle_prompt

data = None

def determine_data():
    """
        A function to determine which data the user wants to use
    """

    print("Which data set would you like to use? ")
    data = input('j/jobs or m/mental health: ')

    if data == job_dict["input_key"]:
        return job_dict["urls"]
    elif data == mental_health_dict["input_key"]:
        return handle_prompt(mental_health_dict["urls"])
    else:
        print("Please select a valid option...")
        time.sleep(1)
        return determine_data()


urls = determine_data()

# Register Google Chrome as the default browser
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Open each URL in Google Chrome with a delay
for url in urls:
    print(url)
    webbrowser.get('chrome').open_new(url)
    time.sleep(1)  # Wait for 1 second before opening the next URL
