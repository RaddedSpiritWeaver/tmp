import random


def read(path):
    with open(path) as file:
        x_list = []
        y_list = []

        train_x_list = []
        train_y_list = []
        for line in file:
            tokens = line.split(',')
            if tokens[2] == 1:  # label 1 for train data
                train_x_list.append(float(tokens[0]))
                train_y_list.append(float(tokens[1]))
            else:
                x_list.append(float(tokens[0]))
                y_list.append(float(tokens[1]))
