Merge "porous2.msh";
//+
Physical Curve("bottom concave", 1) = {1};
//+
Physical Curve("bottom concave", 1) += {1};
//+
Physical Curve("bottom left", 2) = {2};
//+
Physical Curve("left", 3) = {3};
//+
Physical Curve("top left", 4) = {4};
//+
Physical Curve("top concave", 5) = {5};
//+
Physical Curve("top right", 6) = {6};
//+
Physical Curve("right", 7) = {7};
//+
Physical Curve("bottom right", 8) = {8};
//+
Physical Curve("inter hole 1", 9) = {9};
//+
Physical Curve("inter hole 2", 10) = {10};
//+
Physical Curve("inter hole 3", 11) = {11};
//+
Physical Point(12) -= {4, 10, 9, 3, 2, 1, 11, 6, 5, 7, 8};
//+
Physical Surface("2D domain", 12) = {7};
