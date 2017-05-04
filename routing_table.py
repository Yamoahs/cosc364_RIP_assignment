# r = {node: [(hop, metric)]}

r = { 1: [(2, 1), (7, 8), (6, 5)], 
      2: [(1, 1), (3, 3)],
      3: [(2, 3), (4, 4)],
      4: [(3, 4), (7, 6), (5, 2)],
      5: [(4, 2), (6, 1)],
      6: [(5, 1), (1, 5)],
      7: [(1, 8), (4, 6)]}

for i in r:
    print("node", i, "------------//")
    
    for j in r[i]:
        next_hop, metric = j
        print("    next hop:", next_hop)
        print("    metric:  ", metric)
        print()
        

    
    
