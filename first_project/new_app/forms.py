from django import froms
from .models import ContactFrom

class Contactf(froms.ModelFrom):
    class Meta:
        model = ContactFrom
        field = "__all__"
