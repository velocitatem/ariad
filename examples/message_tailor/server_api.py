from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data for the demonstration
teams_data = {
    "Team A": ["Member1", "Member2", "Member3"],
    "Team B": ["Member4", "Member5", "Member6"],
    "Team C": ["Member7", "Member8", "Member9"]
}

member_preferences_data = {
    "Member1": {"Name": "John", "Preferences": {"Interest": "Cycling", "Topic": "Tour de France"}},
    "Member2": {"Name": "Doe", "Preferences": {"Interest": "Programming", "Topic": "Python"}},
    "Member3": {"Name": "Smith", "Preferences": {"Interest": "Reading", "Topic": "Classical Novels"}},
    # Extend for other members...
}

@app.route('/teams', methods=['GET'])
def get_teams():
    """Endpoint to get the list of teams."""
    return jsonify(list(teams_data.keys()))

@app.route('/members/<team>', methods=['GET'])
def get_members(team):
    """Endpoint to get the list of members in a specific team."""
    if team in teams_data:
        return jsonify(teams_data[team])
    return jsonify([]), 404

@app.route('/preferences/<member>', methods=['GET'])
def get_member_preferences(member):
    """Endpoint to get preferences for a specific member."""
    if member in member_preferences_data:
        return jsonify(member_preferences_data[member])
    return jsonify({}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)