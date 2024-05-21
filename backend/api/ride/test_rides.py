from .models import Ride
import pytest
import random

@pytest.mark.django_db
def test_create_new_ride():
    test_ride = Ride.objects.create(
      user_initiator="pra",
      src_location="sadar",
      dst_location="college",
      total_fare=250,
      num_passengers=5,
      start_datetime="2006-10-25T14:34:59Z"
    )
    assert Ride.objects.count() == 1

@pytest.mark.django_db
def test_change_no_of_passengers():
    test_ride = Ride.objects.create(
      user_initiator="pra",
      src_location="sadar",
      dst_location="college",
      total_fare=250,
      num_passengers=5,
      start_datetime="2006-10-25T14:34:59Z"
    )
    new_passengers_cnt=random.randint(1,15)
    test_ride.num_passengers=new_passengers_cnt
    test_ride.save()

    updated_ride=Ride.objects.get(id=test_ride.id)
    assert updated_ride.num_passengers == new_passengers_cnt
