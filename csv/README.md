# CSV Format Guide
Each CSV file stores information about one typical building structure. 

## Walls
Walls are treated as a collection of line segments in pyRevit.

For the rows starting with `wall`, the rest of 6 numbers are: `start_point_x,start_point_y,start_point_z,end_point_x,end_point_y,end_point_z` for each line segment. Each line segment represents a chunk of wall.

## Doors
Doors are treated as points in pyRevit.

For the rows starting with `door`, the rest of 6 numbers are: `x,y,z,UNUSED,UNUSED,UNUSED`.
