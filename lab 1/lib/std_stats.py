import math


class StdStats:
    def __init__(self):
        pass

    @staticmethod
    def max(a):
        StdStats.validate_not_null(a)
        max_val = -float('inf')
        for val in a:
            if math.isnan(val):
                return float('nan')
            if val > max_val:
                max_val = val
        return max_val

    @staticmethod
    def max_subarray(a, lo, hi):
        StdStats.validate_not_null(a)
        StdStats.validate_subarray_indices(lo, hi, len(a))
        max_val = -float('inf')
        for i in range(lo, hi):
            if math.isnan(a[i]):
                return float('nan')
            if a[i] > max_val:
                max_val = a[i]
        return max_val

    @staticmethod
    def max_int(a):
        StdStats.validate_not_null(a)
        max_val = -float('inf')
        for val in a:
            if val > max_val:
                max_val = val
        return max_val

    @staticmethod
    def min(a):
        StdStats.validate_not_null(a)
        min_val = float('inf')
        for val in a:
            if math.isnan(val):
                return float('nan')
            if val < min_val:
                min_val = val
        return min_val

    @staticmethod
    def min_subarray(a, lo, hi):
        StdStats.validate_not_null(a)
        StdStats.validate_subarray_indices(lo, hi, len(a))
        min_val = float('inf')
        for i in range(lo, hi):
            if math.isnan(a[i]):
                return float('nan')
            if a[i] < min_val:
                min_val = a[i]
        return min_val

    @staticmethod
    def min_int(a):
        StdStats.validate_not_null(a)
        min_val = float('inf')
        for val in a:
            if val < min_val:
                min_val = val
        return min_val

    @staticmethod
    def mean(a):
        StdStats.validate_not_null(a)
        if len(a) == 0:
            return float('nan')
        return sum(a) / len(a)

    @staticmethod
    def mean_subarray(a, lo, hi):
        StdStats.validate_not_null(a)
        StdStats.validate_subarray_indices(lo, hi, len(a))
        length = hi - lo
        if length == 0:
            return float('nan')
        return sum(a[lo:hi]) / length

    @staticmethod
    def mean_int(a):
        StdStats.validate_not_null(a)
        if len(a) == 0:
            return float('nan')
        return sum(a) / len(a)

    @staticmethod
    def var(a):
        StdStats.validate_not_null(a)
        if len(a) == 0:
            return float('nan')
        avg = StdStats.mean(a)
        sum_sq_diff = sum((x - avg) ** 2 for x in a)
        return sum_sq_diff / (len(a) - 1)

    @staticmethod
    def var_subarray(a, lo, hi): 
        StdStats.validate_not_null(a)
        StdStats.validate_subarray_indices(lo, hi, len(a))
        length = hi - lo
        if length == 0:
            return float('nan')
        avg = StdStats.mean_subarray(a, lo, hi)
        sum_sq_diff = sum((a[i] - avg) ** 2 for i in range(lo, hi))
        return sum_sq_diff / (length - 1)

    @staticmethod
    def var_int(a):
        StdStats.validate_not_null(a)
        if len(a) == 0:
            return float('nan')
        avg = StdStats.mean_int(a)
        sum_sq_diff = sum((x - avg) ** 2 for x in a)
        return sum_sq_diff / (len(a) - 1)

    @staticmethod
    def varp(a):
        StdStats.validate_not_null(a)
        if len(a) == 0:
            return float('nan')
        avg = StdStats.mean(a)
        sum_sq_diff = sum((x - avg) ** 2 for x in a)
        return sum_sq_diff / len(a)

    @staticmethod
    def varp_subarray(a, lo, hi):
        StdStats.validate_not_null(a)
        StdStats.validate_subarray_indices(lo, hi, len(a))
        length = hi - lo
        if length == 0:
            return float('nan')
        avg = StdStats.mean_subarray(a, lo, hi)
        sum_sq_diff = sum((a[i] - avg) ** 2 for i in range(lo, hi))
        return sum_sq_diff / length

    @staticmethod
    def stddev(a):
        return math.sqrt(StdStats.var(a))

    @staticmethod
    def stddev_int(a):
        return math.sqrt(StdStats.var_int(a))

    @staticmethod
    def stddev_subarray(a, lo, hi):
        return math.sqrt(StdStats.var_subarray(a, lo, hi))

    @staticmethod
    def stddevp(a):
        return math.sqrt(StdStats.varp(a))

    @staticmethod
    def stddevp_subarray(a, lo, hi):
        return math.sqrt(StdStats.varp_subarray(a, lo, hi))

    @staticmethod
    def validate_not_null(x):
        if x is None:
            raise ValueError("argument is null")

    @staticmethod
    def validate_subarray_indices(lo, hi, length):
        if lo < 0 or hi > length or lo > hi:
            raise ValueError(f"subarray indices out of bounds: [{lo}, {hi})")


# Usage examples
if __name__ == "__main__":
    # Sample data
    data = [1.0, 2.0, 3.0, 4.0, 5.0]

    print("Max:", StdStats.max(data))
    print("Min:", StdStats.min(data))
    print("Mean:", StdStats.mean(data))
    print("Variance:", StdStats.var(data))
    print("Standard Deviation:", StdStats.stddev(data))
