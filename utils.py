from rest_framework.response import Response







def sendresponse(message, status_code, data=None, **kwargs):
    if data == None:
        return Response(
            {"message": message, **kwargs},
            status=status_code,
        )
    else:
        return Response(
            {"data": data, "message": message, **kwargs},
            status=status_code,
        )