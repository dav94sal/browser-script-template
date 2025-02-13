# Changes to data must be reflected here!
# Change variable names to reflect your data
from .mental_health_data import mental_health_dict
from .job_seeking_data import job_dict


# This list is being used to create your custom prompt,
# Be sure to update it with the proper data!
data_list = [
    job_dict,
    mental_health_dict
]
