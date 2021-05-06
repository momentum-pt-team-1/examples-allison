# Year - has many months
# Month - has many days
# Day - name, hours

days_in_may = {
    1 : 'Saturday',
    2 : 'Sunday', 
    3: 'Monday',
    4: 'Tuesday', 
    5: 'Wednesday',
    6: 'Thursday',
    7: 'Friday' 
}

class Day:
    def __init__(self, name, date, month):
        self.name = name
        self.date = date
        self.month = month

    def __str__(self):
        return f'{self.name} the {self.date} of {self.month.name}'


class Month:
    def __init__(self, name, placement):
        self.name = name
        self.placement = placement
        self.days = []

    def __str__(self):
        return f'{self.name}({self.placement})'

may = Month("May", 5)
# yesterday = Day("Wednesday", 5, may)
# today = Day("Thursday", 6, may)
# tomorrow = Day("Friday", 7, may)

for date, name in days_in_may.items():
    day = Day(name, date, may)
    may.days.append(day)

for day in may.days:
    print(day)