#!/usr/bin/env python3
"""Module for filtering sensitive information from log messages."""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Replaces occurrences of specified fields in a log message with a redaction string.
    """
    return re.sub(
        rf"({'|'.join(fields)})=.+?{separator}", rf"\1={redaction}{separator}", message
    )
