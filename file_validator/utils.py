"""Utils for file validator."""
from itertools import groupby
from filetype import is_archive, is_audio, is_font, is_image, is_video
from termcolor import colored
from file_validator.constants import (
    ALL_SUPPORTED_LIBRARIES,
    ARCHIVE,
    AUDIO,
    FONT,
    IMAGE,
    LIBRARY_IS_NOT_SUPPORTED,
    MIMES_IS_EQUAL,
    PARAMETERS_ARE_EMPTY,
    SELECTING_ALL_SUPPORTED_LIBRARIES,
    SUPPORTED_TYPES,
    TYPE_NOT_SUPPORTED,
    VIDEO,
)
from file_validator.exceptions import (
    EmptyParametersException,
    LibraryNotSupportedException,
    MimesEqualException,
    TypeNotSupportedException,
)
def all_mimes_is_equal(acceptable_mimes: list):
    """Returns True if all the mimes are equal to each other if the length of
    mimes is one returned false."""
    pass
def is_library_supported(library: str):
    """If we do not support the library you choose, a
    LibraryNotSupporteexception error is thrown.
    supported libraries: python magic, pure magic, filetype, mimetypes
    """
    pass
def generate_information_about_file(
    status=None,
    library=None,
    file_name=None,
    file_extension=None,
    file_mime=None,
    **kwargs,
) -> dict:
    """Generates information about file validated."""
    pass
def guess_the_type(file_path: str) -> str:
    """This function is used to guess the overall type of file such image,
    audio, video, font and archive."""
    pass
def parameters_are_empty(acceptable_types: list, acceptable_mimes: list):
    """This function check whether parameters are empty or no?"""
    pass
def is_type_supported(acceptable_types: list):
    """This function check whether the type is supported by file-validator
    library, List of supported types: font, audio, video, image, archive."""
    pass
def set_the_library(libraries: list):
    """This function set the libraries."""
    pass
def set_the_acceptable_mimes(acceptable_mimes):
    """This function for set the acceptable mimes."""
    pass