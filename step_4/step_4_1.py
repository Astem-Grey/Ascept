from sys import argv

step_4_1, hour, rate, prem, four_param = argv


def zp(hour, rate, prem):
    hour = int(hour)
    rate = int(rate)
    prem = int(prem)
    all_zp = (hour * rate) + prem
    return all_zp


print(zp(hour, rate, prem))

