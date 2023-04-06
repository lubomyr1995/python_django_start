from django.db.models import QuerySet


class AutoParkManager(QuerySet):
    def auto_parks_auth(self, user_id):
        return self.filter(user=user_id)
