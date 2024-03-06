_str1 = input()

count_uppercase = sum(1 for charup in _str1 if charup.isupper())
count_lowercase = sum(1 for charlow in _str1 if charlow.islower())
print(count_uppercase, count_lowercase)
