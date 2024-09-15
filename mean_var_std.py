import numpy as np

def calculate(list):
    arr = np.array(list).reshape(3, 3)

    calculations = dict()
    calculations['mean'] = mean_calculations(arr)
    calculations['variance'] = variance_calculations(arr)
    calculations['standard deviation'] = 
    calculations['max'] = 
    calculations['min'] = 
    calculations['sum'] = 

    return calculations


def mean_calculations(arr):
    axis1 = np.mean(arr, axis=0) # columns (i.e. returns [mean(all_rows[0]), mean(all_rows[1]), mean(all_rows[2]))
    axis2 = np.mean(arr, axis=1) # rows (i.e. returns [mean(all_columns[0]), mean(all_columns[1]), mean(all_columns[2])])
    flattened =  np.mean(arr) # arr.flatten() or arr.reshape(-1) also works
    return [axis1, axis2, flattened]


def variance_calculations(arr):
    axis1 = np.var(arr, axis=0)
    axis2 = np.var(arr, axis=1)
    flattened = np.var(arr)
    return [axis1, axis2, flattened]


def std_deviation_calculations(arr):
    axis1 = 
    axis2 = 
    flattened = 
    return [axis1, axis2, flattened]
