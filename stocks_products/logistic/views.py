from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer

#
# class ProductsList(ListAPIView):
#     model = Product
#     serializer_class = ProductSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ["title", "description"]
#
#     def get_queryset(self):
#         stock = self.request.stock
#         return stock.stocks_set.all()


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class StockViewSet(ModelViewSet):
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    search_fields = ["id", "products", "address"]

    def get_queryset(self):
        queryset = Stock.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset