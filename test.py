import json
# file_paths = {'INPUT_PATH': 'fds',
#               'OUT_PATH':'dfads'}
#
# with open('default_setting.txt','w') as file:
#     file.write(json.dumps(file_paths))


with open('default_setting.txt','r') as file:
    DEFAULT_SETTING = file.read()
print(DEFAULT_SETTING)