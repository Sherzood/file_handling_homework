def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    mx_length=0
    data1=data.split('\n')
    for i in data1:
        if len(i)>mx_length:
            mx_length=len(i)
    return mx_length        
# Read data from file
f=open('txt_file\data10.txt')
data=f.read()
print(main(data))