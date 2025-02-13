import time

def get_valid_input(urls):
    """
        A function to determine if the user needs a tab for their Total Behavioral Health appointment
    """

    appt = input('Do you have an appointment today? ')

    # Continuously prompt user until a valid response is given
    if appt != 'n' and appt != 'y':
        print('Please enter "y" for yes or "n" for no... ')
        time.sleep(3)
        return False

    if appt == 'y':
        print('Adding Total Behavioral Health tab! ')
        urls.append("https://total.doxy.me/behavioral")
        time.sleep(1)
        print("sorting urls...")
        urls.sort(reverse=True)

    return urls


def handle_prompt(urls):
    # Prompt user for a valid response
    # up to limit times
    counter = 0
    limit = 5
    valid_input = None

    while not valid_input:
        counter = counter + 1
        if counter >= limit:
            break
        valid_input = get_valid_input(urls)

    return valid_input
