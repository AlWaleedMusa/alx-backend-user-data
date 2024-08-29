#!/usr/bin/env python3
"""Module for filtering sensitive information from log messages."""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Replaces occurrences of specified fields in a log message with a redaction string.

    Args:
        fields (list of str): List of field names to be redacted.
        redaction (str): The string to replace the field values with.
        message (str): The log message containing the fields to be redacted.
        separator (str): The character that separates the field names and their values in the message.

    Returns:
        str: The log message with the specified fields redacted.
    """
    return re.sub(
        rf"({'|'.join(fields)})=.+?{separator}", rf"\1={redaction}{separator}", message
    )
