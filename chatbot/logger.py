import logging
import os
from datetime import datetime

# Create a log file name based on the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}_log.txt"

# Get the current working directory and create a "logs" directory
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

# Define the full file path for the log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    filename=LOG_FILEPATH,  # Define the log file path
    format=" [%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Log format
)

if __name__ == "__main__":
    logging.info("starting logging")