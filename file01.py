def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    new_list=[]
    data1=data.split(',')
    for i in data1:
        new_list.append(int(i))
    return new_list   

# Read data from file
f=open('txt_file/data01.txt')
data=f.read()
print(main(data))