import uuid

from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.db import models
from django.urls.base import reverse

# def upload_location_activity_images(instance, filename):
#     file_path = 'the_'+str(filename)
#     return file_path

# def upload_location_activity_images(instance, filename):
#     file_path = 'user/{user_id}/{filename}'.format(
#             user_id     = instance.id,
#             filename    = f"{user_id}.wav"
#         )
#     return file_path

def upload_location_activity_images(instance, filename):
    file_path = 'the_'+str(filename)
    return file_path


class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voice_record = models.FileField(
        upload_to=upload_location_activity_images)
    language = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("core:record_detail", kwargs={"id": str(self.id)})



class Step(models.Model):

    
    page_number            = models.IntegerField(unique =True)
    duration_in_sec        = models.IntegerField(default = 30)
    no_question_to_display = models.IntegerField(default = 1)
    active                 = models.BooleanField( default = True)

    def __str__(self):
        return str(self.page_number)


class Question(models.Model):
    active                      = models.BooleanField( default = True)
    question                    = models.TextField(unique = True)
    display_question_on_page    = models.ForeignKey('Step', on_delete=models.CASCADE, related_name="step_questions")


    def __str__(self):
        return self.question

def upload_location_activity_images(instance, filename):
    file_path = 'user/{user_id}/{filename}'.format(
            session_id  = instance.session_id,
            user_id     = instance.user_id,
            filename    = f"microphone_audio.mp3"
        )
    return file_path
