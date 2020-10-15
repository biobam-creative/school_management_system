from django.shortcuts import render
from django.contrib.auth.models import User
from registration . models import Student
from .models import Csv
from .forms import CsvForm
from django.db.models import Q
import csv


def result(request):
    if request.method == "GET":
        form = CsvForm()
        return render(request, 'exams_results/result.html', {'form': form})
    else:
        form = CsvForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            my_form = form.save(commit=False)
            my_form.uploaded_by = request.user
            my_form.save()
            obj = Csv.objects.get(activated=False)
            with open(obj.csv.path, 'r')as f:
                reader = csv.reader(f)

                for i, row in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                        student = int(row[2])
                        term = row[3]
                        session = row[4]
                        first_ca = int(row[5])
                        second_ca = int(row[6])
                        third_ca = int(row[7])
                        exam = int(row[8])
                        subject = row[9]
                        print(student, term, session, subject,
                              first_ca, second_ca, third_ca, exam)

                obj.activated = True
                obj.save()
        return render(request, 'exams_results/result.html', {'form': form})
