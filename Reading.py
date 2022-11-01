def read_all():
        
    file = open('what is halo.txt', 'r')
        
    all_lines = file.read()
        
    print(all_lines)
        
    file.close()
    
def main():
    read_all()
    
main()