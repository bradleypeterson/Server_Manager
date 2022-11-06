from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from .forms import GroupForm


# Create your views here.
def createGroup(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('profHome')
            except:
                pass
    else:
        form = GroupForm()
        return render(request, 'group/createGroup.html', {'form': form})


def groupDetail(request, id):
    group = get_object_or_404(Group, pk=id)
    return render(request, "group/groupDetail.html", {"group": group})
