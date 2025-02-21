import time
import subprocess

def get_valid_input(urls, isMaxed):
    """
        A function to determine if the user needs a tab for their Total Behavioral Health appointment
    """

    appt = input('\nDo you have an appointment today? ')

    # Prompt user for a valid response
    if appt != 'n' and appt != 'y':
        err = '\nPlease enter "y" for yes or "n" for no... '
        if (isMaxed):
            err = '\nLimit reached, try again\n'
            subprocess.run("clear", shell=True)
        print(err)
        # time.sleep(1)
        return False

    if appt == 'y':
        print('Adding Total Behavioral Health tab! ')
        urls.append("https://totalbehavioral.com/")
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

    while not valid_input and counter < limit:
        # print("Counter: ", counter)
        counter = counter + 1
        valid_input = get_valid_input(urls, counter == limit)

    if valid_input:
        return valid_input
    else:
        return []
