"""Calculates total volume of all walls in the model."""

from Autodesk.Revit import DB

doc = __revit__.ActiveUIDocument.Document

# Creating collector instance and collecting all the walls from the model
wall_collector = DB.FilteredElementCollector(doc).OfCategory(
    DB.BuiltInCategory.OST_Walls).WhereElementIsNotElementType()
print("Total number of wall is: {}".format(len(wall_collector.ToElements())))\

window_collector = DB.FilteredElementCollector(doc).OfCategory(
    DB.BuiltInCategory.OST_Windows).WhereElementIsNotElementType()
print("Total number of windows is: {}".format(
    len(window_collector.ToElements())))

door_collector = DB.FilteredElementCollector(doc).OfCategory(
    DB.BuiltInCategory.OST_Doors).WhereElementIsNotElementType()
print("Total number of doors is: {}".format(len(door_collector.ToElements())))

# iterate wall and collect wall shape
for wall in wall_collector:
  loc_param = wall.Location
  if isinstance(loc_param, DB.LocationCurve):
    curve = loc_param.Curve
    if isinstance(curve, DB.Line):
      print("wall,{},{},{},{},{},{}".format(
          curve.GetEndPoint(0).X,
          curve.GetEndPoint(0).Y,
          curve.GetEndPoint(0).Z,
          curve.GetEndPoint(1).X,
          curve.GetEndPoint(1).Y,
          curve.GetEndPoint(1).Z))
      print("\n")

# iterate door and collect door shape
for door in door_collector:
  loc_param = door.Location
  if isinstance(loc_param, DB.LocationPoint):
    print("door,{},{},{}".format(loc_param.Point.X, loc_param.Point.Y,
                                 loc_param.Point.Z))
