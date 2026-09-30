def same_object(var1_value, var2_value) -> bool:
    return id(var1_value) == id(var2_value)
    """
    Given two values already assigned to two separate variables
    by the caller, determine whether they point at the same
    object in memory (not just equal values).

    Return True if they store the same address, False otherwise.
    """
