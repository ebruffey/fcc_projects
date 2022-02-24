import numpy as np

def calculate(nums):

    nums = np.array(nums)
    
    final_dict = dict()
   
    comb_mean = []
    comb_var = []
    comb_std = []
    comb_max = []
    comb_min = []
    comb_sum = []

    try:
        num_matrix = nums.reshape((3,3))
        #print(num_matrix)

    except ValueError:
        raise ValueError('List must contain nine numbers.')

    flat_mean = num_matrix.mean(dtype=np.float64).tolist()
    mean1 = num_matrix.mean(0, dtype=np.float64).tolist()
    mean2 = num_matrix.mean(1, dtype=np.float64).tolist()
    comb_mean.append(mean1)
    comb_mean.append(mean2)
    comb_mean.append(flat_mean)

    #print(comb_mean)
    flat_var = num_matrix.var(dtype=np.float64).tolist()
    var1 = num_matrix.var(0, dtype=np.float64).tolist()
    var2 = num_matrix.var(1, dtype=np.float64).tolist()
    comb_var.append(var1)
    comb_var.append(var2)
    comb_var.append(flat_var)

    flat_std = num_matrix.std(dtype=np.float64).tolist()
    std1 = num_matrix.std(0, dtype=np.float64).tolist()
    std2 = num_matrix.std(1, dtype=np.float64).tolist()
    comb_std.append(std1)
    comb_std.append(std2)
    comb_std.append(flat_std)

    flat_max = num_matrix.max().tolist()
    max1 = num_matrix.max(0).tolist()
    max2 = num_matrix.max(1).tolist()
    comb_max.append(max1)
    comb_max.append(max2)
    comb_max.append(flat_max)

    flat_min = num_matrix.min().tolist()
    min1 = num_matrix.min(0).tolist()
    min2 = num_matrix.min(1).tolist()
    comb_min.append(min1)
    comb_min.append(min2)
    comb_min.append(flat_min)

    flat_sum = num_matrix.sum().tolist()
    sum1 = num_matrix.sum(0).tolist()
    sum2 = num_matrix.sum(1).tolist()
    comb_sum.append(sum1)
    comb_sum.append(sum2)
    comb_sum.append(flat_sum)

    # print(final_dict)
    # mean1 = list(mean1)
    # mean1 = mean1.tolist()

    # print(mean1)
    # print(type(mean1))
    # final_dict = {'mean': list(num_matrix.mean(1))}

    # print(final_dict)

    final_dict = {'mean': comb_mean,
                  'variance': comb_var,
                  'standard deviation': comb_std,
                  'max': comb_max,
                  'min': comb_min,
                  'sum': comb_sum}

    return final_dict