def check_box_fit():
    # 1. Define the dummy data
    product_dims = [10, 5, 2]
    product_weight = 1

    box_dims = [5, 12, 3]
    box_capacity = 5

    # 2. Replicate the sorting logic
    # Sorting ensures we are always comparing the smallest side to the smallest side,
    # the middle to the middle, and the largest to the largest, regardless of orientation.
    sorted_prod = sorted(product_dims)
    sorted_box = sorted(box_dims)

    # 3. Replicate the comparison logic
    weight_fits = box_capacity >= product_weight
    
    dims_fit = (
        sorted_prod[0] <= sorted_box[0] and
        sorted_prod[1] <= sorted_box[1] and
        sorted_prod[2] <= sorted_box[2]
    )
    
    is_valid_match = weight_fits and dims_fit

    # 4. Print the results
    print("--- 3D Spatial Rotation Verification ---")
    print(f"Original Product Dims: {product_dims}")
    print(f"Sorted Product Dims:   {sorted_prod}")
    print("-" * 40)
    print(f"Original Box Dims:     {box_dims}")
    print(f"Sorted Box Dims:       {sorted_box}")
    print("-" * 40)
    print(f"Weight Check Passed:   {weight_fits}")
    print(f"Dimensions Fit:        {dims_fit}")
    print(f"Overall Fit Result:    {is_valid_match}")

if __name__ == "__main__":
    check_box_fit()