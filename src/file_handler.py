import random


def read(path):
    with open(path) as file:
        data = []
        labels = []
        for line in file:
            tokens = line.split(',')
            data.append([float(tokens[0]), float(tokens[1])])
            labels.append(int(tokens[2]))
        random.shuffle(labels)  # assign shuffled labels to the data
        return data, labels

