#!/usr/bin/env python3
"""Basic Auth class"""

from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user credentials from the decoded Base64 authorization header.

        Args:
            decoded_base64_authorization_header (str):
            The decoded Base64 string.

        Returns:
            tuple: A tuple containing the user email and
            the user password, or (None, None) if the input is invalid.
        """

        if not decoded_base64_authorization_header:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        try:
            email, password = decoded_base64_authorization_header.split(':', 1)
        except ValueError:
            return None, None

        email, password = decoded_base64_authorization_header.split(":")
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on
        the provided email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The User instance if the
            credentials are valid, otherwise None.
        """

        if not user_email or not isinstance(user_email, str):
            return None

        if not user_pwd or not isinstance(user_pwd, str):
            return None

        try:
            user = User.search({'email': user_email})
        except Exception:
            return None

        if not user or len(user) == 0:
            return None

        user = user[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request.

        Args:
            request: The HTTP request containing
            the Authorization header.

        Returns:
            User: The User instance if authentication
            is successful, otherwise None.
        """
        header = self.authorization_header(request)

        if not header:
            return None

        encode = self.extract_base64_authorization_header(header)

        if not encode:
            return None

        decode = self.decode_base64_authorization_header(encode)

        if not decode:
            return None

        email, password = self.extract_user_credentials(decode)

        if not email or not password:
            return None

        user = self.user_object_from_credentials(email, password)

        return user
