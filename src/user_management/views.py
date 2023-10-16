import dbm
from flask import Flask, jsonify, request

from user_management.dashboard_models import UserPreference

app = Flask(__name__)

@app.route('/getPreferences/<int:user_id>', methods=['GET'])
def get_preferences(user_id):
    preferences = UserPreference.query.filter_by(user_id=user_id).first()
    return jsonify(preferences)

@app.route('/savePreferences', methods=['POST'])
def save_preferences():
    data = request.json
    user_id = data.get('user_id')
    preferences = UserPreference.query.filter_by(user_id=user_id).first()
    
    preferences.widget_order = data.get('widget_order')
    preferences.widget_visibility = data.get('widget_visibility')
    
    # Save the updated preferences
   
    # to the database
    dbm.session.commit()

    return jsonify({"status": "success", "message": "Preferences saved successfully!"}), 200
