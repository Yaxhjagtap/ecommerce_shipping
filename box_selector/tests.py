from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Box, Product


class BoxSelectionAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Multiple boxes
        self.small_box = Box.objects.create(
            name="Small Box",
            internal_length=5,
            internal_width=12,
            internal_height=3,
            max_weight_capacity=5,
            cost=1.50
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            internal_length=15,
            internal_width=15,
            internal_height=15,
            max_weight_capacity=10,
            cost=2.50
        )

        self.large_box = Box.objects.create(
            name="Large Box",
            internal_length=20,
            internal_width=20,
            internal_height=20,
            max_weight_capacity=25,
            cost=4.00
        )

        # Product fits multiple boxes
        self.phone = Product.objects.create(
            name="Smartphone",
            length=10,
            width=5,
            height=2,
            weight=1
        )

        # Heavy product
        self.heavy_product = Product.objects.create(
            name="Anvil",
            length=5,
            width=5,
            height=5,
            weight=500
        )

        # Rotation test product
        self.rotated_product = Product.objects.create(
            name="Rotated Item",
            length=10,
            width=5,
            height=2,
            weight=2
        )

        # Exact weight boundary
        self.boundary_product = Product.objects.create(
            name="Boundary Product",
            length=4,
            width=4,
            height=2,
            weight=5
        )

    # --------------------------------------------------------
    # 1. Success case
    # --------------------------------------------------------
    def test_recommend_box_success(self):
        """
        API should return cheapest valid box
        """
        response = self.client.get(
            f'/api/box-selector/recommend-box/{self.phone.id}/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['recommended_box']['name'],
            "Small Box"
        )

    # --------------------------------------------------------
    # 2. No suitable box
    # --------------------------------------------------------
    def test_recommend_box_no_fit(self):
        """
        API should return 404 when no box fits
        """
        response = self.client.get(
            f'/api/box-selector/recommend-box/{self.heavy_product.id}/'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn(
            "No suitable box exists",
            response.data['error']
        )

    # --------------------------------------------------------
    # 3. Invalid product id
    # --------------------------------------------------------
    def test_invalid_product_id(self):
        """
        API should return 404 if product does not exist
        """
        response = self.client.get(
            '/api/box-selector/recommend-box/999/'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # --------------------------------------------------------
    # 4. Cheapest box chosen
    # --------------------------------------------------------
    def test_cheapest_box_selected(self):
        """
        If multiple boxes fit, choose lowest cost
        """
        response = self.client.get(
            f'/api/box-selector/recommend-box/{self.phone.id}/'
        )

        self.assertEqual(
            response.data['recommended_box']['name'],
            "Small Box"
        )

        self.assertEqual(
            float(response.data['recommended_box']['cost']),
            1.50
        )

    # --------------------------------------------------------
    # 5. Rotation logic test
    # --------------------------------------------------------
    def test_rotation_logic(self):
        """
        Product dimensions should fit after sorting/rotation
        """
        response = self.client.get(
            f'/api/box-selector/recommend-box/{self.rotated_product.id}/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --------------------------------------------------------
    # 6. Exact weight boundary
    # --------------------------------------------------------
    def test_exact_weight_boundary(self):
        """
        Product weight equal to max box weight should work
        """
        response = self.client.get(
            f'/api/box-selector/recommend-box/{self.boundary_product.id}/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --------------------------------------------------------
    # 7. Remove all boxes
    # --------------------------------------------------------
    def test_no_boxes_in_database(self):
        """
        If no boxes exist, API should fail gracefully
        """
        Box.objects.all().delete()

        response = self.client.get(
            f'/api/box-selector/recommend-box/{self.phone.id}/'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # --------------------------------------------------------
    # 8. Response structure validation
    # --------------------------------------------------------
    def test_response_structure(self):
        """
        API response should contain expected keys
        """
        response = self.client.get(
            f'/api/box-selector/recommend-box/{self.phone.id}/'
        )

        self.assertIn("recommended_box", response.data)
        self.assertIn("name", response.data["recommended_box"])
        self.assertIn("cost", response.data["recommended_box"])