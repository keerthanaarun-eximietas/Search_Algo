# Search Algo Lab

A small, dependency-free Python playground for search algorithms, graph traversal,
tries, tests, and controlled quality-assurance defects.

## Layout

- `search_algorithms\` contains reusable algorithms grouped by data structure.
- `tests\` covers normal behavior and documents known-bug examples.
- `fixtures\Bad-Names.py` deliberately violates naming and line-length rules.
- `fixtures\generate_rule_violations.py` produces oversized temporary files for
  testing filename, line-count, function-size, and final-newline checks.
- `search.py` keeps the original `linear_search` and `binary_search` entry points.

## Algorithms

The package includes linear and sentinel scans; binary, jump, interpolation,
exponential, Fibonacci, and ternary search; breadth-first and depth-first graph
path search; and a prefix trie.

| Algorithm | Typical time | Worst time | Extra space |
|---|---:|---:|---:|
| Linear search | O(n) | O(n) | O(1) |
| Sentinel search | O(n) | O(n) | O(n) |
| Binary search | O(log n) | O(log n) | O(1) |
| Jump search | O(sqrt(n)) | O(sqrt(n)) | O(1) |
| Interpolation search | O(log log n) | O(n) | O(1) |
| Exponential search | O(log n) | O(log n) | O(1) |
| Fibonacci search | O(log n) | O(log n) | O(1) |
| Ternary search | O(log n) | O(log n) | O(1) |
| BFS / DFS | O(V + E) | O(V + E) | O(V) |
| Trie lookup / insert | O(L) | O(L) | O(L) per new key |

`n` is the input size, `V` and `E` are graph vertices and edges, and `L` is
the length of the searched or inserted string. Interpolation's typical bound
assumes reasonably uniform values. Sentinel search copies the sequence so it
can append a sentinel without mutating caller-owned data.

```python
from search_algorithms import binary_search, breadth_first_search

print(binary_search([1, 4, 8, 12], 8))
print(breadth_first_search({"A": ["B"], "B": ["C"], "C": []}, "A", "C"))
```

Binary, jump, interpolation, exponential, Fibonacci, and ternary search expect
ascending sorted input. Graph functions accept a mapping of nodes to neighbors
and return a path, or `None` when no path is found. `Trie` stores string keys.

## Run the tests and demo

```powershell
python -m unittest discover -s tests -v
python search.py
```

The tests for known defects are marked as expected failures so the normal test
run stays usable while making those defects visible. `fixtures\Bad-Names.py`
and files produced by the fixture generator are intentionally invalid examples;
do not import or use them in application code. To create generated fixtures:

```powershell
python fixtures\generate_rule_violations.py C:\temp\search-rule-fixtures
```

The generator writes a non-snake-case filename, an over-500-line module, a
function over 80 lines, a line over 120 characters, and a file without a final
newline. Its output folder can be safely removed after testing.

## Intentionally unsafe-looking demo values

`search_algorithms\demo_config.py` includes obvious `FAKE_DO_NOT_USE` strings
for secret-scanner testing. They are invented placeholders, not credentials,
and must never be treated as usable keys.
