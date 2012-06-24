def regular_numbers(baseline):
    """
    Return some regular numbers higher then baseline
    it'll return several numbers, one of which will be
    the mininum.
    """
    # try an number of twos
    twos_value = 1
    while twos_value <= baseline:
        twos_value *= 2
        # try any number of threes
        threes_value = twos_value
        while threes_value <= baseline:
            threes_value *= 3
            # keep adding fives until we pass the baseline
            # a little math should make it possible to avoid this loop

            fives_value = threes_value
            while fives_value <= baseline:
                fives_value *= 5
            # at this point, we know fives_value is > baseline
            yield fives_value
        # because we've just exited the while loop
        # threes_value > baseline
        yield threes_value
    # ditto, twos_value > baseline
    yield twos_value

def next_regular(number):
    return min(regular_numbers(number))
