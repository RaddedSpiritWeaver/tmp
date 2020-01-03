import random
import matplotlib.pyplot as plt


def read(path):
    with open(path) as file:
        data = []
        labels = []
        for line in file:
            tokens = line.split(',')
            data.append([float(tokens[0]), float(tokens[1])])
            labels.append(int(tokens[2]))

        x_list_1 = []
        y_list_1 = []

        x_list_0 = []
        y_list_0 = []

        for point in data[0:100]:
            x_list_0.append(point[0])
            y_list_0.append(point[1])

        for point in data[100:200]:
            x_list_1.append(point[0])
            y_list_1.append(point[1])

        plt.scatter(x_list_0, y_list_0, c="red", label="type0")
        plt.scatter(x_list_1, y_list_1, c="blue", label="type1")

        plt.show()

        shuffle_tmp = list(zip(data, labels))
        random.shuffle(shuffle_tmp)  # assign shuffled labels to the data
        data, labels = zip(*shuffle_tmp)
        return data, labels