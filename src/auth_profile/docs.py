from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from . import serializers

LISTUSER = swagger_auto_schema(
    tags=['auth_profile'],
    operation_summary='List all users.',
    operation_description='This endpoint retrieves all users of the site.',
    operation_id='list_users',
    request_body=None,
    responses={200: serializers.UserListSerializer(many=True), 400: "Invalid data"}
)

CREATEUSER = swagger_auto_schema(
    tags=['auth_profile'],
    operation_summary='Create a user.',
    operation_description='This endpoint creates a new user.',
    operation_id='create_user',
    request_body=serializers.UserCreateSerializer,
    responses={201: "User created successfully", 400: "Invalid data"}
)

RETRIEVEUSER = swagger_auto_schema(
    tags=['auth_profile'],
    operation_summary='Retrieve a user.',
    operation_description='This endpoint retrieves a user by id.',
    operation_id='retrieve_user',
    request_body=None,
    responses={200: serializers.UserListSerializer, 400: "Invalid data"}
)

USERLOGIN = swagger_auto_schema(
    tags=['auth_profile'],
    operation_summary='Login a user.',
    operation_description='This endpoint logs in a user.',
    operation_id='login_user',
    request_body=serializers.UserLoginSerializer,
    responses={200: "Login successful", 400: "Invalid credentials"}
)


STORELIST = swagger_auto_schema(
    tags=['store'],
    operation_summary='List all stores.',
    operation_description='This endpoint retrieves all stores of the site.',
    operation_id='list_stores',
    request_body=None,
    responses={200: serializers.StoreSerializer(many=True), 400: "Invalid data"}
)

STORECREATE = swagger_auto_schema(
    tags=['store'],
    operation_summary='Create a store.',
    operation_description='This endpoint creates a new store.',
    operation_id='create_store',
    request_body=serializers.StoreSerializer,
    responses={201: "Store created successfully", 400: "Invalid data"}
)

STORERETRIEVE = swagger_auto_schema(
    tags=['store'],
    operation_summary='Retrieve a store.',
    operation_description='This endpoint retrieves a store by id.',
    operation_id='retrieve_store',
    request_body=None,
    responses={200: serializers.StoreSerializer, 400: "Invalid data"}
)

STOREUPDATE = swagger_auto_schema(
    tags=['store'],
    operation_summary='Update a store.',
    operation_description='This endpoint updates a store by id.',
    operation_id='update_store',
    request_body=serializers.StoreSerializer,
    responses={204: "Store updated successfully", 400: "Invalid data"}
)

SELLERLIST = swagger_auto_schema(
    tags=['seller'],
    operation_summary='List all sellers.',
    operation_description='This endpoint retrieves all sellers of the site.',
    operation_id='list_sellers',
    request_body=None,
    responses={200: serializers.SellerSerializer(many=True), 400: "Invalid data"}
)

