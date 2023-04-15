from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name='Menu name')

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=100)

    parent = models.ForeignKey('MenuItem', blank=True, default=None, null=True, on_delete=models.CASCADE,
                               verbose_name='Linked parent'
                               )

    href = models.CharField(max_length=200, blank=True, default=None, null=True,
                            verbose_name='Link to referred page (in priority)'
                            )

    named_url = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default=None,
        verbose_name='Link name to page'
    )

    menu = models.ForeignKey(
        'Menu',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        verbose_name='Related menu'
    )

    class Meta:
        ordering = ['menu', 'id']

    def __str__(self) -> str:
        return self.title
