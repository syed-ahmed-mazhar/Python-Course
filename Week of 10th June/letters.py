# letters.py

# Written by: Syed Mazhar, Paul, Minh, 13.06.24
# Changed by: Syed Mazhar, Paul, Minh, 13.06.24

# Wikipedia statistics
wikipedia_stats_english = {'e': 0.1270, 't': 0.09056, 'a': 0.08167, 'o': 0.07507, 'l': 0.06966, 'n': 0.06749}
wikipedia_stats_german = {'e': 0.1639, 'n': 0.0978, 's': 0.0727, 'r': 0.0700, 'i': 0.0655, 'a': 0.0651}
wikipedia_stats_italian = {'e': 0.1179, 'a': 0.1174, 'i': 0.1128, 'o': 0.0983, 'n': 0.0688, 'l': 0.0651}

def read_file_to_letters(filename):
    # Initialize a dictionary to count the letters
    letter_counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    total_letters = 0
    
    # Open and read the file
    with open(filename, 'r') as f:
        content = f.read()
        
    # Count the letters
    for char in content:
        if char.isalpha():
            char = char.lower()
            letter_counts[char] += 1
            total_letters += 1
            
    # Convert counts to frequencies
    letter_frequencies = {letter: count / total_letters for letter, count in letter_counts.items() if total_letters > 0}
    
    return letter_frequencies

# Test the function
if __name__ == "__main__":
    filename = 'test01.txt'
    frequencies = read_file_to_letters(filename)
    print(frequencies)
