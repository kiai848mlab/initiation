
from django.db import models
from .members import Member


class Achievement(models.Model):
    """
    Column: 挑戦者, ID_number, 項目, 日付, 確認者
    """

    in_progress = 'IP'
    on_Achieved = 'AC'

    ACHIEVED_CHOICES = [
        (in_progress, 'in Progress'),
        (on_Achieved, 'Achieved!'),
    ]

    # challenger = models.OneToOneField(Member, on_delete=models.CASCADE)  # 外部キー
    achieved = models.CharField(
        # help_text='',
        max_length=2,
        choices=ACHIEVED_CHOICES,
        default=in_progress,
    )
    id_number  = models.PositiveSmallIntegerField(
        # help_text='',
        unique=True,
    )
    small_goal = models.CharField(
        max_length=255,
        # help_text='',
        unique=True,
    )
    clear_date = models.DateField(
        # help_text='',
        auto_now=True,
        blank=True,
        null=True,
    )
    # confirmer  = models.OneToOneField(
    #     Member,
    #     on_delete=models.CASCADE
    # )  # 外部キー
