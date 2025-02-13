"""
    An example of a data set WITH customization.
    "input_key" is the keystroke you want to use for this data_set
    and "name" is for reference in the custom prompt.
    This "customized" data_set contains a helper function that will
    further prompt the user and add a new url if desired

    ** DON'T FORGET TO UPDATE YOUR URLS! **
"""

from utils import handle_prompt

data_2 = {
    "input_key": "2",
    "name":"mental health",
    "customized": handle_prompt,
    "urls": [
        "https://www.psychologytoday.com/us",
        "https://www.google.com/",
    ]
}
