from django.contrib.auth.models import Group
my_group = Group.objects.get(name='my_group_name')
my_group.user_set.add(your_user)
