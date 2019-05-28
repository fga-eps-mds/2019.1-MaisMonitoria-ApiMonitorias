from django.db import models


class Like(models.Model):
    id_like = models.AutoField(primary_key=True)
    user_that_likes = models.ForeignKey("user_account.UserAccount", on_delete=models.CASCADE, related_name='user_that_likes')
    tutoring_session = models.ForeignKey("tutoring_session.TutoringSession", on_delete=models.CASCADE, related_name='tutoring_session')
    create_date = models.DateTimeField(auto_now_add=True)