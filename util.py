import copy
import numpy
import scipy
import sympy

def lagrange_interpolation(x_value: list, y_value: list) -> sympy.core.add.Add:
    """拉格朗日插值
    Args:
        :param - x_value：x值
        :param - y_value：y值
    Returns:
        sympy.core.add.Add：符号多项式
    """
    x = sympy.symbols("x")
    x1 = copy.deepcopy(x_value)
    y1 = copy.deepcopy(y_value)

    l = 0
    for i in range(len(x1)):
        t1 = 1
        t2 = 1
        for j in range(len(x1)):
            if j == i:
                continue
            t1 = t1 * (x1[i] - x1[j])
            t2 = t2 * (x - x1[j])
        l = l + t2 / t1 * y1[i]
    return sympy.expand(l)


def get_diff_quotient(n: int, x_list: list, y_list: list) -> numpy.ndarray:
    """计算差商
    Args:
        :param - n：需要的最高差商的阶数
        :param - x_list：x值
        :param - y_list：y值
    Return:
        numpy.ndarray：包含各阶差商的矩阵
    """
    x5 = copy.deepcopy(x_list)
    y5 = copy.deepcopy(y_list)

    diff = numpy.zeros((len(x_list), len(x_list)), dtype=float)
    diff[0] = y5
    diff = diff.T
    for i in range(1, n+1):
        for j in range(i, len(x5)):
            diff[j][i] = (diff[j][i-1] - diff[j-1][i-1]) / (x5[j] - x5[j-i])
    return diff


def three_interpolation():
    pass
