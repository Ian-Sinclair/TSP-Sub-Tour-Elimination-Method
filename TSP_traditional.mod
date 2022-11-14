set variables;

param mu1 = 0;
param mu2 = 0.001;

param object{x in variables};

var Y{y in variables} >=0;

minimize total_Object: sum{y in variables} object[y]*Y[y] - mu1*(80-30*Y[1]-50*Y[3]) - mu2*(60-30*Y[2]-50*Y[4]);

subject to CONSTRAINT_1: Y[1] + Y[2] = 1;
subject to CONSTRAINT_2: Y[3] + Y[4] = 1;



