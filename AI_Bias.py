import numpy as np


def bias(result):  # slenkstine aktyvacijos funkcija
    if result >= 0:
        return 1
    if result < 0:
        return 0


k = -0.2  # slenkstis

w = np.linspace(-5, 5, 101)

results_w_1 = np.array([])
results_w_2 = np.array([])
for i in w:
    for j in w:
        y = (-0.2*i) + (0.5*j) + k
        result = bias(y)
        if result < 0:
            results_w_1 = np.append(results_w_1, [i, j])

n = results_w_1.size

n = int(n/2)
print("Pirma eilute", n, sep=' = ')
results_w_1 = results_w_1.reshape(n, 2)
# print(results_w_1)

results_w_2 = np.array([])
for i in w:
    for j in w:
        y = (0.2 * i) + (-0.5*j) + k
        result = bias(y)
        if result < 0:
            results_w_2 = np.append(results_w_2, [i, j])

n = results_w_2.size
n = int(n/2)
print("Antra eilute", n, sep="= ")
results_w_2 = results_w_2.reshape(n, 2)
# print(results_w_2)


results_w = np.array([])
for i in results_w_1:
    for j in results_w_2:
        if i[0] == j[0]:
            if i[1] == j[1]:
                results_w = np.append(results_w, [i, j])

n = results_w.size
n = int(n/2)
results_w_one = results_w.reshape(n, 2)

print(results_w_one)
###############################################################


results_w_1 = np.array([])
results_w_2 = np.array([])
for i in w:
    for j in w:
        y = (0.8 * i) + (-0.8*j) + k
        result = bias(y)
        if result >= 0:
            results_w_1 = np.append(results_w_1, [i, j])

n = results_w_1.size

n = int(n/2)
print("Trecia eilute", n, sep="= ")
results_w_1 = results_w_1.reshape(n, 2)
# print(results_w_1)

results_w_2 = np.array([])
for i in w:
    for j in w:
        y = (0.8 * i) + (0.8*j) + k
        result = bias(y)
        if result >= 0:
            results_w_2 = np.append(results_w_2, [i, j])

n = results_w_2.size
n = int(n/2)
print("Ketvirta eilute", n, sep="= ")
results_w_2 = results_w_2.reshape(n, 2)
# print(results_w_2)


results_w = np.array([])
for i in results_w_1:
    for j in results_w_2:
        if i[0] == j[0]:
            if i[1] == j[1]:
                results_w = np.append(results_w, [i, j])

n = results_w.size
n = int(n/2)

results_w_two = results_w.reshape(n, 2)

print(results_w_two)

results_weight = np.array([])
for i in results_w_one:
    for j in results_w_two:
        if i[0] == j[0]:
            if i[1] == j[1]:
                results_weight = np.append(results_weight, [i, j])

print(results_weight)

# 0.6 0.3 -0.2
