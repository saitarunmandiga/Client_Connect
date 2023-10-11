from collections import UserDict
from pyexpat import model

from sklearn import model_selection


class UserPreference:
    """
    Model to store user preferences.
    (Assuming a SQL-based database like SQLite or MySQL for simplicity)
    """
    user_id = model_selection.ForeignKey(UserDict, on_delete=model.CASCADE)
    widget_order = models.TextField()  # A JSON string containing order of widgets.
    widget_visibility = models.TextField()  # A JSON string containing visibility of widgets.
