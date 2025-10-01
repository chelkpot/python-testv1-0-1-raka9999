# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())

    weight=float(input("Введите ваш вес (в кг): "))
    height=float(input("Введите ваш рост (в метрах): "))

    bmi=weight / (height**2)

    print("Ваш индекс массы тела (BMI):", round(bmi,2))

   

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()