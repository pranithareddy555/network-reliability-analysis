# Network Reliability Analysis (Triangle Failures)

Computes network reliability for a complete graph on 5 nodes where **triangles fail** with probability (1-p).
A failed triangle removes all 3 of its edges. The network is **operational if no node is isolated**.

## How to run
```bash
pip install networkx matplotlib numpy
python network_reliability.py
