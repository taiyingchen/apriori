from sys import stdin
from collections import Counter
from itertools import combinations


def read_input():
    with open('input.txt', 'r') as stdin:
        min_support = int(stdin.readline())
        TDB = []
        for tran in stdin:
            TDB.append(set(tran.strip().split()))
    return TDB, min_support


def print_output(itemsets):
    itemset_list = [(support, ' '.join(itemset)) for itemset, support in itemsets.items()]
    itemset_list = sorted(itemset_list, key=lambda x: (-x[0], x[1]))
    for support, itemset in itemset_list:
        print(f'{support}: {itemset}')
    print()


class Apriori():
    def __init__(self, min_support):
        self.min_support = min_support
        self.freq_itemsets = {}
        self.cand_itemsets = {}
    
    def has_infreq_subset(self, cand, k):
        for subset in combinations(cand, k):
            if self.freq_itemsets[k][frozenset(subset)] < self.min_support:
                return True
        return False

    def generate_cand_itemsets(self, k):
        cand_itemsets = set()
        for i, p in enumerate(self.freq_itemsets[k-1]):
            for j, q in enumerate(self.freq_itemsets[k-1]):
                if i < j and len(p - q) == 1:
                    cand = p | q # Join
                    if self.has_infreq_subset(cand, k-1):
                        continue # Prune
                    else:
                        cand_itemsets.add(cand)
        return cand_itemsets

    def generate_freq_itemsets(self, k):
        counter = Counter()
        if k == 1:
            for tran in self.TDB:
                for item in tran:
                    counter[item] += 1
        else:
            for tran in self.TDB:
                for itemset in self.cand_itemsets[k]:
                    if itemset.issubset(tran):
                        counter[itemset] += 1
        freq_itemset = {frozenset(itemset): support for itemset, support in counter.items() if support >= self.min_support}
        freq_itemset = Counter(freq_itemset)
        return freq_itemset
        
    def compute(self, TDB):
        self.TDB = TDB
        k = 1
        self.freq_itemsets[k] = self.generate_freq_itemsets(k) # frequent 1-itemset
        while self.freq_itemsets[k]:
            self.cand_itemsets[k+1] = self.generate_cand_itemsets(k+1) # candidate generation
            self.freq_itemsets[k+1] = self.generate_freq_itemsets(k+1) # frequent itemset generation
            k += 1

    def get_all_freq_itemsets(self):
        all_freq_itemsets = Counter()
        for k in self.freq_itemsets:
            all_freq_itemsets += self.freq_itemsets[k]
        return all_freq_itemsets


def extract_closed_itemsets(itemsets):
    closed_itemsets = {}
    all_itemsets = set(itemsets.keys())
    for itemset_x in itemsets:
        is_closed_itemset = True
        for itemset_y in all_itemsets:
            if itemset_x != itemset_y and itemset_y.issuperset(itemset_x) and itemsets[itemset_y] == itemsets[itemset_x]:
                 is_closed_itemset = False
        if is_closed_itemset:
            closed_itemsets[itemset_x] = itemsets[itemset_x]
    return closed_itemsets


def extract_max_itemsets(itemsets):
    max_itemsets = {}
    all_itemsets = set(itemsets.keys())
    for itemset_x in itemsets:
        is_max_itemset = True
        for itemset_y in all_itemsets:
            if itemset_x != itemset_y and itemset_y.issuperset(itemset_x):
                 is_max_itemset = False
        if is_max_itemset:
            max_itemsets[itemset_x] = itemsets[itemset_x]
    return max_itemsets


def main():
    TDB, min_support = read_input()
    apriori = Apriori(min_support)
    apriori.compute(TDB)
    freq_itemsets = apriori.get_all_freq_itemsets()
    closed_itemsets = extract_closed_itemsets(freq_itemsets)
    max_itemsets = extract_max_itemsets(freq_itemsets)

    print_output(freq_itemsets)
    print_output(closed_itemsets)
    print_output(max_itemsets)


if __name__ == '__main__':
    main()
