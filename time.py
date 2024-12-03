def convert_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds
time_input = input("Введите время в формате часы-минуты-секунды (например, 1-11-11): ")
hours, minutes, seconds = map(int, time_input.split('-'))
total_seconds = convert_to_seconds(hours, minutes, seconds)
print(f"Общее количество секунд: {total_seconds}")
