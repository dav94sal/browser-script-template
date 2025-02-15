# browser-script-template
A dynamic script that a user can tailor to their individuals needs

## Usage

### Clone this repository

`cd` into your desired path and `git clone` this repository

```bash
git clone https://github.com/dav94sal/browser-script-template.git
```

### Change origin url

If you want to save your customized script to your own repository, 
be sure to specify your repo's url using `git remote set-url origin`

```bash
git remote set-url origin <your-repo-url>
```

### Understand the code

This script is built to handle multiple data-sets. A `determine_data()` function in the `__main__.py` file 
prompts the user for their desired data set and returns that data to a variable. If only one dataset exists, 
the prompt is bypassed. Google Chrome is the default browser. 

<div align=center>
    <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXo1NG40dTNwcGVweDB2d2ZzZmk2ZHV5M2k0MXdlNzRvYjYxaDYzOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iPYNAEd8kKdK3AsMAk/giphy.gif" />
</div>

> May have to update chrome_path to your specific machine's path or
> Register a different browser of your choosing. You will need a name and a path to the browsers executable.

The utils module holds helper functions necessary for the script to run, as well as a space for customizing 
functions. The example present in the template uses two functions to 1) get a valid response from the user to
add a special url - "y" / "n" and 2) limit the number of times asked before redirecting to a previous prompt.
This function is passed into the data_2 object as the value for it's "customized" property. The "customized" 
property is checked by the `determine_data()` function so there is no need to refactor code.

```python
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
```

```python
from utils import handle_prompt

data_2 = {
    "input_key": "m",
    "name":"mental health",
    "customized": handle_prompt, # custom function to be executed if this dataset is chosen
    "urls": [
        "https://www.psychologytoday.com/us",
        "https://www.google.com/",
    ]
}

```

> Custom functions are meant to edit url lists, therefore a custom function should always return a list.

### Customize the data module

The data module is where you will do the majority of work needed to customize this script. I highly encourage
that you change the data's file name to match the theme of your dataset. For example, if you have a set of urls
that you need opened evertime you start work, then you could call this dataset 'work' on the "name" property,
`work_data_obj` for the variable and `work-data.py` for the file name. Your "input_key" property is whatever 
alphanumerical character you would like. Each file is a new dataset. Add or remove to your desire.

```python3
work_data_obj = {
    "input_key": "w", # The key needed to choose this dataset
    "name":"work", # The name that will show up in the prompt
    "customized": False, # Must be a custom function or false
    "urls": [ # replace urls with your own ]
}
```

> Sample urls are provided - replace with appropriate urls!
> `data.__init__.py` must be edited to reflect data changes. Simply add or change an existing import to your 
> new files and objects, then add all objects to the data_list. Done!

### Run Your Script

Using Command Prompt or PowerShell, run the script with `python browser-script-template`
Running this script in any shell that is isolated from your Operating system will merely print the urls. 


