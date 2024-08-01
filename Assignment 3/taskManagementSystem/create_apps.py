import os

# List of app names to create
apps_to_create = ['task', 'taskCategory']

for app in apps_to_create:
    os.system(f'python manage.py startapp {app}')


# Add the apps to INSTALLED_APPS in settings.py
settings_file = 'taskManagementSystem/settings.py'

with open(settings_file, 'r') as file:
    lines = file.readlines()

for app in apps_to_create:
    for i, line in enumerate(lines):
        if 'INSTALLED_APPS' in line:
            indent = ' ' * (len(line) - len(line.lstrip())) + '    '  # Four spaces (or tab) before the app name
            lines.insert(i + 1, f"{indent}'{app}',\n")
            break

with open(settings_file, 'w') as file:
    file.writelines(lines)