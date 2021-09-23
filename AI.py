import numpy as np

arr_x = np.array([-0.2, 0.5])


def bias(a):
    if a > 0:
        y = 1
    else:
        y = 0
    return y


arr_x_1 = np.array([])
for j in range(0, 11):
    i = arr_x[0]
    j = j/10
    arr_x_1 = np.append(arr_x_1, i*j)

arr_x_2 = np.array([])
for j in range(0, 11):
    i = arr_x[1]
    j = j/10
    arr_x_2 = np.append(arr_x_2, i*j)

arr_x_1 = arr_x_1.reshape(11, 1)


arr_x_2 = arr_x_2.reshape(11, 1)


for i in arr_x_1:
    for j in arr_x_2:
        temp = str(i) + " + " + str(j)
        print(temp, i*j, sep=" = ")


# y = bias(a)
# print(y)
