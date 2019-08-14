from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Pairs
from .serializers import PairSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the RomanToArabic index.")


def value(r):
    if r in "IVXLDM":
        for result in Pairs.objects.raw("SELECT id, arabic FROM roman_to_arabic_pairs WHERE roman = %s", r):
            return result.arabic
    return -1


def romanToDecimal(str):
    res = 0
    i = 0

    while (i < len(str)):
        # Getting value of symbol s[i]
        s1 = value(str[i])

        if (i + 1 < len(str)):

            # Getting value of symbol s[i+1]
            s2 = value(str[i + 1])

            # Comparing both values
            if (s1 >= s2):

                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:

                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res


@api_view(['POST'])
def converter(request):
    roman = request.data.get("roman")
    print("roman:", roman)
    arabic = romanToDecimal(roman)
    print("arabic:", arabic)
    return HttpResponse(arabic)


class PairView(viewsets.ModelViewSet):
    queryset = Pairs.objects.all()
    serializer_class = PairSerializer
