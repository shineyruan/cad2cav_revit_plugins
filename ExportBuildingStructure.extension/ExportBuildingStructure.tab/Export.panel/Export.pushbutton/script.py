"""Calculates total volume of all walls in the model."""

FEET2METER = 0.3048

from Autodesk.Revit import DB

doc = __revit__.ActiveUIDocument.Document

# Creating collector instance and collecting all the walls from the model
wall_collector = DB.FilteredElementCollector(doc).OfCategory(
    DB.BuiltInCategory.OST_Walls).WhereElementIsNotElementType()
print("Total number of wall is: {}".format(len(wall_collector.ToElements())))

window_collector = DB.FilteredElementCollector(doc).OfCategory(
    DB.BuiltInCategory.OST_Windows).WhereElementIsNotElementType()
print("Total number of windows is: {}".format(
    len(window_collector.ToElements())))

door_collector = DB.FilteredElementCollector(doc).OfCategory(
    DB.BuiltInCategory.OST_Doors).WhereElementIsNotElementType()
print("Total number of doors is: {}".format(len(door_collector.ToElements())))

# print csv title
print("Type,x_1,y_1,z_1,x_2,y_2,z_2,Orientation,Width,Height")

# iterate wall and collect wall shape
for wall in wall_collector:
  loc_param = wall.Location
  if isinstance(loc_param, DB.LocationCurve):
    curve = loc_param.Curve
    if isinstance(curve, DB.Line):
      # no width or height info for wall object
      print("wall,{},{},{},{},{},{},0.0,0.0,0.0".format(
          FEET2METER * curve.GetEndPoint(0).X,
          FEET2METER * curve.GetEndPoint(0).Y,
          FEET2METER * curve.GetEndPoint(0).Z,
          FEET2METER * curve.GetEndPoint(1).X,
          FEET2METER * curve.GetEndPoint(1).Y,
          FEET2METER * curve.GetEndPoint(1).Z))
      print("\n")

# iterate door and collect door shape
for door in door_collector:
  original_name_str = door.Name
  list_str = original_name_str.split()

  # door name is always in pattern `0864 x 2032mm`
  door_width = float(list_str[0]) / 1000
  door_height = float(list_str[-1][:-2]) / 1000

  loc_param = door.Location
  if isinstance(loc_param, DB.LocationPoint):
    print("door,{},{},{},0.0,0.0,0.0,{},{},{}".format(
        FEET2METER * loc_param.Point.X, FEET2METER * loc_param.Point.Y,
        FEET2METER * loc_param.Point.Z, loc_param.Rotation, door_width,
        door_height))

# iterate window and collect window shape
for window in window_collector:
  original_name_str = window.Name
  list_str = original_name_str.split()

  # window name is always in pattern `0864 x 2032mm`
  window_width = float(list_str[0]) / 1000
  window_height = float(list_str[-1][:-2]) / 1000

  loc_param = window.Location
  if isinstance(loc_param, DB.LocationPoint):
    print("window,{},{},{},0.0,0.0,0.0,{},{},{}".format(
        FEET2METER * loc_param.Point.X, FEET2METER * loc_param.Point.Y,
        FEET2METER * loc_param.Point.Z, loc_param.Rotation, window_width,
        window_height))
