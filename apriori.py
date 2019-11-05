from sys import stdin

def read_input():
    min_support = int(input())
    TDB = []
    for tran in stdin:
        TDB.append(tran.strip().split())
    return TDB, min_support


def main():
    TDB, min_support = read_input()
    
    
if __name__ == '__main__':
    main()
