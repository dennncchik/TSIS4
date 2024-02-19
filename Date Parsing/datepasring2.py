from datetime import datetime, timedelta 
today = datetime.now()
t = timedelta(days=1)
yesterday = today - t
tomorrow = today + t
print(yesterday)
print(today)
print(tomorrow)
