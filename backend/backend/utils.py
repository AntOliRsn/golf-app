import os

def relative_path(script_reference_path, rel_path):
    """
    Method to build a path given a reference and a relative one
    __file__ should be passed as script_reference_path

    :param script_reference_path: str
    :param rel_path: str
    :return: str
    """

    script_path = os.path.abspath(script_reference_path)
    script_dir = os.path.split(script_path)[0]
    return os.path.join(script_dir, rel_path)