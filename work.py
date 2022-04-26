import time


def transformator_2ES11():
    """ скрипт для расчета коэффициента трансформации по диапазону напряжений КС"""
    U_1 = [21000, 22000, 25000, 27000, 29000, 30000]
    k_transform = 11
    u_2 = []
    for item in U_1:
        u_2.append(int(item / k_transform))
    print(U_1)
    print(u_2)
    U_pk = []
    for item in u_2:
        temp = item * 1.42
        U_pk.append(int(temp))

    print(U_pk)
    power = 1300000  # total power
    for item in u_2:
        print(power / item)


def traction_motor_length_cable():
    v_impuls = [50, 100, 150, 200, 250, 300]  # скорость распространения импульса (м/мкс)
    impuls_time = [0.05, 0.2, 0.3, 0.5, 0.75, 1]  # типичное время нарастания импульса (мкс)
    length_critical = []  # критическая длина кабеля (в метрах)
    diapazone = len(v_impuls)
    for i in range(0, diapazone):
        length_critical.append(1 / (2 * v_impuls[i] * impuls_time[i]))

    return length_critical


class RC_link_2ES6:
    """ Электрические параметры представлены в системе СИ """
    U_ks = 3800  # вольт
    Q_rr = 2500 / 1000000  # заряд обратного восстановления, Кл
    I_rrm = 50 / 1000  # обратный ток, А
    R_dempf = 10  # Ом
    C_dempf = 1 / 1000000  # емкость демпферной цепи, F
    n = 3  # количество диодов

    def power_of_shunt_resistor(self):
        R = self.n * self.U_ks
        pass


def my_decorator(func):
    def wrapper(arg_1, arg_2):
        print(f'Something here before func')
        func(arg_1, arg_2)
        print(f'Something here after func')

    return wrapper


def time_decorator(func):
    def wrapper(*args, **kwargs):
        t_1 = time.process_time()
        res = func(*args, **kwargs)
        t_2 = time.process_time()
        print(t_2 - t_1)
        return res
    return wrapper
