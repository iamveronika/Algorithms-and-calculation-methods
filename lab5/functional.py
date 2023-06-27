# Варіант №8
# Метод Гауса з одиничними коефіцієнтами


def single_gauss(a):
    n = len(a)
    result_x = []
    for i in range(n):

        tmp_a = a[i][i]
        for k in range(n+1):
            a[i][k] /= tmp_a

        for j in range(n):

            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    for i in range(n):
        result_x.append(a[i][n])

    return result_x


matrix_a = [[1.84, 2.25, 2.58, -6.09],
            [2.32, 2.00, 2.82, -6.96],
            [1.83, 2.06, 2.24, -5.52]]
