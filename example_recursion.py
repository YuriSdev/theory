def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number // base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False


def sum_positive_numbers(n):
    if n == 1:
        return 1
    elif n > 1:
        return n + sum_positive_numbers(n - 1)
    else:
        return 0


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15


