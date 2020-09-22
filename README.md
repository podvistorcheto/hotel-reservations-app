
--------

Happy coding!

Creating Data in the shell with SQL:

gitpod /workspace/hotel-reservations-app $ python manage.py shell
Python 3.8.5 (default, Sep  9 2020, 09:09:42) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from hotel.models import Room

In [2]: from django.contrib.auth.models import User

In [3]: User.objects.all()
Out[3]: <QuerySet [<User: dsd>, <User: TestUser>]>

In [4]: User.objects.first()
Out[4]: <User: dsd>

In [5]: User.objects.filter(username="dsd")
Out[5]: <QuerySet [<User: dsd>]>

In [6]: User.objects.filter(username="dsd").first()
Out[6]: <User: dsd>

In [7]: user = User.objects.filter(username="dsd").first()

In [8]: user
Out[8]: <User: dsd>

In [9]: user.id
Out[9]: 1

In [10]: user.pk
Out[10]: 1

In [11]: user = User.object.get(id=1)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-11-95ded9d8c819> in <module>
----> 1 user = User.object.get(id=1)

AttributeError: type object 'User' has no attribute 'object'

In [12]: user = User.objects.get(id=1)

In [13]: user
Out[13]: <User: dsd>

In [14]: Room.objects.all()
Out[14]: <QuerySet [<Room: 1001. twin with 2 beds for 2 adults and 0 children>]>

In [15]: room_2 = Post(number="1002", category="Double Room", bed=2, capacity=2, childred_capacity=0)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-15-e779e3ae4213> in <module>
----> 1 room_2 = Post(number="1002", category="Double Room", bed=2, capacity=2, childred_capacity=0)

NameError: name 'Post' is not defined

In [16]: room_2 = Room(number="1002", category="Double Room", bed=2, capacity=2, childred_capacity=0)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-ce211af43e1c> in <module>
----> 1 room_2 = Room(number="1002", category="Double Room", bed=2, capacity=2, childred_capacity=0)

/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/base.py in __init__(self, *args, **kwargs)
    499                     pass
    500             for kwarg in kwargs:
--> 501                 raise TypeError("%s() got an unexpected keyword argument '%s'" % (cls.__name__, kwarg))
    502         super().__init__()
    503         post_init.send(sender=cls, instance=self)

TypeError: Room() got an unexpected keyword argument 'bed'

In [17]: room_2 = Room(number="1002", category="Double Room", beds=2, capacity=2, children_capacity=0)

In [18]: Room.objects.all()
Out[18]: <QuerySet [<Room: 1001. twin with 2 beds for 2 adults and 0 children>]>

In [19]: room_2.save()

In [20]: Room.objects.all()
Out[20]: <QuerySet [<Room: 1001. twin with 2 beds for 2 adults and 0 children>, <Room: 1002. Double Room with 2 beds for 2 adults and 0 children>]>

In [21]: room_3 = Room(number="1003", category="Family Room", beds=3, capacity=2, children_capacity=1)

In [22]: room_3.save()

In [23]: Room.objects.all()
Out[23]: <QuerySet [<Room: 1001. twin with 2 beds for 2 adults and 0 children>, <Room: 1002. Double Room with 2 beds for 2 adults and 0 children>, <Room: 1003. Family Room with 3 beds for 2 adults and 1 children>]>

In [24]: user
Out[24]: <User: dsd>

In [25]: room_4 = Room(number="1004", category="Deluxe Suite", beds=3, capacity=2, children_capacity=1)

In [26]: room_4.save()

In [27]: room_5 = Room(number="1005", category="Apartment", beds=4, capacity=2, children_capacity=2)

In [28]: room_5.save()

In [29]: Room.objects.all()
Out[29]: <QuerySet [<Room: 1001. twin with 2 beds for 2 adults and 0 children>, <Room: 1002. Double Room with 2 beds for 2 adults and 0 children>, <Room: 1003. Family Room with 3 beds for 2 adults and 1 children>, <Room: 1004. Deluxe Suite with 3 beds for 2 adults and 1 children>, <Room: 1005. Apartment with 4 beds for 2 adults and 2 children>]>

In [30]: room_6 = Room(number="1006", category="Deluxe Apartment", beds=4, capacity=2, children_capacity=2)

In [31]: room_6.save()

In [32]: 