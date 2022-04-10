def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    count_d=0
    count_s=0
    
    for i in data:
        if i.isdigit():
            count_d+=1
        else:
            count_s+=1   
    return [count_d,count_s]
# Read data from file
f=open('txt_file\data05.txt')
data=f.read()
print(main(data))