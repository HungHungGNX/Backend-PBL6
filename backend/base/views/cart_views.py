from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Product, Cart, CartItem
from base.serializers import CartSerializer

from rest_framework import status
from datetime import datetime




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCartItems(request):
    user = request.user
    data = request.data

    cartItems = data['cartItems']

    if cartItems and len(cartItems) == 0:
        return Response({'detail': 'No Cart Items'}, status=status.HTTP_400_BAD_REQUEST)
    else:

        # (1) Create cart
        cart = Cart.objects.create(
            user=user,
            totalPrice=data['totalPrice']
        )

        # (3) Create cart items adn set cart to cartItem relationship
        for i in cartItems:
            product = Product.objects.get(_id=i['product'])

            item = CartItem.objects.create(
                product=product,
                cart=cart,
                name=product.name,
                qty=i['qty'],
                price=i['price'],
                image=product.image.url,
            )


        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCart(request, pk):
    cart = Cart.objects.get(_id=pk)
    cart.delete()
    return Response('Cart Deleted')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCarts(request):
    user = request.user
    carts = user.cart_set.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCart(request, pk):
     cart = Cart.objects.get(_id=pk)
     data = request.data['product']
     product = Product.objects.get(_id=data['product'])
    
     CartItem.objects.create(
                product=product,
                cart=cart,
                name=product.name,
                qty=i['qty'],
                price=i['price'],
                image=product.image.url,
            )

     return Response('Add item cart')



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCartItems(request, pk):
    cartItem = Cart.objects.get(_id=pk)
    cartItem.delete()
    return Response('Cart remove item')