from django.db import models

# Create your models here.


class Skill(models.Model):
    pass

class Questions(models.Model):
    _content=models.TextField()
    """Type of question 0=(detail answer)  1=(Yes/No) 2< number of options   """
    type=models.IntegerField ()
    hardness = models.IntegerField()



class Test(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()




class SkillTest(models.Model):

    skill=models.ForeignKey(Skill)

    test=models.ForeignKey(Test)



class TestQuestion(models.Model):
    question= models.ForeignKey(Questions)
    test= models.ForeignKey(Test)

