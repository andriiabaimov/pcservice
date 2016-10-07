from django.core.urlresolvers import reverse
from django.db import DatabaseError, transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from .models import Repair
from .utils import check_user


def repair_detail(request, pk):
    request = check_user(request)
    repair = get_object_or_404(Repair, pk=pk)

    return render(request, 'actions/repair_detail.html', {'now': timezone.now()})


@transaction.non_atomic_requests
def posting_repair_status(request, pk, status):
    repair = get_object_or_404(Repair, pk=pk)
    repair.latest_status_change_attempt = timezone.now()
    repair.save()
    try:
        with transaction.atomic():
            repair.status = status
            repair.latest_status_change_success = timezone.now()
            repair.save()
            return HttpResponse('Hooray')
    except DatabaseError:
        return HttpResponse('Sadness', status_code=400)


class RepairListView(ListView):
    model = Repair


class RepairDetailView(DetailView):
    model = Repair


class RepairDeleteView(DeleteView):
    model = Repair


# class RepairResultsView(RepairDetailView):
#     template_name = 'actions/repair_results.html'


class RepairUpdateView(UpdateView):
    model = Repair

    def get_success_url(self):
        return reverse('actions:repair_detail', kwargs={'pk': self.object.pk})
