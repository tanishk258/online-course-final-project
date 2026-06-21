```python
from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, Enrollment, Submission, Choice


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    enrollment = Enrollment.objects.get(
        user=request.user,
        course=course
    )

    submission = Submission.objects.create(
        enrollment=enrollment
    )

    choices = request.POST.getlist('choice')

    for choice_id in choices:
        choice = Choice.objects.get(pk=int(choice_id))
        submission.choices.add(choice)

    submission.save()

    return redirect(
        'onlinecourse:show_exam_result',
        course_id=course.id,
        submission_id=submission.id
    )


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)

    submission = get_object_or_404(
        Submission,
        pk=submission_id
    )

    total_score = 0
    possible_score = 0

    for question in course.question_set.all():
        possible_score += question.grade

        selected_choices = submission.choices.filter(
            question=question
        )

        if question.is_get_score(selected_choices):
            total_score += question.grade

    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score,
    }

    return render(
        request,
        'onlinecourse/exam_result_bootstrap.html',
        context
    )
```
