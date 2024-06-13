# module test_analysis.py

# written by: Syed Mazhar, Minh, Paul, 12.06.2024
# changed by: Syed Mazhar, Minh, Paul, 13.06.2024



import logging
import re
from io import StringIO

# Prepare the log capture to test the code
log_stream = StringIO()
logging.basicConfig(stream=log_stream, level=logging.ERROR, format='%(message)s')

def detect_errors(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    previous_last_word = None
    empty_line_counter = 0
    previous_line_num = None
    
    for line_num, line in enumerate(lines):
        line = line.strip()
        
        # Detect word duplication within the line
        words = re.split('\W+', line)
        for i in range(len(words) - 1):
            if words[i] == words[i + 1] and words[i] != '':
                logging.error(f'line {line_num + 1} word #{i + 1}: {words[i]}')
        
        # Detect punctuation errors
        words_with_punctuation = line.split()
        for i in range(len(words_with_punctuation) - 1):
            if words_with_punctuation[i].endswith(('.', '!', '?')) and words_with_punctuation[i + 1][0].islower():
                logging.error(f'line {line_num + 1} punctuation error: {words_with_punctuation[i + 1]}')
        
        # Detect word duplication across lines considering empty lines
        if previous_last_word and words and previous_last_word == words[0]:
            logging.error(f'lines {previous_line_num + 1} and {line_num + 1} word duplication: {words[0]}')
        
        # Update the previous_last_word and previous_line_num for the next iteration
        if words:
            previous_last_word = words[-1]
            previous_line_num = line_num
        else:
            previous_last_word = None

        # Detect word duplication with empty lines in between
        if line == "":
            empty_line_counter += 1
        else:
            if empty_line_counter > 0 and previous_last_word and words:
                for i in range(1, empty_line_counter + 1):
                    if line_num - i >= 0:
                        previous_line = lines[line_num - i].strip()
                        previous_words = re.split('\W+', previous_line)
                        if previous_words and previous_words[-1] == words[0]:
                            logging.error(f'lines {line_num - i + 1} and {line_num + 1} word duplication: {words[0]}')
            empty_line_counter = 0
    
    # Output the log results
    return log_stream.getvalue()

# Run the refined detect_errors function on the sample text
log_contents = detect_errors('data/faulty_text.txt')
print(log_contents)
