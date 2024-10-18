import sys


def error_message_detail(error, error_detail: sys) -> str:
    """
    Returns a formatted error message with details about the error.

    Args:
        error: The exception instance that was raised.
        error_detail (sys): The sys module to get traceback details.

    Returns:
        str: A string with the filename, line number, and error message where the exception occurred.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        "Error occurred in Python script name [{0}] at line number [{1}] with error message [{2}]"
        .format(file_name, exc_tb.tb_lineno, str(error))
    )
    return error_message


class CustomException(Exception):
    """
    Custom exception class for handling exceptions with detailed error information.

    Attributes:
        error_message (str): A detailed error message with the filename, line number, and error message.
    """

    def __init__(self, error_message: str, error_detail: sys):
        """
        Initializes the CustomException class with an error message and detailed traceback info.

        Args:
            error_message (str): The custom error message.
            error_detail (sys): The sys module used to capture the traceback details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self) -> str:
        """
        Returns the string representation of the error message.

        Returns:
            str: The detailed error message.
        """
        return self.error_message
