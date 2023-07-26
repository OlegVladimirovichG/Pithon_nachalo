import csv
import pickle


def csv_to_pickle_string(path):
    with open(path, "r") as c:
        csv_string = ''
        for line in c:
            csv_string += line
        pkl = pickle.dumps(csv_string)
        return  pkl

print(csv_to_pickle_string('../out/hw_task_1.csv'))