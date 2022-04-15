"""Functions to support the cleaning and
translation process
"""
#function to save text in a file
def save_text(text, filename):
    """Save text in a file.
    """
    with open(filename, 'w') as file:
        file.write(text)

# read file
def read_save(raw_text, clean_function,clean_text):
    with open(raw_text, 'r') as f:
        text = f.read()
        #call function
        text = clean_function(text)
        #save result
        save_text(text, clean_text)