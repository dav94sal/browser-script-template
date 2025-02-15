def build_prompt(data_list):
    """
        Takes the name and input key of all data sets and joins them together
        to create an automatic prompt
    """
    prompt_list = []

    for i in range(len(data_list)):
        data = data_list[i]
        cmd = f'{data["input_key"]}/{data["name"]}'
        prompt_list.append(cmd)

    return ' or '.join(prompt_list) + ': '


def get_urls(data):
    if data["customized"]:
        urls = data["customized"](data["urls"])
        if len(urls):
            return urls
    else:
        return data["urls"]
