import json

from django.db import connection
from rest_framework.decorators import api_view, authentication_classes

from myapp import utils
from myapp.handler import APIResponse
from myapp.models import Classification, Thing, Tag, User, ShopCar
from myapp.serializers import ThingSerializer, ClassificationSerializer, ListThingSerializer, DetailThingSerializer
from myapp.utils import dict_fetchall


@api_view(['POST'])
def create(request):
    payload = json.loads(request.body.decode())

    shop_car = ShopCar.objects.filter(thing_id=payload.get('thing_id'), user_id=payload.get('user_id')).first()
    if not shop_car:
        shop_car = ShopCar()
        shop_car.count = payload.get('count')
    else:
        shop_car.count = shop_car.count + payload.get('count')
    shop_car.thing_id = payload.get('thing_id')
    shop_car.user_id = payload.get('user_id')

    shop_car.save()

    return APIResponse(code=0, msg='操作成功')


@api_view(['GET'])
def query_list(request):
    data = []
    for shop_car in ShopCar.objects.filter(user_id=request.GET.get("userId")[0]):
        thing = Thing.objects.filter(id=shop_car.thing_id).first()
        data.append({
            'thing_id': shop_car.id,
            'count': shop_car.count,
            'title': thing.title,
            'price': thing.price,
            'cover': thing.cover.url,
            'selected': False
        })

    return APIResponse(code=0, msg='操作成功', data=data)
