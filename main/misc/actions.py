from rest_framework.parsers import JSONParser

def handle_post(request, Serializer):
    data = JSONParser().parse(request)
    serializer = Serializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return True, serializer.data
    return False, serializer.errors

def handle_get_by_name(Serializer, key_val):
    result = dict()
    for idx, obj in enumerate(Serializer.objects.filter(name = key_val).values(), 1):
        result[idx] = obj
    return result

def handle_patch(request, Serializer, obj):
    data = JSONParser().parse(request)
    serializer = Serializer(obj, data = data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return True, serializer.data
    return False, serializer.errors

def handle_delete(request):
    pass