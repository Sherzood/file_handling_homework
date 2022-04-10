def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    mx=0
    for i in data:
        if i.isdigit():
            if int(i)>mx:
                mx=int(i)
    return mx            
# Read data from file
f=open('txt_file/data08.txt')
data=f.read()
print(main(data))