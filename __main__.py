import webbrowser
import time

data = None

def determine_data():
    """
        A function to determine which data the user wants to use
    """

    print("Which data set would you like to use? ")
    data = input('j/jobs or m/mental health: ')

    if data == 'j':
        from data import job_urls
        return job_urls
    elif data == 'm':
        from data import mental_health_urls
        valid_input = None

        # Continuously prompt user until a valid response is given
        counter = 0
        while not valid_input:
            counter = counter + 1
            if counter >= 5:
                break
            valid_input = get_valid_input()

        if valid_input == 'y':
            print('Adding Total Behavioral Health tab! ')
            mental_health_urls.append("https://total.doxy.me/behavioral")
            time.sleep(1)
            print("sorting urls...")
            mental_health_urls.sort(reverse=True)

        return mental_health_urls
    else:
        print("Please select a valid option...")
        time.sleep(1)
        return determine_data()



def get_valid_input():
    """
        A function to determine if the user needs a tab for their Total Behavioral Health appointment
    """

    appt = input('Do you have an appointment today? ')

    if appt == 'n' or appt == 'y':
        return appt

    print('Please enter "y" for yes or "n" for no... ')
    time.sleep(3)
    return False



urls = determine_data()

# Register Google Chrome as the default browser
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Open each URL in Google Chrome with a delay
for url in urls:
    print(url)
    webbrowser.get('chrome').open_new(url)
    time.sleep(1)  # Wait for 2 seconds before opening the next URL
