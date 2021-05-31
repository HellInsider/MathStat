from Reader import reader, make_arrays
from visualization import plot_graphics
from scr.algorithms import correlation_function, normalization

if __name__ == '__main__':
    data = reader("../data/21022518.txt")
    array1, array2, array3, array4, array5, array6, array7, array8, array9, array10, array11, array12 = make_arrays(data)
    plot_graphics(array9, array12, 'plasma_pos', 't, мс', 'plasma_pos')
    plot_graphics(array9, array8, 'neutron_glob', 't, мс', 'neutron_glob')
    plot_graphics(array9, array10, 'neutron_glob', 't, мс', 'neutron_glob')
    tau, correlation_function = correlation_function(array8, array12)
    plot_graphics(tau, correlation_function, 'corr_func', 'tau', 'correlation_function')
    correlation_function = normalization(correlation_function)
    plot_graphics(tau, correlation_function, 'norm_corr_func', 'tau', 'n_corr')

    tau, correlation_function = correlation_function(array10, array12)
    plot_graphics(tau, correlation_function, 'corr_func', 'tau', 'correlation_function')
    correlation_function = normalization(correlation_function)
    plot_graphics(tau, correlation_function, 'norm_corr_func', 'tau', 'n_corr')
    tau, correlation_function = correlation_function(array8, array10)


