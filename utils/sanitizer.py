"""
A utility module that sanitizes the text
main use: sanitize the title of the songs for comparison
"""


def sanitizer(text):
    """The main function that sanitizes the text(title)"""
    title = text.title().strip()
    if title[:4] == 'The ':
        title = title[4:]
    if title[:2] == 'A ':
        title = title[2:]
    if title[:3] == 'An ':
        title = title[:3]
    title = title.replace(' (Title Track)', '')
    title = title.replace(' - Title Track', '')
    title = title.replace(' Title Track', '')
    title = title.replace(' Song', '')
    for word in ['Female Version', 'Male Version', 'Film Version']:
        title = title.replace(f' ({word})', f' - {word}')
        if f' - {word}' in title:
            pass
        elif f' {word}' in title:
            title = title.replace(f' {word}', f' - {word}')
    return title.strip()
