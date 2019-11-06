# Apriori

An efficient Python implementation of Apriori algorithm using built-in modules and frozenset data structure to accelerate performance.

Apriori is an algorithm for frequent item set mining and association rule learning over relational databases. It proceeds by identifying the frequent individual items in the database and extending them to larger and larger item sets as long as those item sets appear sufficiently often in the database. The frequent item sets determined by Apriori can be used to determine association rules which highlight general trends in the database. [1]

## Installation

```bash
git clone https://github.com/taiyingchen/apriori.git
cd apriori/
pip install .
```

### Dependecies

Required only Python (>= 3.6)

## Usage

`TDB` stands for transactional database. Each element in `TDB` is an transaction containing all items associated with it.

```python
from apriori import Apriori

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

# {'B'}: 2, {'A'}: 2, {'D'}: 2, {'C'}: 3
# {'B', 'D'}: 2, {'A', 'C'}: 2, {'B', 'C'}: 2, {'D', 'C'}: 2
# {'B', 'C', 'D'}: 2
```

## References

* [1] [Apriori Algorithm Wikipedia](https://en.wikipedia.org/wiki/Apriori_algorithm)
* [2] [Rakesh Agrawal and Ramakrishnan Srikant. Fast algorithms for mining association rules. Proceedings of the 20th International Conference on Very Large Data Bases, VLDB, pages 487-499, Santiago, Chile, September 1994.](http://www.vldb.org/conf/1994/P487.PDF)
