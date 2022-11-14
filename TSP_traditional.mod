set ORIG; 
set DEST; 

param DISTANCE{i in ORIG, j in DEST}; 

var X{i in ORIG, j in DEST} binary;

minimize tour_cost: sum{i in ORIG, j in DEST} DISTANCE[i,j]*X[i,j];

subject to CONSTRAINT_1{j in DEST}: sum{i in ORIG} X[i,j] = 1;
subject to CONSTRAINT_2{i in ORIG}: sum{j in DEST} X[i,j] = 1;
subject to CONSTRAINT_3: sum{j in ORIG} X[j,j] = 0;
