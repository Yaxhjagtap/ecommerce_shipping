from .models import Box

def get_best_box_for_product(product):
    """
    Finds the cheapest box that can fit a product's dimensions and weight.
    Handles 3D rotation by sorting dimensions smallest to largest.
    """
    # 1. Query boxes that meet the weight requirement
    # 3. Order by cost ascending at the database level for optimization
    eligible_boxes = Box.objects.filter(
        max_weight_capacity__gte=product.weight
    ).order_by('cost')

    # Sort product dimensions (smallest to largest) to handle rotation
    prod_dims = sorted([product.length, product.width, product.height])

    for box in eligible_boxes:
        # Sort internal box dimensions (smallest to largest)
        box_dims = sorted([box.internal_length, box.internal_width, box.internal_height])

        # 2. Compare sorted dimensions to ensure a 3D fit
        if (prod_dims[0] <= box_dims[0] and
            prod_dims[1] <= box_dims[1] and
            prod_dims[2] <= box_dims[2]):
            
            # 4. Return the cheapest box (guaranteed by the order_by clause)
            return box

    # 5. Return None if no boxes fit
    return None