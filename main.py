from sys import argv
import asian_call_option_2
import american_put_option

if __name__ == '__main__':

    filename = argv[2]              #store filepath
    file = open(filename, 'r')
    text = file.read()              #read file
    all_lines = text.split('\n')    #split file to get all new lines
    linelist = []                   #will data for all lines

    for nextline in all_lines:

        data = nextline.strip('\r').split('\t')
        if(len(data)==6):           #check if 6 parameters
            linelist.append(data)

    if(argv[1].lower() == "asian"):
        print("Asian Call Option:\n")
        asian_call_option_2.find_price(linelist)
    elif(argv[1].lower() =="american"):
        print("American Put Option:\n")
        american_put_option.find_price(linelist)
    elif(argv[1].lower() == "both"):
        print("American Put Option:\n")
        american_put_option.find_price(linelist)
        print('\n')
        print("Asian Call Option:\n")
        asian_call_option_2.find_price(linelist)
