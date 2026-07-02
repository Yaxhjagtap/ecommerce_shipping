from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import BoxSerializer
from .services import get_best_box_for_product

@api_view(['GET'])
def recommend_box_for_product(request, product_id):
    """
    API endpoint that accepts a Product ID and returns the best Box.
    """
    # 1. Fetch the product. Returns standard 404 JSON if not found.
    product = get_object_or_404(Product, id=product_id)

    # 2. Run the 3D packing algorithm
    best_box = get_best_box_for_product(product)

    # 3. Handle the case where no box fits
    if not best_box:
        return Response(
            {"error": f"No suitable box exists that can fit product '{product.name}'."},
            status=status.HTTP_404_NOT_FOUND
        )

    # 4. Serialize and return the best box
    serializer = BoxSerializer(best_box)
    return Response(
        {
            "message": "Optimal box found.",
            "recommended_box": serializer.data
        },
        status=status.HTTP_200_OK
    )