"""
    An example of a data set WITH customization.
    "input_key" is the keystroke you want to use for this data_set
    and "name" is for reference in the custom prompt.
    This "customized" data_set contains a helper function that will
    further prompt the user and add a new url if desired

    ** DON'T FORGET TO UPDATE YOUR URLS! **
"""

from utils import handle_prompt

mental_health_dict = {
    "input_key": "m",
    "name":"mental health",
    "customized": handle_prompt,
    "urls": [
        "https://docs.google.com/document/d/1y6-LV9h100EzaoJvVpzRfKRiHtfDMw8Ce1jVPi9xgzI/edit?tab=t.0",
        "https://docs.google.com/document/d/16M6FZE4LLRqVZ2ND1IMgdN9JiF6maQ3jyjkDnoyxOtk/edit?tab=t.0",
    ]
}
