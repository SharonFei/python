fpath = 'C:\AppData'
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath,'rb') as f:
        block = f.read(BLOCK_SIZE)
        if block:
            yield block
        else:
            return 
