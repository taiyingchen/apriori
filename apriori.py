from sys import stdin


def read_input():
    min_support = int(input())
    TDB = []
    for tran in stdin:
        TDB.append(tran.strip().split())
    return TDB, min_support


class Apriori():
    def __init__(self, TDB, min_support):
        self.TDB = TDB
        self.min_support = min_support
        self.freq_itemset = {}
        self.cand_itemset = {}
        
    def generate_cand_itemset(self, k):
        pass 
    
    def generate_freq_itemset(self, k):
        pass
        
    def compute(self):
        k = 1
        self.freq_itemset[k] = self.generate_freq_itemset(k) # frequent 1-itemset
        while self.freq_itemset[k]:
            self.cand_itemset[k+1] = self.generate_cand_itemset(k+1) # candidate generation
            self.freq_itemset[k+1] = self.generate_freq_itemset(k+1) # frequent itemset generation
            k += 1

def main():
    TDB, min_support = read_input()
    apriori = Apriori(TDB, min_support)
    
    
if __name__ == '__main__':
    main()
