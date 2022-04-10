def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    sum_digits=0
    new_list=[]
    for i in data:
        if i.isdigit():
            sum_digits+=int(i)
    new_list.append(sum_digits)
    return sum_digits

# Read data from file
f=open('txt_file/data07.txt')
data=f.read()
print(main(data))