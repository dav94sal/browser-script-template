import webbrowser
import time
from data import data_list
from utils import build_prompt, get_urls

def determine_data():
    """
        A function to determine which data the user wants to use
    """

    if len(data_list) == 1:
        data = data_list[0]
        return get_urls(data)

    prompt = build_prompt(data_list)
    print("Which data set would you like to use? ")
    user_input = input(prompt)

    for i in range(len(data_list)):
        data = data_list[i]

        if user_input == data["input_key"]:
            return get_urls(data)

    print("Please select a valid option...\n")
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
