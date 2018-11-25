from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Quiz(models.Model):
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField('date published')
    quiz_name = models.CharField(max_length=50)
    quiz_title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    instructions = models.CharField(max_length=2000)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=50)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return "%s : %s" % (self.question_name, self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_name = models.CharField(max_length=50)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.choice_name
