from django.db import models
from periodic_table.models import Element
from simulations.models import Material
from users.models import StudentProfile

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='quizzes', on_delete=models.CASCADE)
    question = models.TextField()
    options = models.JSONField(help_text="Provide a list of strings options")
    correct_option_index = models.IntegerField()
    xp_reward = models.IntegerField(default=10)

    def __str__(self):
        return f"Quiz for {self.lesson.title}"

class StudentProgress(models.Model):
    student = models.ForeignKey(StudentProfile, related_name='progress', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.lesson.title}"
