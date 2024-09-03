#!/usr/bin/env python3
"""Basic Auth class"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Authentication Class """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header containing 'Basic <Base64-encoded string>'.

        Returns:
            str: The Base64-encoded part of the Authorization header.
                 Returns None if the header is invalid or not properly formatted.
        """

        if not authorization_header:
            return None
        
        if not isinstance(authorization_header, str):
            return None
        
        if not authorization_header.startswith("Basic "):
            return None
        
        return authorization_header[6:]
