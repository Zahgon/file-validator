"""In this module, there is a file validator for python, and it uses different
libraries such as filetype, python-magic, mimetypes, and files are validated
based on mimes, extensions, and magic numbers; The termcolor library is also
used to color the error messages."""

import os
import platform
from mimetypes import guess_type
from pathlib import Path

import magic
import puremagic
from dotenv import load_dotenv
from filetype import guess
from humanize import naturalsize
from puremagic import PureError
from termcolor import colored

from file_validator.constants import (
    DJANGO,
    ERROR_MESSAGE_FOR_EXTENSION_VALIDATION,
    ERROR_MESSAGE_FOR_MIME_VALIDATION,
    ERROR_MESSAGE_FOR_TYPE_VALIDATION,
    FILE_SIZE_IS_NOT_VALID,
    FILETYPE,
    MIME_NOT_VALID,
    MIMETYPES,
    OK,
    PURE_MAGIC,
    PYTHON_MAGIC,
    SIZE,
    SUPPORTED_TYPES,
    TYPE_NOT_SUPPORTED,
)
from file_validator.exceptions import (
    error_message,
    FileValidationException,
    SizeValidationException,
    TypeNotSupportedException,
)
from file_validator.utils import generate_information_about_file, guess_the_type


class FileValidator:
    """File validator."""

    # pylint: disable=too-many-instance-attributes
    # Eight are reasonable in this case.
    def __init__(
        self,
        file_path: str = None,
        libraries: list = None,
        acceptable_mimes: list = None,
        max_upload_file_size: int = None,
        **kwargs,
    ):
        self.file_mime_guessed_by_django = kwargs.get("file_mime_guessed_by_django")
        self.acceptable_extensions = kwargs.get("acceptable_extensions")
        self.result_of_validation = {}
        self.max_upload_file_size = max_upload_file_size
        self.acceptable_mimes = acceptable_mimes
        self.acceptable_types = kwargs.get("acceptable_types")
        self.file_path = file_path
        self.libraries = libraries

    def validate_extension(self):
        """This method for validating the extension of file."""
        pass

    def validate_size(self):
        """This method for validating the size of file."""
        pass

    def validate_type(self):
        """This method for validating the type of file."""
        pass

    def validate_mime(self):
        """This method for validating the mime of file."""
        pass

    def validate(self):
        """This method for validating file based on mime using all
        libraries."""
        pass

    def python_magic(self):
        """This method for validating file based on mime using python-magic
        library."""
        pass

    def pure_magic(self):
        """This method for validating file based on mime using the pure-magic
        library."""
        pass

    def mimetypes(self):
        """This method for validating file based on mime using the mimetypes
        library."""
        pass

    def filetype(self):
        """This method for validating file based on mime using the filetype
        library."""
        pass

    def django(self):
        """This method for validating file based on mime using data from
        django."""
        pass