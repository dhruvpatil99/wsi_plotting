from matplotlib import image
from matplotlib import pyplot as plt

data = image.imread('img.png')

input_data = '''
    Node* s = new Node("s",1690,340,0,true,30); 
    Node* c = new Node("c",950,310, 90, false ,50); 
    Node* d = new Node("d",520,480, 180, true,5); 
  
    Node* p1 = new Node("p1",1420,1528, 0, false,15);     
    Node* p2 = new Node("p2",1420,2566, 0, false,15); 
    Node* p3 = new Node("p3",1420,3550, 0, false,15);  
  
    Node* p1m = new Node("p1m",1630-60,1370-70, 0, true,5);  
    Node* p1h = new Node("p1h",1630-60,1685+100, 0, true,5);     
    Node* p2m = new Node("p2m",1630-60,2385-70, 0, true,5); 
    Node* p2h = new Node("p2h",1630-60,2700+100, 0, true,5); 
    Node* p3m = new Node("p3m",1630-60,3397-70, 0, true,5);  
    Node* p3h = new Node("p3h",1630-60,3700+100, 0, true,5); 
     
    Node* p4 = new Node("p4",580,3550, 180, false,15); 
    Node* p5 = new Node("p5",580,2520, 180, false,15); 
  
    Node* p4m = new Node("p4m",370+60,3710+100 , 180, true,5); 
    Node* p4h = new Node("p4h",370+60,3400-70 , 180, true,5); 
    Node* p5m = new Node("p5m",370+60,2645+100, 180, true,5); 
    Node* p5h = new Node("p5h",370+60,2337-70, 180, true,5); 
  
  
  
  
    Node* nsh = new Node("nsh",250,1260, -90, true,5); 
     
  
    Node* c1 = new Node("c1",1650,640, -1, false, 20); 
    Node* c2 = new Node("c2",720,640, -1, false, 30); 
    Node* c3 = new Node("c3",879,1528, -1, false,40); 
    Node* c4 = new Node("c4",879,2536, -1, false, 20); 
    Node* c5 = new Node("c5",879,3549, -1, false, 20); 
    Node* w = new Node("w",710,1210,180,true, 5); 
  
    Node* g1 = new Node("g1", 1220, 1435, 90, true,5); 
    Node* g2 = new Node("g2", 1220, 2445, 90, true,5); 
    Node* g3 = new Node("g3", 1220, 3455, 90, true,5); 
    Node* g4 = new Node("g4", 880, 3020, 180, true,5); 
    Node* g5 = new Node("g5", 880, 1950, 180, true,5);    

    Edge* edge_101 = new Edge(g1,c3 ); 
    Edge* edge_102 = new Edge(g2,c4 );
    Edge* edge_103 = new Edge(g3,c5 ); 
    Edge* edge_104 = new Edge(g4,c4 ); 
    Edge* edge_105 = new Edge(g5,c4 ); 

   Edge* edge_1 = new Edge(s,c1 ); 
    Edge* edge_2 = new Edge(c1,c2 ); 
    Edge* edge_3 = new Edge(c2,c ); 
    Edge* edge_4 = new Edge(c,d ); 
    Edge* edge_5 = new Edge(c2,nsh ); 
    Edge* edge_6 = new Edge(c2,c3 );  
    Edge* edge_7 = new Edge(c3, c4 ); 
    Edge* edge_8 = new Edge(c4,c5 ); 
    Edge* edge_11 = new Edge(c3, c5 );  
    Edge* edge_12 = new Edge(c,w); 
  
    Edge* edge_13 = new Edge(c3,p1m ); 
    Edge* edge_14 = new Edge(c3,p1h ); 
    Edge* edge_15 = new Edge(p1, p1m ); 
    Edge* edge_16 = new Edge(p1, p1h ); 
  
    Edge* edge_17 = new Edge(c4,p2m ); 
    Edge* edge_18 = new Edge(c4,p2h ); 
    Edge* edge_19 = new Edge(p2, p2m ); 
    Edge* edge_20= new Edge(p2, p2h ); 
  
    Edge* edge_21 = new Edge(c4,p5m ); 
    Edge* edge_22 = new Edge(c4,p5h ); 
    Edge* edge_23= new Edge(p5, p5m ); 
    Edge* edge_24 = new Edge(p5, p5h ); 
  
    Edge* edge_25 = new Edge(c5,p3m ); 
    Edge* edge_26 = new Edge(c5,p3h ); 
    Edge* edge_27 = new Edge(p3, p3m ); 
    Edge* edge_28 = new Edge(p3, p3h ); 
  
    Edge* edge_29 = new Edge(c5,p4m ); 
    Edge* edge_30 = new Edge(c5,p4h ); 
    Edge* edge_31 = new Edge(p4, p4m ); 
    Edge* edge_32 = new Edge(p4, p4h ); 
  
    Edge* edge_33 = new Edge(c2,w);
'''

lines = input_data.split(';')
filtered_lines = []
filtered_edges = []
for line in lines:
    if line.strip().startswith('N'):
        filtered_lines.append(line.strip())
        #print(line.strip())
    elif(line.strip().startswith('E')):
        filtered_edges.append(line.strip())
        #print(line.strip())
names = []
for line in filtered_lines:
    names.append(line.split('"')[1])

#for n in names:
#    print(n)

x_axis = []
for line in filtered_lines:
    x_axis.append(eval(line.split(',')[1].strip()))

edge_1 = []
edge_2 = []
for edge in filtered_edges:
    edge_1.append(edge.split('(')[1].split(',')[0].strip())
    edge_2.append(edge.split(',')[1].split(')')[0].strip())

for i in range(len(edge_1)):
    #print(edge_1[i], edge_2[i])
    pass
#for x in x_axis:
    #print(x)

y_axis = []
for line in filtered_lines:
    y_axis.append(eval(line.split(',')[2].strip()))

#for y in y_axis:
    #print(y)

#print(lines[0])
#data_array = []
#for i in range(0,len(filtered_lines)):
#    data_array.append(filtered_lines[i][21:23])

#for m in data_array:
#    print(m)

for i in range(0, len(names)):
    plt.plot(int(y_axis[i]), int(x_axis[i]), marker='v', color="black",)
    plt.annotate(names[i], (int(y_axis[i]), int(x_axis[i])))

for i in range(len(edge_1)):
    plt.plot((y_axis[names.index(edge_1[i])],y_axis[names.index(edge_2[i])]),(x_axis[names.index(edge_1[i])],x_axis[names.index(edge_2[i])]),color="black", linewidth=2)
#print(x_axis[names.index(edge_2[0])])
#plt.plot((1220,879),(1435,1538), color="black", linewidth=3)

plt.imshow(data)
plt.show()