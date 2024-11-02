from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer


@api_view(['GET'])
def get_products(request):
    """
    Retrieve a list of all products.
    Returns a JSON response containing serialized product data or a message if no products are found.
    """
    products = Product.objects.all()

    if not products:
        return Response({"message": "No data found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(products, many=True)
    return Response({"products":serializer.data})


@api_view(['POST'])
def create_product(request):
    """
    Create a new product.
    Returns a JSON response with the created product data and a success message.
    """
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Product created successfully", "data": serializer.data},
                        status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, pk):
    """
    Retrieve, update, or delete a product by its primary key (pk).
    Returns a JSON response based on the requested method.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response({"product": serializer.data}, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product updated successfully", "product": serializer.data},
                            status=status.HTTP_200_OK)
        return Response({"message": "Update failed", "errors": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product deleted successfully"},
                        status=status.HTTP_204_NO_CONTENT)
