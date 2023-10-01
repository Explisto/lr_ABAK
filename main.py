# формализм работы с троичными строками
# примеры
"""
δ1 = (0 1 -), δ2  = (1 - 0), δ3 = (- 1 0)
а) δ1 v δ2 = ((0 1 -),(1 - 0))
б) δ1 & δ2 = 0 - пустая строка
"""


# Подключение модулей
from Sum import Sum
from Multiplication import sub_matrix
from Negation import neg_matrix

#=====================

# логика

def CheckInputArgumentsMatrix(m, n):

    if m.isdigit() and n.isdigit():

        if (m != 0) and (n != 0) and (m != 0) and (n != 0):
            pass
        else:
            return False
    else:
        return False

    return True


def SetMatrix(m, n):

    matrix_row = []
    matrix = [[]]

    for i in range(int(m)):

        for j in range(int(n)):
            print("Введите значение элемента матрицы:", i + 1, " строка, ", j + 1, "столбец.")
            choice_element = input("Введите элемент:")

            if choice_element == "1" or choice_element == "0" or choice_element == "-":
                matrix_row.append(choice_element)

        matrix.append(matrix_row)
        matrix_row = []

    matrix.pop(0)

    return matrix


def PrintMatrix(matrix):

    for index in matrix:
        print('(' + ' '.join(index) + ')')


def InputMatrix(mark):

    list_size = []

    if mark == 1:
        print("Введите, пожалуйста, размер первой исходной матрицы в формате m x n (m - количество строк, n - количество столбцов)")
        list_size.append(input("Введите количество строк первой матрицы:"))
        list_size.append(input("Введите количество столбцов первой матрицы:"))
        print("Введите, пожалуйста, размер второй исходной матрицы в формате m x n (m - количество строк, n - количество столбцов)")
        list_size.append(input("Введите количество строк второй матрицы:"))
        list_size.append(input("Введите количество столбцов второй матрицы:"))

    if mark == 2:
        print("Введите, пожалуйста, размер матрицы в формате m x n (m - количество строк, n - количество столбцов)")
        list_size.append(input("Введите количество строк матрицы:"))
        list_size.append(input("Введите количество столбцов матрицы:"))

    # list_size.pop(0)

    return list_size

def UserMessage():

    choice_user = '0'

    print("Здравствуйте! Вас приветствует программа для работы с троичными матрицами.")
    print("Эта программа реализует операции сложения, умножения и отрицания троичных матриц.")

    while(choice_user != 'e'):

        print("Пожалуйста, выберите операцию, которую вы хотите совершить над матрицами (нажмите клавишу, соответствующую операции):")
        print("1. Сложение")
        print("2. Произведение")
        print("3. Отрицание")
        print("Вы можете завершить выполнение программы, нажав клавишу 'e'.")
        choice_user = input("Ваш выбор:")

        if (choice_user == '1'):

            print("Вы выбрали пункт: сложение троичных матриц.")

            list_size = InputMatrix(1)

            flag_matrix_1 = CheckInputArgumentsMatrix(list_size[0], list_size[1])
            flag_matrix_2 = CheckInputArgumentsMatrix(list_size[2], list_size[3])

            if flag_matrix_1 and flag_matrix_2 == 1:
                print("Начинайте ввод элементов первой матрицы:")
                matrix_1 = SetMatrix(list_size[0], list_size[1])
                print("Начинайте ввод элементов второй матрицы:")
                matrix_2 = SetMatrix(list_size[2], list_size[3])

                print("Ваши исходные матрицы:")
                PrintMatrix(matrix_1)
                print("=====================================================")
                PrintMatrix(matrix_2)
                print("=====================================================")

                matrix_ans = Sum(matrix_1, matrix_2)

                print("Ответ:")
                print("=====================================================")
                PrintMatrix(matrix_ans)
                print("=====================================================")

            else:
                print("Вы неправильно ввели размерность матриц. Попробуйте еще раз!")

        if (choice_user == '2'):

            print("Вы выбрали пункт: умножение троичных матриц.")

            list_size = InputMatrix(1)

            flag_matrix_1 = CheckInputArgumentsMatrix(list_size[0], list_size[1])
            flag_matrix_2 = CheckInputArgumentsMatrix(list_size[2], list_size[3])

            if flag_matrix_1 and flag_matrix_2 == 1:
                print("Начинайте ввод элементов первой матрицы:")
                matrix_1 = SetMatrix(list_size[0], list_size[1])
                print("Начинайте ввод элементов второй матрицы:")
                matrix_2 = SetMatrix(list_size[2], list_size[3])

                print("Ваши исходные матрицы:")
                PrintMatrix(matrix_1)
                print("=====================================================")
                PrintMatrix(matrix_2)
                print("=====================================================")

                matrix_ans = sub_matrix(matrix_1, matrix_2)

                print("Ответ:")
                print("=====================================================")
                PrintMatrix(matrix_ans)
                print("=====================================================")

            else:
                print("Вы неправильно ввели размерность матриц. Попробуйте еще раз!")

        if (choice_user == '3'):

            print("Вы выбрали пункт: отрицание троичной матрицы.")

            list_size = InputMatrix(2)

            flag_matrix_1 = CheckInputArgumentsMatrix(list_size[0], list_size[1])

            if flag_matrix_1 == 1:
                print("Начинайте ввод элементов матрицы:")
                matrix_1 = SetMatrix(list_size[0], list_size[1])

                print("Ваша исходная матрица:")
                PrintMatrix(matrix_1)
                print("=====================================================")

                matrix_ans = neg_matrix(matrix_1)

                print("Ответ:")
                print("=====================================================")
                PrintMatrix(matrix_ans)
                print("=====================================================")

            else:
                print("Вы неправильно ввели размерность матриц. Попробуйте еще раз!")

    print("Работа программы закончена, до свидания!")


UserMessage()