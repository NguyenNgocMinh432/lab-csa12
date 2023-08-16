#khai báo class
from datetime import datetime
class DateHandler :
    def __init__(self, date):
        self.date = date

    def format_date(self, date):
        return date.strftime("%d/%m/%Y")
    def get_days_between(self,date1,date2):
        between_days = (date1 - date2).days
        return between_days
    
start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)
# print(start_date)
# print(end_date)
newDate = DateHandler(start_date)
endDate = DateHandler(end_date)
print("Start:", newDate.format_date(start_date))
print("End:", endDate.format_date(end_date))
print("Days between:", newDate.get_days_between(start_date, end_date))