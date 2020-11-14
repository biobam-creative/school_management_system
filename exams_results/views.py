from django.shortcuts import render
from django.contrib.auth.models import User
from registration . models import Student, StudentClass
from .models import Csv, Result
from .forms import CsvForm, TermForm
from django.db.models import Q
import csv
from django.contrib.auth.decorators import login_required


@login_required
def result(request):
    if request.method == "GET":
        form = CsvForm()
        return render(request, 'exams_results/result.html', {'form': form})
    else:
        form = CsvForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form)
            my_form = form.save(commit=False)
            my_form.uploaded_by = request.user.teacher
            my_form.save()
            obj = Csv.objects.get(activated=False)
            with open(obj.csv.path, 'r')as f:
                reader = csv.reader(f)

                for i, row in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                        student = Student.objects.get(id=int(row[2]))
                        term = row[3]
                        session = row[4]
                        first_ca = int(row[5])
                        second_ca = int(row[6])
                        third_ca = int(row[7])
                        exam = int(row[8])
                        subject = row[9]
                        student_class = row[10]
                        total = first_ca + second_ca + third_ca + exam
                        if total >= 70:
                            remark = 'Excellent'
                            grade = 'A1'
                        elif total >= 60:
                            remark = 'Very Good'
                            grade = 'B2'
                        elif total >= 50:
                            remark = 'Good'
                            grade = 'C4'
                        elif total >= 45:
                            remark = 'CREDIT'
                            grade = 'C5'
                        elif total >= 40:
                            remark = 'CREDIT'
                            grade = 'C6'
                        elif total >= 35:
                            remark = 'PASS'
                            grade = 'D7'
                        elif total >= 30:
                            remark = 'PASS'
                            grade = 'E8'
                        else:
                            remark = 'FAIL'
                            grade = 'F9'
                        Result.objects.create(student=student, term=term, session=session,
                                              first_ca=first_ca, second_ca=second_ca, third_ca=third_ca, exam=exam, subject=subject, total=total, remark=remark, grade=grade, student_class=student_class)
                        print(student, term, session, subject,
                              first_ca, second_ca, third_ca, exam, grade, remark)

                obj.activated = True
                obj.save()
                message = "Uploaded Successfully"
                return render(request, 'exams_results/result.html', {'message': message, 'form': form})
        return render(request, 'exams_results/result.html', {'form': form})


@login_required
def report_card(request):
    if request.method == "GET":
        students = Student.objects.filter(user=request.user,)
        form = TermForm()
        return render(request, 'exams_results/report_card.html', {'form': form, 'students': students, })
    else:
        students = Student.objects.filter(user=request.user,)
        principal = User.objects.filter(is_superuser=True)
        form = TermForm(request.POST)
        if form.is_valid():
            term = form.cleaned_data['term']
            #session = form.cleaned_data['session']
            input_class = form.cleaned_data['student_class']
            student_class = StudentClass.objects.filter(title=input_class)[0]
            score = Result.objects.filter(
                student=request.user.student,  term=term, student_class=student_class)
            session = score.values('session')
            for session in session:
                session = (session['session'])
# first C.A total
        first_cas = score.values('first_ca')
        first_ca_list = []
        for first_ca in first_cas:
            first_cas = first_ca['first_ca']
            first_ca_list.append(first_cas)
        first_ca_total = (sum(first_ca_list))

# second C.A total
        second_cas = score.values('second_ca')
        second_ca_list = []
        for second_ca in second_cas:
            second_cas = second_ca['second_ca']
            second_ca_list.append(second_cas)
        second_ca_total = (sum(second_ca_list))

# third C.A total
        third_cas = score.values('third_ca')
        third_ca_list = []
        for third_ca in third_cas:
            third_cas = third_ca['third_ca']
            third_ca_list.append(third_cas)
        third_ca_total = (sum(third_ca_list))

# exam total
        exams = score.values('exam')
        exam_list = []
        for exam in exams:
            exams = exam['exam']
            exam_list.append(exams)
        exam_total = (sum(exam_list))

# grand total
        totals = score.values('total')
        my_total = []
        for t in totals:
            totals = t['total']
            my_total.append(totals)
        grand_total = (sum(my_total))

        context = {
            'score': score,
            'form': form,
            'students': students,
            'principal': principal,
            'grand_total': grand_total,
            'first_ca_total': first_ca_total,
            'second_ca_total': second_ca_total,
            'third_ca_total': third_ca_total,
            'exam_total': exam_total,
            'session': session,
            'term': term,
            'student_class': student_class
        }

        return render(request, 'exams_results/report_card.html', context)
    return render(request, 'exams_results/form.html')
