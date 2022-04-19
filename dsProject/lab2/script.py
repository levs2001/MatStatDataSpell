from math import exp


def df_dx1(x1, x2):
    return 2 * x1 + 2 * x1 * exp(x1 ** 2 + 2 * x2 ** 2) + 4


def df_dx2(x1, x2):
    return 4 * x2 * exp(x1 ** 2 + 2 * x2 ** 2) + 3


def ddf(x, y):
    return (exp(x ** 2 + 2 * y ** 2) * (4 * x ** 2 + 2) + 2) * (exp(x ** 2 + 2 * y ** 2) * (16 * y ** 2 + 4)) - (
                exp(x ** 2 + 2 * y ** 2) * 8 * x * y) ** 2


if __name__ == '__main__':
    x1_ans = -0.66
    x2_ans = -0.37
    print(df_dx1(x1_ans, x2_ans))
    print(df_dx2(x1_ans, x2_ans))
    print(ddf(x1_ans, x2_ans))

