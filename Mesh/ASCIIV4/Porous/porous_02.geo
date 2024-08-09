Merge "porous_02.msh";
//+
Physical Point(1) -= {4, 5, 6, 7, 10, 11, 9, 3, 2, 1, 8};
//+
Physical Curve("bottom concave", 1) = {1};
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
Physical Curve("bottom right", 8) = {10, 8};
//+
Physical Curve("inter hole 1", 9) = {10};
//+
Physical Curve("inter hole 2", 11) = {9};
//+
Physical Curve("inter hole 3", 12) = {11};
//+
Physical Curve(" inter hole 2", 11) -= {9};
//+
Physical Curve(" inter hole 3", 12) -= {11};
//+
Physical Curve("inter hole 2", 10) = {9};
//+
Physical Curve("inter hole 3", 13) = {11};
//+
Physical Curve("inter hole 3", 11) = {11};
//+
Physical Curve("inter hole 3", 11) = {11};
//+
Physical Curve(" inter hole 3", 13) -= {11};
//+
Physical Curve("inter hole 3", 11) = {11};
//+
Physical Surface("2D Domain", 12) = {7};
