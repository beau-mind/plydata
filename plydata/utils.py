from contextlib import contextmanager


def hasattrs(obj, names):
    """
    Return True of obj has all the names attributes
    """
    return all(hasattr(obj, attr) for attr in names)


@contextmanager
def temporary_key(d, key, value):
    """
    Context manager that removes key from dictionary on closing

    The dictionary will hold the key for the duration of
    the context.

    Parameters
    ----------
    d : dict-like
        Dictionary in which to insert a temporary key.
    key : hashable
        Location at which to insert ``value``.
    value : object
        Value to insert in ``d`` at location ``key``.
    """
    d[key] = value
    try:
        yield d
    finally:
        del d[key]
