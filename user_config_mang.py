def add_setting(setting, new_set):
    key = new_set[0].lower()
    value = new_set[1].lower()

    if key in setting:
        return f'Setting {key} already exists! Cannot add a new setting with this name.'
    else:
        return f'Setting {key} added with value {value} successfully!'

def update_setting(setting, new_set):
    key = new_set[0].lower()
    value = new_set[1].lower()
    if key in setting:
        setting.update({key:value})
        return f'Setting {key}.lower() updated to {value}.lower() successfuly!'
    else:
        return f'Setting {key}.lower() does not exist! Cannot update a non-existing setting.'

def delete_setting(setting, new_set):
    key = new_set.lower()
    if key in setting:
        del setting[key]
        return 'Setting {key}.lower() deleted successfully!'
    else:
        return 'Setting not found'

def view_settings(setting):
    if not setting:
        return 'No settings available.'
    display = 'Current User Settings:'
    for key, value in setting.items():
        display += f'\n{key.capitalize()}: {value}'
    return display

test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

print(view_settings(test_settings))