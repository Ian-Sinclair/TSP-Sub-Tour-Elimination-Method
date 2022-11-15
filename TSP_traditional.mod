set ORIG; 
set DEST; 

param DISTANCE{i in ORIG, j in DEST}; 


var X{i in ORIG, j in DEST} binary;

minimize tour_cost: sum{i in ORIG, j in DEST} DISTANCE[i,j]*X[i,j];

subject to Flow_IN_constraint{j in DEST}: sum{i in ORIG} X[i,j] = 1;
subject to Flow_OUT_constraint{i in ORIG}: sum{j in DEST} X[i,j] = 1;

subject to Dont_Stay_at_city{j in ORIG}: X[j,j] = 0;