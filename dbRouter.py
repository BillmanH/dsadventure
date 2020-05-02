# DB router for game
# if 'game_db' not in settings.DATABASES:
class gameDBRouter(object):
    """
    A router to control game db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on app models to 'game_db'"
        from django.conf import settings
        if 'game_db' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'game':
            return 'game_db'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on game models to 'game_db'"
        from django.conf import settings
        if 'game_db' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'game':
            return 'game_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in game is involved"
        from django.conf import settings
        if 'game_db' not in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'game' or obj2._meta.app_label == 'game':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the game app only appears on the 'game' db"
        from django.conf import settings
        if 'game_db' not in settings.DATABASES:
            return None
        if db == 'game_db':
            return model._meta.app_label == 'game'
        elif model._meta.app_label == 'game':
            return False
        return None