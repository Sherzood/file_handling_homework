def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    new_list=[]
    for i in data:
        if not i.isdigit():
            new_list.append(i)
    return new_list        
    
# Read data from file
f=open('txt_file\data04.txt')
data=f.read()
print(main(data))
