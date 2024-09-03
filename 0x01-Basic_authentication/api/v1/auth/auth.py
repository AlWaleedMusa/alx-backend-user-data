#!/usr/bin/env python3

from typing import TypeVar, List
from flask import request


class Auth:
    """
    A class used to handle authentication-related tasks.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a given path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths
            that do not require authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        if not path or not excluded_paths:
            return True

        if path.endswith("/"):
            tmp_path = path
        else:
            tmp_path = f"{path}/"

        for exc in excluded_paths:
            if not exc:
                continue

            if exc.endswith("*"):
                if path.startswith(exc[:-1]):
                    return False
            elif tmp_path == exc:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.

        Args:
            request: The request object.

        Returns:
            str: The value of the Authorization header, or None if not present.
        """
        if not request:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieves the current user from the request.

        Args:
            request: The request object.

        Returns:
            TypeVar("User"): The current user, or None if not present.
        """
        return None
