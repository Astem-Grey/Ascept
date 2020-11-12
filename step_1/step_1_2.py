
time = int(input('Введите количество пройденных секунд: '))

sec_gap = time % 3600
minutes = sec_gap // 60
hour = time // 3600
sec = sec_gap % 60

print(f'Пройденное время {hour}:{minutes}:{sec}')
