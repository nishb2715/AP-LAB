#Create a log file and write error messages.
def log_error(message, log_file_path):
    try:
        with open(log_file_path, 'a') as log_file:
            log_file.write(message + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the log file: {e}")
#usage:
log_file_path = "C:\\Users\\NISHTHA\\Desktop\\error_log.txt"  # Replace with your log file path
error_message = "This is a sample error message."
log_error(error_message, log_file_path)
