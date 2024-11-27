import sys

class CustomException(Exception):
    """A custom exception class for detailed error tracking."""

    def __init__(self, error_message, error_details: sys):
        """
        Initialize the CustomException with error message and details.

        Args:
            error_message (str): The error message to display.
            error_details (sys): The system-specific error details (e.g., traceback).
        """
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()  # Get traceback details
        self.line_number = exc_tb.tb_lineno  # Line number where error occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename  # File where error occurred
        super().__init__(self.error_message)

    def __str__(self):
        """
        Customize the string representation of the exception.

        Returns:
            str: Formatted error message with file name, line number, and error message.
        """
        return (
            f"Error occurred in Python script: [{self.file_name}] "
            f"at line number: [{self.line_number}] "
            f"with error message: [{self.error_message}]"
        )
if __name__ == "__main__":
    try:
        a = 1 / 0  # Example: Division by zero error
    except Exception as e:
        # Raise the custom exception with the original exception and sys details
        raise CustomException("An error occurred", sys) from e