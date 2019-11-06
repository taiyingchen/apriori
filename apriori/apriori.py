from collections import Counter
from itertools import combinations


class Apriori():
    """
    Apriori is an algorithm for frequent item set mining and association rule learning.
    Using in-build python modules and frozenset data structure to accelerate performance.

    Parameters
    ----------
    min_support : int
        Minimum support threshold.
        If the support of an itemset is above this minimum support threshold,
        then it is a frequent itemset.
    """

    def __init__(self, min_support):
        self.min_support = min_support
        self.freq_itemsets = {}
        self.cand_itemsets = {}

    def has_infreq_subset(self, cand, k):
        """Check if a candidate itemset has an infrequent subset

        Parameters
        ----------
        cand : set of string
            Candidate itemset.
            Each element is a string represent an item.
        k : int
            Size of itemset.
            Should be len(cand) - 1

        Returns
        -------
        has_infreq_subset : bool
        """
        for subset in combinations(cand, k):
            if self.freq_itemsets[k][frozenset(subset)] < self.min_support:
                return True
        return False

    def generate_cand_itemsets(self, k):
        """Generate candidate itemsets of size k

        Parameters
        ----------
        k : int
            Size of itemset.

        Returns
        -------
        cand_itemsets : set of set of strings
            Candidate itemsets of size k.
            Each element is a set (frozenset) of items.
        """
        cand_itemsets = set()
        for i, p in enumerate(self.freq_itemsets[k-1]):
            for j, q in enumerate(self.freq_itemsets[k-1]):
                if i < j and len(p - q) == 1:
                    cand = p | q  # Joining
                    if self.has_infreq_subset(cand, k-1):
                        continue  # Pruning
                    else:
                        cand_itemsets.add(cand)
        return cand_itemsets

    def generate_freq_itemsets(self, k):
        """Generate frequent itemsets of size k based on candidate itemsets of size k

        Parameters
        ----------
        k : int
            Size of itemset.

        Returns
        -------
        freq_itemsets : dictionary
            Frequent itemsets of size k.
            Each key is an itemset stored with set (frozenset).
            Each value is the support value corresponding to its key.
        """
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
        freq_itemset = {frozenset(itemset): support for itemset,
                        support in counter.items() if support >= self.min_support}
        freq_itemset = Counter(freq_itemset)
        return freq_itemset

    def compute(self, TDB):
        """Main algorithm of Apriori

        Parameters
        ----------
        TDB : list of list of strings
            TDB stands for transactional database.
            Each row is a transaction with multiple items (strings).
        """
        # self.TDB = TDB
        self.TDB = [set(tran) for tran in TDB]
        k = 1
        # Frequent 1-itemset
        self.freq_itemsets[k] = self.generate_freq_itemsets(k)
        while self.freq_itemsets[k]:
            # Candidate generation
            self.cand_itemsets[k+1] = self.generate_cand_itemsets(k+1)
            # Derive frequent itemsets from candidates
            self.freq_itemsets[k+1] = self.generate_freq_itemsets(k+1)
            k += 1

    def get_all_freq_itemsets(self):
        """Return all the frequent itemsets in every size

        Returns
        -------
        all_freq_itemsets : Counter
            All frequent itemsets.
            Each key is an itemset stored with set (frozenset).
            Each value is the support value corresponding to its key.
        """
        all_freq_itemsets = Counter()
        for k in self.freq_itemsets:
            all_freq_itemsets += self.freq_itemsets[k]
        return all_freq_itemsets


def extract_closed_itemsets(itemsets):
    """Extract the closed itemsets from the given itemsets

    Returns
    -------
    closed_itemsets : dictionary
        Each key is an itemset stored with set (frozenset).
        Each value is the support value corresponding to its key.
    """
    closed_itemsets = {}
    all_itemsets = set(itemsets.keys())
    for itemset_x in itemsets:
        is_closed_itemset = True
        for itemset_y in all_itemsets:
            if itemset_x != itemset_y and itemset_y.issuperset(itemset_x) and itemsets[itemset_y] == itemsets[itemset_x]:
                is_closed_itemset = False
                break
        if is_closed_itemset:
            closed_itemsets[itemset_x] = itemsets[itemset_x]
    return closed_itemsets


def extract_max_itemsets(itemsets):
    """Extract the maximal itemsets from the given itemsets

    Returns
    -------
    closed_itemsets : dictionary
        Each key is an itemset stored with set (frozenset).
        Each value is the support value corresponding to its key.
    """
    max_itemsets = {}
    all_itemsets = set(itemsets.keys())
    for itemset_x in itemsets:
        is_max_itemset = True
        for itemset_y in all_itemsets:
            if itemset_x != itemset_y and itemset_y.issuperset(itemset_x):
                is_max_itemset = False
                break
        if is_max_itemset:
            max_itemsets[itemset_x] = itemsets[itemset_x]
    return max_itemsets


def main():
    TDB = [
        ['B', 'A', 'C', 'E', 'D'],
        ['A', 'C'],
        ['C', 'B', 'D']
    ]

    apriori = Apriori(min_support=2)
    apriori.compute(TDB)
    freq_itemsets = apriori.get_all_freq_itemsets()

    for itemset, support in freq_itemsets.items():
        print(f'{itemset}: {support}')


if __name__ == '__main__':
    main()
