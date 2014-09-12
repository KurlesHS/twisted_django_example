from django.db import models


class EmailSettings(models.Model):
    pass


class MainSettings(models.Model):
    class Meta:
        app_label = 'main'
    audio_folder = models.FilePathField(max_length=0x200, allow_files=False, allow_folders=True)
    script_folder = models.FilePathField(max_length=0x200, allow_files=False, allow_folders=True)
    service_port = models.IntegerField()

    def __str__(self):
        return u'Settings'


class UskSettings(models.Model):
    usk_number = models.IntegerField()

    def __str__(self):
        return u'USK Settings'


class UskScriptModelEntry(models.Model):
    class Meta:
        db_table = 'script'

    name = models.CharField(max_length=0x100)

    def __str__(self):
        return u'Script: %s' % self.name


class EventVariableModelEntry(models.Model):
    class Meta:
        db_table = "event_var"
    name = models.CharField(max_length=32)
    value = models.CharField(max_length=0x0400)

    def __str__(self):
        return u'Event Var: %s' % self.name


class EventModelEntry(models.Model):
    class Meta:
        db_table = "event"

    description = models.CharField(max_length=0x100)
    script = models.ForeignKey(UskScriptModelEntry)
    event_id = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=32)
    variables = models.ManyToManyField(EventVariableModelEntry)

    def __str__(self):
        return u'Event: %s' % self.description


class EventIncomingSmsModelEntry(EventModelEntry):
    class Meta:
        db_table = "event_sms"
    modem = models.CharField(max_length=32)