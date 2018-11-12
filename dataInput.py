import csv

fileName = "./data/dataset.csv"

if __name__ == '__main__':
    with open(fileName) as f:
        reader = csv.reader(f)
        keywords = list(reader)[0]
        f.close()

    num = int(input('size of data?'))
    
    with open(fileName,'a+') as f:
        f.write('\n')
        print(keywords)
        for i in range(1,num):
            for x in keywords:
                q = input(x+': ')
                f.write(q+',')
            f.write('\n')
            print('\n')
            