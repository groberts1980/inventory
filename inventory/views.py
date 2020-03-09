from inventory.models import *
from inventory.forms import *

def index(request):
    return render(request, "index.html", {"form" : form})
