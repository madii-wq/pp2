import datetime

n, p = int(input()), int(input())
first_t = datetime.timedelta(days=n)
second_t = datetime.timedelta(days=p)

print(abs(first_t - second_t))