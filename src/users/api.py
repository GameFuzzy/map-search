from django.contrib.gis.geos.point import Point
from django.contrib.gis.geos.polygon import Polygon
from django.http import Http404
from geojson_pydantic import Point as PointType
from ninja import ModelSchema, Router, Schema

from .models import User

router = Router()


# Schema for returning a user
class UserOut(ModelSchema):
    geo_pos_geometry: PointType

    class Config:
        model = User
        model_fields = ["id"]


# Schema for creating a user
class UserIn(Schema):
    longitude: float
    latitude: float


# Endpoint for creating a user
@router.post("/create")
async def create_user(request, data: UserIn):
    user = await User.objects.acreate(geo_pos=Point(data.longitude, data.latitude))
    return {"id": user.id}


# Endpoint for deleting a user
@router.delete("/delete")
async def delete_user(request, user_id: int):
    try:
        user = await User.objects.aget(pk=user_id)
        await user.adelete()
    except:
        raise Http404
    return {"success": True}


# Endpoint for viewing all users
@router.get("/view-all", response=list[UserOut])
async def view_all_users(request):
    return [user async for user in User.objects.all()]


# Endpoint for viewing all users within a given bounding box
@router.get("/view-within-bbox", response=list[UserOut])
async def view_users_within_bounding_box(
    request,
    longitude_min: float,
    latitude_min: float,
    longitude_max: float,
    latitude_max: float,
):

    bbox = (longitude_min, latitude_min, longitude_max, latitude_max)
    geom = Polygon.from_bbox(bbox)

    return [user async for user in User.objects.filter(geo_pos__within=geom)]
