import random
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.

def mediana(list):
    clone = [i for i in list]
    clone = sorted(clone)
    length = len(clone)
    if (length%2 != 0):
        return clone[length//2]
    else:
        return (clone[length//2] + clone[length//2 + 1])/2

def moda(list):
    clone = [i for i in list]
    clone = sorted(clone)
    current = clone[0]
    repeatDict = {}
    count = 0
    for i in clone:
        if i == current:
            count += 1
        else:
            repeatDict[current] = count
            current = i
            count = 0

    result = []
    MAX = max(repeatDict.values())
    for i in repeatDict.keys():
        if repeatDict[i] == MAX:
            result.append(i)
    return result

if __name__ == "__main__":
    image = Image.open("temp.jpg")  # Открываем изображение.
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pix = image.load()  # Выгружаем значения пикселей.
    x = np.arange(26)
    y = [0 for i in range(0,26)]
    sValues = []
    count = 0
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            sValues.append(S)
            print(S)
            draw.point((i, j), (S, S, S))
            if S // 10 not in x:
                x[S // 10] = 1
            y[S//10] += 1
            count += 1
    print("bar")
    y = [i / count for i in y]
    print("after bar")
    average = sum(sValues)/count
    print("average = " + str(average))
    correctDisp = np.sqrt(sum([(i - average)**2 for i in sValues])/count - 1)
    print("correctDisp = " + str(correctDisp))

    print("mediana:")
    print(mediana(sValues))

    print("moda:")
    print(moda(sValues))

    plt.bar(x, y, width=1)
    plt.show()
    # plt.hist(x)
    # plt.show()
    image.save("ans.jpg", "JPEG")
    del draw
