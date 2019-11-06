# Apriori

An efficient Python implementation of Apriori algorithm using in-build python modules and frozenset data structure to accelerate performance.

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
