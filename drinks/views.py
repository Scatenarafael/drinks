from django.http import JsonResponse
from drinks.models import Drink
from drinks.serializers import DrinkSerializer


def drink_list(request):
  # get all the drinks
  # serialize them
  # return json
  
  drinks = Drink.objects.all()
  serializer = DrinkSerializer(drinks, many=True)
  return JsonResponse(serializer.data, safe=False)