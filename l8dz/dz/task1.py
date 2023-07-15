import csv
import pickle


def pickle_to_csv(pickle_path, result_path):
    with (
        open(pickle_path, 'rb') as p,
        open(result_path, 'w', encoding='utf-8', newline='') as c
    ):
        pkl = pickle.load(p)
        headers = pkl[0].keys()
        csv_writer = csv.DictWriter(c, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(pkl)


pickle_to_csv('../out/pickles/task_4.pickle', '../out/hw_task_1.csv')