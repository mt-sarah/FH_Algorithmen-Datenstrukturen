def transform_to_row(infile, outfile):
    with open(infile, 'r') as reader:
        contents = reader.read().split(',')

    with open(outfile, 'w') as writer:
        for name in contents:
            writer.write('{}\n'.format(name))


# transform_to_row("test", "test2")


def add_greeting(infile, outfile):
    with open(infile, 'r') as reader:
        contents = reader.readlines()

    with open(outfile, 'w') as writer:
        for name in contents:
            writer.write('Hello {}'.format(name)) 


#add_greeting('test2.txt', 'test3.txt')


def strip_greeting(infile, outfile):
    with open(infile, 'r') as reader:
        contents = reader.readlines()

    with open(outfile, 'w') as writer:
        for line in contents:
            parts = line.split(' ')
            writer.write(parts[1])


# strip_greeting('test3.txt', 'test4.txt')


def combine_files(file1, file2, outfile):
    with open(file1, 'r') as reader:
        contents1 = reader.readlines()
    
    with open(file2, 'r') as reader:
        contents2 = reader.readlines()

    if len(contents1) != len(contents2):
        raise ValueError("This function only allows files with the same amount of lines")
    
    else:
        with open(outfile, 'w') as writer:
           combined = zip(contents1, contents2)
           for pair in combined:
               writer.write('{0} {1}\n'.format(pair[0].strip(), pair[1].strip()))



# combine_files('test3.txt', 'test1.txt', 'test5.txt')