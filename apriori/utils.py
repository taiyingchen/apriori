def read_input(filename):
    with open(filename, 'r') as file:
        min_support = int(file.readline())
        TDB = []
        for tran in file:
            TDB.append(tran.strip().split())
    return TDB, min_support


def print_output(itemsets):
    itemset_list = [(support, sorted(list(itemset))) for itemset, support in itemsets.items()]
    itemset_list = sorted(itemset_list, key=lambda x: (-x[0], x[1]))
    for support, itemset in itemset_list:
        print(f'{support}: {" ".join(itemset)}')
