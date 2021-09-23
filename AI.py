import numpy as np

arr_x = np.array([0.2, -0.5])


def bias(a):
    if a > 0:
        y = 1
    else:
        y = 0
    return y


w_1 = 0
w_2 = 10

for i in range(0, 9):
    w_1 += 1
    w_2 -= 1
    a = arr_x[0] * (w_1/10) + arr_x[1] * (w_2/10)
    w = str(w_1) + ", " + str(w_2)
    print(w, str(a), sep="- > ")

# Pirma iteracija:
# 8-2
# 9-1


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

count_x = -1

# 1-9 2-8 3-7 4-6 5-5 6-4 7-3 8-2 9-1

# for i in arr_x_1:
#     count_y = 0
#     count_x += 1
#    for j in arr_x_2:
#        print("x_1", str(count_x/10), sep=" = ")
#        print("x_2", str(count_y/10), sep=" = ")
#        temp = str(i) + " + " + str(j)
#        print(temp, i+j, sep=" = ")
#        count_y += 1
# y = bias(a)
# print(y)
