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


class Apriori():
    def __init__(self, TDB, min_support):
        self.TDB = TDB
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
        
    def compute(self):
        k = 1
        self.freq_itemsets[k] = self.generate_freq_itemsets(k) # frequent 1-itemset
        while self.freq_itemsets[k]:
            self.cand_itemsets[k+1] = self.generate_cand_itemsets(k+1) # candidate generation
            self.freq_itemsets[k+1] = self.generate_freq_itemsets(k+1) # frequent itemset generation
            k += 1

def main():
    TDB, min_support = read_input()
    apriori = Apriori(TDB, min_support)
    apriori.compute()
    pass
    
if __name__ == '__main__':
    main()
