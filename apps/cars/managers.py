from django.db.models import QuerySet


class CarManager(QuerySet):
    def cars_by_auto_park_id(self, _id):
        return self.filter(auto_park_id=_id)
