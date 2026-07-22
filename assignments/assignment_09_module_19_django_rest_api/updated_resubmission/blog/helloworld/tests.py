from datetime import timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Post


class PostAPITests(APITestCase):
    def setUp(self):
        self.first_user = User.objects.create_user(
            username="abhijeet",
            password="BlogApi@2026"
        )

        self.second_user = User.objects.create_user(
            username="otheruser",
            password="OtherUser@2026"
        )

        self.first_token = Token.objects.create(
            user=self.first_user
        )

        self.second_token = Token.objects.create(
            user=self.second_user
        )

        self.base_time = timezone.now().replace(
            hour=12,
            minute=0,
            second=0,
            microsecond=0
        )

        titles = [
            "Django REST API Introduction",
            "Creating the Post Model",
            "Using Model Serializers",
            "Session and Token Authentication",
            "Owner Based Permissions",
            "Filtering and Search",
            "Pagination and Ordering",
        ]

        for index, title in enumerate(titles):
            post = Post.objects.create(
                user=self.first_user,
                title=title,
                content=f"Test content for {title}."
            )

            Post.objects.filter(pk=post.pk).update(
                created_at=self.base_time - timedelta(days=index)
            )

        self.other_post = Post.objects.create(
            user=self.second_user,
            title="Other User Private Post",
            content="This post belongs to another user."
        )

        self.list_url = reverse("post-list-create")

    def authenticate_first_user(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.first_token.key}"
        )

    def test_unauthenticated_user_cannot_access_posts(self):
        response = self.client.get(self.list_url)

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ]
        )

    def test_token_authentication_and_pagination(self):
        self.authenticate_first_user()

        response = self.client.get(self.list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(response.data["count"], 7)
        self.assertEqual(len(response.data["results"]), 5)

    def test_user_can_only_list_own_posts(self):
        self.authenticate_first_user()

        response = self.client.get(self.list_url)

        returned_users = {
            post["user"]
            for post in response.data["results"]
        }

        self.assertEqual(returned_users, {"abhijeet"})
        self.assertEqual(response.data["count"], 7)

    def test_create_post_assigns_logged_in_user(self):
        self.authenticate_first_user()

        data = {
            "title": "New Authenticated Post",
            "content": "Created through the API test."
        }

        response = self.client.post(
            self.list_url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(response.data["user"], "abhijeet")

        created_post = Post.objects.get(
            title="New Authenticated Post"
        )

        self.assertEqual(
            created_post.user,
            self.first_user
        )

    def test_retrieve_update_and_delete_own_post(self):
        self.authenticate_first_user()

        post = Post.objects.filter(
            user=self.first_user
        ).first()

        detail_url = reverse(
            "post-detail",
            kwargs={"pk": post.pk}
        )

        retrieve_response = self.client.get(detail_url)

        self.assertEqual(
            retrieve_response.status_code,
            status.HTTP_200_OK
        )

        update_response = self.client.put(
            detail_url,
            {
                "title": "Updated Blog Post",
                "content": "The post was updated successfully."
            },
            format="json"
        )

        self.assertEqual(
            update_response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            update_response.data["title"],
            "Updated Blog Post"
        )

        delete_response = self.client.delete(detail_url)

        self.assertEqual(
            delete_response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertFalse(
            Post.objects.filter(pk=post.pk).exists()
        )

    def test_user_cannot_access_another_users_post(self):
        self.authenticate_first_user()

        detail_url = reverse(
            "post-detail",
            kwargs={"pk": self.other_post.pk}
        )

        response = self.client.get(detail_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_search_and_ordering(self):
        self.authenticate_first_user()

        search_response = self.client.get(
            self.list_url,
            {"search": "Filtering"}
        )

        self.assertEqual(
            search_response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(search_response.data["count"], 1)
        self.assertEqual(
            search_response.data["results"][0]["title"],
            "Filtering and Search"
        )

        ordering_response = self.client.get(
            self.list_url,
            {"ordering": "-id"}
        )

        returned_ids = [
            post["id"]
            for post in ordering_response.data["results"]
        ]

        self.assertEqual(
            returned_ids,
            sorted(returned_ids, reverse=True)
        )

    def test_creation_date_filter(self):
        self.authenticate_first_user()

        filter_date = (
            self.base_time - timedelta(days=2)
        ).date().isoformat()

        response = self.client.get(
            self.list_url,
            {"created_after": filter_date}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(response.data["count"], 3)

    def test_token_endpoint_returns_token(self):
        response = self.client.post(
            reverse("api-token"),
            {
                "username": "abhijeet",
                "password": "BlogApi@2026"
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertIn("token", response.data)
