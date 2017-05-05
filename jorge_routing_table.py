inf = 16
r = { 1: [(2, 1), (7, 8), (6, 5)],   
      2: [(1, 1), (3, 3)],  
      3: [(2, 3), (4, 4)],  
      4: [(3, 4), (7, 6), (5, 2)],  
      5: [(4, 2), (6, 1)],  
      6: [(5, 1), (1, 5)],  
      7: [(1, 8), (4, 6)]} 
 
table = { 1: [(1, 0),   (2, 1),   (3, inf), (4, inf), (5, inf), (6, 5),   (7, 8)], 
          2: [(1, 1),   (2, 0),   (3, 3),   (4, inf), (5, inf), (6, inf), (7, inf)], 
          3: [(1, inf), (2, 3),   (3, 0),   (4, 4),   (5, inf), (6, inf), (7, inf)], 
          4: [(1, inf), (2, inf), (3, 4),   (4, 0),   (5, 2),   (6, inf), (7, 6)], 
          5: [(1, inf), (2, inf), (3, inf), (4, 2),   (5, 0),   (6, 1),   (7, inf)], 
          6: [(1, 5),   (2, inf), (3, inf), (4, inf), (5, 1),   (6, 0),   (7, inf)], 
          7: [(1, 8),   (2, inf), (3, inf), (4, 6),   (5, inf), (6, inf), (7, 0)]} 
 
for i_router in table.keys():  
  print ("router:", i_router, "------------//")
   
  for to_node_and_cost in table[i_router]:  
    print("table i_router:" table[i_router])
    next_hop = to_node_and_cost[0]  
    metric = to_node_and_cost[1] 
       
    #min_cost = min( (
    #print "min cost:", min_cost 
     
    #print "    to node:", j[0] 
    #print "    at cost:", j[1] 
 
    if( metric != 0): 
      print ("    next hop:", next_hop)  
      print ("    metric:  ", metric )
      print () 
      
    #for i in range(0, 10000000):
    #  i += i
    
