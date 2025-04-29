from django.contrib.gis.geos.point import Point
from django.test import TestCase
from ninja.testing import TestAsyncClient

from users.api import UserIn, router
from users.models import User


def get_user_ids(users: list[User]):
    return [user.__dict__["id"] for user in users]


class UserTests(TestCase):
    def setUp(self):
        self.client = TestAsyncClient(router)
        self.users = [
            User.objects.create(geo_pos=Point(12.3, 10.4)),
            User.objects.create(geo_pos=Point(10.4, 12.3)),
            User.objects.create(geo_pos=Point(50.4, 22.3)),
            User.objects.create(geo_pos=Point(57.4, 22.3)),
        ]

    async def test_create(self):

        coords = (1, 2)

        response = await self.client.post(
            "/create", json={"longitude": coords[0], "latitude": coords[1]}
        )
        self.assertEqual(response.status_code, 200, response)
        new_user = (await User.objects.alatest("id")).__dict__

        self.assertEqual(new_user["geo_pos"].coords, coords)

    async def test_delete(self):
        old_users = get_user_ids([user async for user in User.objects.all()])
        self.assertNotEqual(old_users, [])

        to_delete = old_users[0]

        response = await self.client.delete(
            "/delete", query_params={"user_id": to_delete}
        )
        self.assertEqual(response.status_code, 200, response)

        new_count = len([user async for user in User.objects.all()])

        # new user count - old user count == 1
        self.assertEqual(len(old_users) - new_count, 1)

        # Deleting a non-existing ID should return a 404
        response = await self.client.delete(
            "/delete", query_params={"user_id": to_delete}
        )
        self.assertEqual(response.status_code, 404, response)

    async def test_view_all(self):
        response = await self.client.get("/view-all")
        user_ids = sorted([user["id"] for user in response.data])

        self.assertListEqual(user_ids, get_user_ids(self.users), response)

    async def test_view_within_bbox_one(self):
        response = await self.client.get(
            "/view-within-bbox",
            query_params={
                "longitude_min": 12.2,
                "latitude_min": 10.3,
                "longitude_max": 12.4,
                "latitude_max": 10.5,
            },
        )
        self.assertEqual(response.status_code, 200, response)
        user_ids = sorted([user["id"] for user in response.data])

        self.assertListEqual(user_ids, get_user_ids([self.users[0]]), response)

    async def test_view_within_bbox_multiple(self):
        response = await self.client.get(
            "/view-within-bbox",
            query_params={
                "longitude_min": 10.3,
                "latitude_min": 10.3,
                "longitude_max": 12.4,
                "latitude_max": 12.4,
            },
        )
        self.assertEqual(response.status_code, 200, response)
        user_ids = sorted([user["id"] for user in response.data])

        self.assertListEqual(
            user_ids, get_user_ids([self.users[0], self.users[1]]), response
        )
