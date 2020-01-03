import numpy as np
import src.file_handler as file_handler
import matplotlib.pyplot as plt


W = [np.random.rand(), np.random.rand()]
b = np.random.rand()
lr = 0.01
train = 150
test = 50
n_epoch = 50


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def dy_dall(x, w, b):
    wx_plus_b = w * x + b
    return x * sigmoid(wx_plus_b) * (1 - sigmoid(wx_plus_b))


def calculate_y(W, X, b):
    w2 = np.array(W)
    x2 = np.array(X)
    w2.reshape([2, 1])
    np.matmul(x2, w2) + b
    return np.matmul(X, W) + b


def calculate_cost(y, y_prim):
    return 1/2*((y - y_prim)**2)


def train_and_test_model(n_epoch):
    for i in range(n_epoch):
        grad = np.zeros([len(W)])
        for r in range(len(W)):
            for j in range(train):
                y = calculate_y(W, data[j], b)
                cost = calculate_cost(labels[j], y)
                dcost_dw = (y - labels[j]) * dy_dall(W[r], data[j][r], b)
                grad[r] += dcost_dw
        for r in range(len(W)):
            W[r] = W[r] - lr*grad[r]
    print("model trained")
    results = []
    for i in range(train, train + test):
        y = calculate_y(W, data[i], b)
        print(y)
        out_label = -1
        if y > 0.5:
            out_label = 1
        else:
            out_label = 0
        results.append((data[i], out_label))
    return results


if __name__ == '__main__':
    data, labels = file_handler.read('./resources/data.csv')
    network_calculated = train_and_test_model(n_epoch)
    x_list_1 = []
    y_list_1 = []

    x_list_0 = []
    y_list_0 = []
    print(network_calculated)
    for data in network_calculated:
        if data[1] == 0:
            x_list_0.append(data[0][0])
            y_list_0.append(data[0][1])
        if data[1] == 1:
            x_list_1.append(data[0][0])
            y_list_1.append(data[0][1])
    plt.scatter(x_list_0, y_list_0, c="red", label="type0")
    plt.scatter(x_list_1, y_list_1, c="blue", label="type1")

    plt.show()
