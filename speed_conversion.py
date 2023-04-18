speed = float(input("Введите скорость: "))
unit = input("Введите единицу измерения скорости (kmh/ms): ")

if unit == "kmh":
    speed_mps = speed / 3.6
    print(f"Скорость: {speed_mps:.2f} м/с")
elif unit == "mps":
    speed_kmh = speed * 3.6
    print(f"Скорость: {speed_kmh:.2f} км/ч")
else:
    print("Неправильно указана единица измерения скорости.")
