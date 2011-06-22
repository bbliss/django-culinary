from django.db import models

class MenuCategory(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    description=models.TextField(blank=True)
    
    def menu_items(self):
        return MenuItem.objects.filter(category=self)
    
    def __unicode__(self):
        return self.title

class MenuItem(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(MenuCategory)
    image=models.ImageField(upload_to='culinary/menuitems', blank=True)
    description=models.TextField()
    
    spicyness=models.IntegerField(default=0)
    goes_well_with=models.ForeignKey('self', blank=True, null=True)
    
    healthy_choice=models.BooleanField(default=False)
    gluten_free=models.BooleanField(default=False)
    low_carb=models.BooleanField(default=False)
    vegan=models.BooleanField(default=False)
    
    price=models.CharField(max_length=10)
    price_with_combo=models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.title

class Special(models.Model):
    menu_item=models.ForeignKey(MenuItem)
    auto=models.BooleanField(default=False)
    weekday=models.CharField(max_length=10, blank=True, choices=[
        ('mon', 'Monday'), 
        ('tue', 'Tuesday'), 
        ('wed','Wednesday'), 
        ('thu', 'Thursday'), 
        ('fri','Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ])
    after_time=models.TimeField(blank=True)
    until_time=models.TimeField(blank=True)
    
    after_date=models.DateField(blank=True)
    until_date=models.DateField(blank=True)
    
    def __unicode__(self):
        return "Special for " + self.menu_item