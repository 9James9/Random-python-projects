import pyperclip
text = pyperclip.paste()
splitText = text.split('\n')
for i in range(len(splitText)):
    splitText[i] = f'* {splitText[i]}'
text = '\n'.join(splitText)
pyperclip.copy(text)