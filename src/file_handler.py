import random


x_list = []
y_list = []
train_x_list = []
train_y_list = []


def read(path):
    with open(path) as file:
        data = []
        labels = []
        for line in file:
            tokens = line.split(',')
            data.append([float(tokens[0]), float(tokens[1])])
            labels.append(int(tokens[2]))
        shuffle_tmp = list(zip(data, labels))
        random.shuffle(shuffle_tmp)
        data, labels = zip(*shuffle_tmp)
        return data, labels
