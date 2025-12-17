from rest_framework import serializers
from .models import Order , OrderItem

class OrderItemSerializer(serializers.ModelsSerilaizer):
    class Meta:
        model = OrderItem
        field =['id', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields= [
            'id', 
            'order_number',
            'created_at',
            'total_price',
            'items'
        ]