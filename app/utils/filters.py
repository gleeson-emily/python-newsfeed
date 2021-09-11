def format_date(date):
    return date.strftime('%m/%d/%y')

# checking to see if format_date works correctly
# from datetime import datetime
# print(format_date(datetime.now()))

def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# checking to see if format_url works correctly
# print(format_url('http://google.com/test'))
# print(format_url('https://www.google.com?q=test'))

def format_plural(amount, word):
    if amount != 1:
        return word + 's'

    return word

# checking to see if format_plural works correctly
# print(format_plural(2, 'cat'))
# print(format_plural(1, 'dog'))