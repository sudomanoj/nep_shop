from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from . import serializers

LISTCATEGORY = swagger_auto_schema(
    tags=['product_category'],
    operation_summary='List all categories.',
    operation_description='This endpoint retrieves all categories of the site.',
    operation_id='list_categories',
    request_body=None,
    responses={200: serializers.CategorySerializer(many=True), 400: "Invalid data"}
)

CREATECATEGORY = swagger_auto_schema(
    tags=['product_category'],
    operation_summary='Create a category.',
    operation_description='This endpoint creates a new category.',
    operation_id='create_category',
    request_body=serializers.CategorySerializer,
    responses={201: "Category created successfully", 400: "Invalid data"}
)

UPDATECATEGORY = swagger_auto_schema(
    tags=['product_category'],
    operation_summary='Update a category.',
    operation_description='This endpoint updates a category by its id.',
    operation_id='update_category',
    request_body=serializers.CategorySerializer,
    responses={200: "Category updated successfully", 400: "Invalid data"}
)
    

LISTPRODUCT = swagger_auto_schema(
    tags=['product'],
    operation_summary='List all products.',
    operation_description='This endpoint retrieves all products of the site.',
    operation_id='list_products',
    request_body=None,
    responses={200: serializers.ProductSerializer(many=True), 400: "Invalid data"}
)

CREATEPRODUCT = swagger_auto_schema(
    tags=['product'],
    operation_summary='Create a product.',
    operation_description='This endpoint creates a new product.',
    operation_id='create_product',
    request_body=serializers.ProductAddSerializer,
    responses={201: "Product created successfully", 400: "Invalid data"}
)

GETPRODUCT = swagger_auto_schema(
    tags=['product'],
    operation_summary='Get a product.',
    operation_description='This endpoint retrieves a product by its id.',
    operation_id='get_product',
    request_body=None,
    responses={200: serializers.ProductSerializer, 400: "Invalid data"}
)


UPDATEPRODUCT = swagger_auto_schema(
    tags=['product'],
    operation_summary='Update a product.',
    operation_description='This endpoint updates a product by its id.',
    operation_id='update_product',
    request_body=serializers.ProductAddSerializer,
    responses={200: "Product updated successfully", 400: "Invalid data"}
)

CREATEPRODUCTIMAGE = swagger_auto_schema(
    tags=['product'],
    operation_summary='Create a product image.',
    operation_description='This endpoint creates a new product image.',
    operation_id='create_product_image',
    request_body=serializers.ProductImageSerializer,
    responses={201: "Product image created successfully", 400: "Invalid data"}
)

UPDATEPRODUCTIMAGE = swagger_auto_schema(
    tags=['product'],
    operation_summary='Update a product image.',
    operation_description='This endpoint updates a product image by its id.',
    operation_id='update_product_image',
    request_body=serializers.ProductImageSerializer,
    responses={200: "Product image updated successfully", 400: "Invalid data"}
)

DELETEPRODUCTIMAGE = swagger_auto_schema(
    tags=['product'],
    operation_summary='Delete a product image.',
    operation_description='This endpoint deletes a product image by its id.',
    operation_id='delete_product_image',
    request_body=None,
    responses={204: "Product image deleted successfully", 400: "Invalid data"}
)

CREATERATING = swagger_auto_schema(
    tags=['rating'],
    operation_summary='Create a rating.',
    operation_description='This endpoint creates a new rating.',
    operation_id='create_rating',
    request_body=serializers.RatingSerializer,
    responses={201: "Rating created successfully", 400: "Invalid data"}
)

LISTRATING = swagger_auto_schema(
    tags=['rating'],
    operation_summary='List all ratings.',
    operation_description='This endpoint retrieves all ratings of the site.',
    operation_id='list_ratings',
    request_body=None,
    responses={200: serializers.RatingSerializer(many=True), 400: "Invalid data"}
)

UPDATERATING = swagger_auto_schema(
    tags=['rating'],
    operation_summary='Update a rating.',
    operation_description='This endpoint updates a rating by its id.',
    operation_id='update_rating',
    request_body=serializers.RatingSerializer,
    responses={200: "Rating updated successfully", 400: "Invalid data"}
)

DELETERATING = swagger_auto_schema(
    tags=['rating'],
    operation_summary='Delete a rating.',
    operation_description='This endpoint deletes a rating by its id.',
    operation_id='delete_rating',
    request_body=None,
    responses={204: "Rating deleted successfully", 400: "Invalid data"}
)