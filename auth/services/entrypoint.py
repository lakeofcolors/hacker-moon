from django.contrib.gis.geoip2 import GeoIP2
from users.models import EntryPoint

def create_entry_point(user: object, remote_addr: str) -> bool:

    entry_point = EntryPoint(
        user = user,
        remote_address = remote_addr,
    )

    try:
        geo = GeoIP2()
        data = geo.city(remote_addr)
    except:
        entry_point.save()
        return True

    entry_point.country = data["country_name"]
    entry_point.city = data["city"]

    entry_point.save()

    return True
