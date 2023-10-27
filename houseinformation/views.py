
from django.http import JsonResponse


def get_house_info(request):
    address = request.GET.get('address')
    num_floors = int(request.GET.get('num_floors'))
    floor_names = request.GET.get.getlist('floor names[]')
    num_rooms = int(request.GET.get('num_rooms'))
    room_links = request.GET.get.getlist

    response = {
        'floor_image1': 'path/to/image1.png',
        'floor_image2': 'path/to/image2.png',
        'house_name': ' PPK SGTU ',

    }
    return JsonResponse(response)
