from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Box, Product
from .services import get_best_box_for_product

class BoxTestDataMixin:
    """Mixin to provide shared test data for both Service and API tests."""
    
    def setUp(self):
        # Box 1: For exact matches
        self.exact_box = Box.objects.create(
            name="Exact Box", internal_length=10, internal_width=10, internal_height=10, max_weight_capacity=10.0, cost=5.00
        )
        
        # Box 2: For 3D rotation testing (L=5, W=10, H=2)
        self.rotation_box = Box.objects.create(
            name="Rotation Box", internal_length=5, internal_width=10, internal_height=2, max_weight_capacity=5.0, cost=2.00
        )
        
        # Box 3 & 4: For testing cheapest selection amongst multiple valid boxes
        self.expensive_medium_box = Box.objects.create(
            name="Expensive Medium Box", internal_length=20, internal_width=20, internal_height=20, max_weight_capacity=20.0, cost=15.00
        )
        self.cheap_medium_box = Box.objects.create(
            name="Cheap Medium Box", internal_length=20, internal_width=20, internal_height=20, max_weight_capacity=20.0, cost=8.00
        )
        
        # Box 5: For testing heavy items (Huge dimensions, but very low weight capacity)
        self.fragile_large_box = Box.objects.create(
            name="Fragile Large Box", internal_length=50, internal_width=50, internal_height=50, max_weight_capacity=2.0, cost=10.00
        )


class BoxSelectionServiceTests(BoxTestDataMixin, TestCase):
    """Directly tests the core 3D packing and selection algorithm in services.py"""

    def test_perfect_fit(self):
        """Edge Case 1: Product dimensions match box internal dimensions exactly."""
        product = Product.objects.create(name="Cube", length=10, width=10, height=10, weight=5)
        best_box = get_best_box_for_product(product)
        
        self.assertIsNotNone(best_box)
        self.assertEqual(best_box.name, "Exact Box")

    def test_3d_rotation_fit(self):
        """Edge Case 2: Product requires 3D rotation to fit."""
        # Product is 10x5x2. Box is 5x10x2.
        product = Product.objects.create(name="Flat Device", length=10, width=5, height=2, weight=1)
        best_box = get_best_box_for_product(product)
        
        self.assertIsNotNone(best_box)
        self.assertEqual(best_box.name, "Rotation Box")

    def test_fits_dimensions_but_too_heavy(self):
        """Edge Case 3: Product fits dimensions but exceeds weight capacity."""
        # Fits inside the 50x50x50 Fragile box, but weighs 15 (max cap is 2).
        product = Product.objects.create(name="Dense Object", length=40, width=40, height=40, weight=15)
        best_box = get_best_box_for_product(product)
        
        self.assertIsNone(best_box)

    def test_multiple_fits_chooses_cheapest(self):
        """Edge Case 4: Product fits in multiple boxes, must select the cheapest."""
        # Fits in both Expensive Medium ($15) and Cheap Medium ($8).
        product = Product.objects.create(name="Standard Item", length=15, width=15, height=15, weight=5)
        best_box = get_best_box_for_product(product)
        
        self.assertIsNotNone(best_box)
        self.assertEqual(best_box.name, "Cheap Medium Box")

    def test_too_large_for_all_boxes(self):
        """Edge Case 5: Product is simply too large for any available box."""
        product = Product.objects.create(name="Giant Item", length=100, width=100, height=100, weight=1)
        best_box = get_best_box_for_product(product)
        
        self.assertIsNone(best_box)


class BoxSelectionAPITests(BoxTestDataMixin, APITestCase):
    """Tests the REST API endpoint responses and status codes."""

    def test_api_perfect_fit_200(self):
        """Edge Case 1 via API: Perfect fit returns 200 OK and correct data."""
        product = Product.objects.create(name="Cube", length=10, width=10, height=10, weight=5)
        response = self.client.get(f'/api/box-selector/recommend-box/{product.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['recommended_box']['name'], "Exact Box")
        # Ensure precision fields are handled correctly
        self.assertEqual(float(response.data['recommended_box']['cost']), 5.00)

    def test_api_3d_rotation_fit_200(self):
        """Edge Case 2 via API: 3D rotation logic holds up through the endpoint."""
        product = Product.objects.create(name="Flat Device", length=10, width=5, height=2, weight=1)
        response = self.client.get(f'/api/box-selector/recommend-box/{product.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['recommended_box']['name'], "Rotation Box")

    def test_api_too_heavy_404(self):
        """Edge Case 3 via API: Heavy item returns 404 with error message."""
        product = Product.objects.create(name="Dense Object", length=40, width=40, height=40, weight=15)
        response = self.client.get(f'/api/box-selector/recommend-box/{product.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)
        self.assertTrue("No suitable box exists" in response.data['error'])

    def test_api_cheapest_selection_200(self):
        """Edge Case 4 via API: Endpoint serves the cheapest valid box."""
        product = Product.objects.create(name="Standard Item", length=15, width=15, height=15, weight=5)
        response = self.client.get(f'/api/box-selector/recommend-box/{product.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['recommended_box']['name'], "Cheap Medium Box")

    def test_api_too_large_404(self):
        """Edge Case 5 via API: Large item returns 404 with error message."""
        product = Product.objects.create(name="Giant Item", length=100, width=100, height=100, weight=1)
        response = self.client.get(f'/api/box-selector/recommend-box/{product.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)

    def test_api_invalid_product_id_404(self):
        """Bonus Edge Case: Querying a product ID that does not exist."""
        # 9999 is highly unlikely to exist in an empty test database
        response = self.client.get('/api/box-selector/recommend-box/9999/')
        
        # get_object_or_404 will throw standard DRF 404 detail message
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)