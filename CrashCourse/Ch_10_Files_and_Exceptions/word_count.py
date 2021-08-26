def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        # 'pass' tells python to do nothing in a block
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['ehmatthes-source-code/chapter_10/alice.txt',
             'ehmatthes-source-code/chapter_10/siddhartha.txt',
             'ehmatthes-source-code/chapter_10/moby_dick.txt',
             'ehmatthes-source-code/chapter_10/little_women.txt'
            ]
for filename in filenames:
    count_words(filename)
