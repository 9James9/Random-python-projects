import pyperclip, re
def extract():
    info = pyperclip.paste()
    phoneNumRegex = re.compile("""
    [(\( )]?
    \d{3}
    [(\( )]?
    [-.,]?
    \d{3}
    [-.,]?
    \d{4}
    """,re.VERBOSE)
    emailRegex = re.compile('\w+@\w+\.\w+')
    phones = phoneNumRegex.findall(info)
    emails = emailRegex.findall(info)
    print(f"""
   Emails: {emails}

   Phone Numbers: {phones}
    """)
extract()
