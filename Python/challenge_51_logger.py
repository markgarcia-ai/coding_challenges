"""
Challenge 51: Logger (logging module)

Problem Statement:
Use the `logging` module to record messages at different severity levels (DEBUG, INFO, WARNING, ERROR) from a simple application.

Requirements:
- Import the `logging` module.
- Configure the basic logging settings to:
  - Display messages of level `DEBUG` and higher.
  - Use a format that includes the log level, timestamp, and message.
- Create a function `run_process()` that simulates some work.
- Inside `run_process()`, log messages for different events:
  - A `DEBUG` message for a detailed internal state (e.g., "Starting data validation...").
  - An `INFO` message for a major milestone (e.g., "Process started successfully.").
  - A `WARNING` message for a potential issue (e.g., "Configuration file not found, using defaults.").
  - An `ERROR` message for a failure that prevents a specific task from completing (e.g., "Failed to connect to the database.").
- Call the function to see the log output.

Solution:
"""
import logging
import time

def run_process():
    """Simulates a process that logs messages at various levels."""
    
    logging.info("Process started successfully.")
    
    logging.debug("Starting data validation...")
    time.sleep(0.1) # Simulate work
    logging.debug("Data validation complete.")
    
    logging.warning("Configuration file not found, using default settings.")
    
    logging.error("Failed to connect to the database. Cannot load user profiles.")
    
    logging.info("Process finished with some errors.")


# Example usage:
if __name__ == "__main__":
    # Basic configuration for the logger
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=log_format)
    
    run_process()

"""
Expected Output (timestamps will vary):

2023-10-27 10:30:00,123 - INFO - Process started successfully.
2023-10-27 10:30:00,123 - DEBUG - Starting data validation...
2023-10-27 10:30:00,224 - DEBUG - Data validation complete.
2023-10-27 10:30:00,224 - WARNING - Configuration file not found, using default settings.
2023-10-27 10:30:00,224 - ERROR - Failed to connect to the database. Cannot load user profiles.
2023-10-27 10:30:00,224 - INFO - Process finished with some errors.
""" 