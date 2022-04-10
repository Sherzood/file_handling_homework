def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    new_list=[]
    data1=data.split("\n")
    for i in data1:
        new_list.append(len(i))   
    return new_list
    
# Read data from file
f=open('txt_file\data06.txt')
data=f.read()
print(main(data))