import datetime

now = datetime.datetime.today()
modified = now.replace(microsecond=0)
print(modified)