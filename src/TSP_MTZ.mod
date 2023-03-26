set ORIG ordered; 
set DEST ordered; 

param DISTANCE{i in ORIG, j in DEST}; 


var X{i in ORIG, j in DEST} binary;
var t{1 .. card(ORIG)} >=0;

minimize tour_cost: sum{i in ORIG, j in DEST} DISTANCE[i,j]*X[i,j];

subject to Flow_IN_constraint{j in DEST}: sum{i in ORIG} X[i,j] = 1;
subject to Flow_OUT_constraint{i in ORIG}: sum{j in DEST} X[i,j] = 1;

subject to Dont_Stay_at_city{j in ORIG}: X[j,j] = 0;

subject to Time_Sequence_Constraint{i in 1..card(ORIG) , j in 1..card(DEST) : j != 1}:  t[j] >= t[i]+1-100*(1-X[member(i, ORIG),member(j, DEST)]);

subject to Initialize_Time_Sequence: t[1] = 1;