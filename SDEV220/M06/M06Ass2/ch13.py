from datetime import datetime
now = datetime.now()
now_str = now.strftime("%Y-%m-%d %H:%M:%S")

with open('today.txt', 'w') as file:
    file.write(now_str)
    
with open('today.txt','r') as file:
        
        today_string = file.read()

date_string = today_string.strip()

parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")       

parsed_date_only = parsed_date.date()

print (parsed_date_only) 