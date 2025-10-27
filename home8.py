seconds = int(input())

days, rem = divmod(seconds, 24*60*60)
hours, rem = divmod(rem, 60*60)
minutes, seconds = divmod(rem, 60)

day_word = "день" if days == 1 else "дні" if 2 <= days <= 4 else "днів"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
