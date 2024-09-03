#!/usr/bin/env python3
"""Basic Auth class"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentication Class """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization
        header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization
            header containing 'Basic <Base64-encoded string>'.

        Returns:
            str: The Base64-encoded part of the Authorization header.
                 Returns None if the header is invalid
                 or not properly formatted.
        """

        if not authorization_header:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64-encoded authorization header.

        Args:
            base64_authorization_header (str):
            The Base64 string to decode.

        Returns:
            str: The decoded UTF-8 string, or
            None if the input is invalid.
        """

        if not base64_authorization_header:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
