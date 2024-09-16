import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape(3, 3)
    calculations = dict()

    calculations['mean'] = mean_calculations(arr)
    calculations['variance'] = variance_calculations(arr)
    calculations['standard deviation'] = std_deviation_calculations(arr)
    calculations['max'] = max_calculations(arr)
    calculations['min'] = min_calculations(arr)
    calculations['sum'] = sum_calculations(arr)

    print(calculations)
    
    return calculations


def mean_calculations(arr):
    axis1 = np.mean(arr, axis=0) # columns (i.e. returns [mean(all_rows[0]), mean(all_rows[1]), mean(all_rows[2]))
    axis2 = np.mean(arr, axis=1) # rows (i.e. returns [mean(all_columns[0]), mean(all_columns[1]), mean(all_columns[2])])
    flattened =  np.mean(arr) # arr.flatten() or arr.reshape(-1) also works
    return [nparr.tolist() for nparr in [axis1, axis2, flattened]]


def variance_calculations(arr):
    axis1 = np.var(arr, axis=0)
    axis2 = np.var(arr, axis=1)
    flattened = np.var(arr)
    return [nparr.tolist() for nparr in [axis1, axis2, flattened]]


def std_deviation_calculations(arr):
    axis1 = np.std(arr, axis=0)
    axis2 = np.std(arr, axis=1)
    flattened = np.std(arr)
    return [nparr.tolist() for nparr in [axis1, axis2, flattened]]


def max_calculations(arr):
    axis1 = np.max(arr, axis=0)
    axis2 = np.max(arr, axis=1)
    flattened = np.max(arr)
    return [nparr.tolist() for nparr in [axis1, axis2, flattened]]


def min_calculations(arr):
    axis1 = np.min(arr, axis=0)
    axis2 = np.min(arr, axis=1)
    flattened = np.min(arr)
    return [nparr.tolist() for nparr in [axis1, axis2, flattened]]


def sum_calculations(arr):
    axis1 = np.sum(arr, axis=0)
    axis2 = np.sum(arr, axis=1)
    flattened = np.sum(arr)
    return [nparr.tolist() for nparr in [axis1, axis2, flattened]]
