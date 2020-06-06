import numpy as np # linear algebra
from numpy.linalg import inv

def multi_run_wrapper_sd(args):
    return statistical_distance(*args)

def multi_run_wrapper_cd(args):
    return class_distance(*args)

def statistical_distance(X, Y, features):
    #Gaussian distribution
    
    class_0 = X[Y == 0, :]
    class_0 = class_0[:, features]
    
    class_1 = X[Y == 1, :]
    class_1 = class_1[:, features]

    mean_class_0 = np.mean(class_0, axis=0)
    mean_class_1 = np.mean(class_1, axis=0)

    if len(features) == 1:
        inverse_var_class_0 = np.array([1]).reshape(1,1)
        inverse_var_class_1 = np.array([1]).reshape(1,1)
    else:
        try:
            inverse_var_class_0 = inv(np.cov(class_0.T))
            inverse_var_class_1 = inv(np.cov(class_1.T))
        except ValueError:
            print('Singular Matrix with features:', features)
            return 0


    mean_difference = (mean_class_0 - mean_class_1).reshape(len(features),1)
    inverse_var_sum = inverse_var_class_0 + inverse_var_class_1

    aux = np.dot(np.dot(mean_difference.T, inverse_var_sum), mean_difference)
    aux *= 0.5

    trace = np.trace(2.0*(np.dot(inverse_var_class_0, inverse_var_class_1)) - 2.0*np.identity(len(features)))

    J = aux + trace
    return J

def class_distance(X, Y, features):
    class_0 = X[Y == 0, :]
    class_0 = class_0[:, features]

    class_1 = X[Y == 1, :]
    class_1 = class_1[:, features]

    mean_class_0 = np.mean(class_0, axis=0)
    mean_class_1 = np.mean(class_1, axis=0)

    covar_class_0 = np.cov(class_0.T)
    covar_class_1 = np.cov(class_1.T)

    mean_difference = mean_class_0 - mean_class_1
    mean_difference = mean_difference.reshape(len(features),1)

    Sb = np.dot(mean_difference, mean_difference.T)
    Sw = (covar_class_0 + covar_class_1)

    t1 = np.trace(Sb)

    if len(features) == 1:
        t2 = np.trace(Sw.reshape(len(features),1))
    else:
        t2 = np.trace(Sw)


    J = t1 / t2
    
    return J