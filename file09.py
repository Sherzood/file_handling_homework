def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    mn=0
    for i in data:
        if i.isdigit():
            if int(i)<mn:
                mn=int(i)
    return mn            

# Read data from file
f=open('txt_file/data09.txt')
data=f.read()
print(main(data))