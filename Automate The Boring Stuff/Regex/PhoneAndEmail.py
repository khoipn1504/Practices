import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                      # area code
    (\s|-|\.)?                              # sep
    (\d{3})                                 # first 3 digits
    (\s|-|\.)                               # sep
    (\d{4})                                 # last 4 digit
    (\s*(ext|x|ext.)\s*(\d{2,5}))?          # extension

)''', re.VERBOSE)

# TODO: Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                       # user name
    @                                       # @ symbol
    [a-zA-Z0-9.-]+                          # domain name
    (\.[a-zA-Z]{2,4})                       # dot-somthing
)''', re.VERBOSE)

# TODO: Find match in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x'+groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')
    