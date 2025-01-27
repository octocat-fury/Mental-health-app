from django.db import models
class User(models.Model):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    def _str_(self):
        return self.username
class JournalEntry(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    entry_text = models.TextField()
    entry_image = models.ImageField(upload_to='journal_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Journal Entry {self.id}"




from django.db import models
class AnxietyTestResponse(models.Model):
    # Fields to store user's responses to each question
    q1 = models.IntegerField("I feel nervous, anxious, or on edge.", choices=[(i, i) for i in range(5)])
    q2 = models.IntegerField("I worry too much about different things.", choices=[(i, i) for i in range(5)])
    q3 = models.IntegerField("I have trouble relaxing.", choices=[(i, i) for i in range(5)])
    q4 = models.IntegerField("I feel easily annoyed or irritable.", choices=[(i, i) for i in range(5)])
    q5 = models.IntegerField("I feel afraid, as if something awful might happen.", choices=[(i, i) for i in range(5)])
    q6 = models.IntegerField("My heart races or pounds without any reason.", choices=[(i, i) for i in range(5)])
    q7 = models.IntegerField("I have difficulty concentrating on tasks.", choices=[(i, i) for i in range(5)])
    q8 = models.IntegerField("I feel tension in my muscles or body.", choices=[(i, i) for i in range(5)])
    q9 = models.IntegerField("I feel faint or lightheaded without reason.", choices=[(i, i) for i in range(5)])
    q10 = models.IntegerField("I avoid situations that make me anxious.", choices=[(i, i) for i in range(5)])

    # Total score and anxiety level
    total_score = models.IntegerField("Total Score", default=0)
    anxiety_level = models.CharField("Anxiety Level", max_length=50, default="Not Evaluated")

    # Timestamp for when the test was taken
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_score_and_level(self):
        """
        Calculates the total score and determines the anxiety level based on the score.
        """
        self.total_score = (
                self.q1 + self.q2 + self.q3 + self.q4 + self.q5 +
                self.q6 + self.q7 + self.q8 + self.q9 + self.q10
        )
        if self.total_score <= 15:
            self.anxiety_level = "Not Anxious"
        elif self.total_score <= 30:
            self.anxiety_level = "Mildly Anxious"
        else:
            self.anxiety_level = "Highly Anxious"
        self.save()

    def __str__(self):
        return f"Anxiety Test taken on {self.created_at} - Level: {self.anxiety_level}"

# Create your models here.
