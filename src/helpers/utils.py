import string


def remove_RT(text: str):
    """

    Args:
        text:

    Returns:

    """
    return " ".join([_ for _ in text.split() if _ != 'RT'])


def remove_mention(text: str):
    """

    Args:
        text:

    Returns:

    """
    return " ".join([_ for _ in text.split() if not _.startswith("@")])


def remove_punctuations(text: str):
    """
    removing the punctuation from the
    Args:
        text:

    Returns:

    """
    return ''.join([_ for _ in text if _ not in string.punctuation])


def remove_amp(text: str):
    """
    removing the punctuation from the
    Args:
        text:

    Returns:

    """
    return " ".join([_ for _ in text.split() if not _.startswith("&amp;")])


def remove_quoted_printable(text):
    """
    removing the punctuation from the
    Args:
        text:

    Returns:

    """
    pass


