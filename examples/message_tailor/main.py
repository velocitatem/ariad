import data_access
from personalization_engine import generate_personalized_message
from integration_layer import send_personalized_message

# Retrieve teams
teams = data_access.get_teams()

target_team = "Team A"
info_message = "We need to finish the project by the end of the week."

# Retrieve members of the target team
members = data_access.get_members(target_team)

# Send a message to each member of the target team
for member in members:
    # Retrieve member preferences
    member_preferences = data_access.get_member_preferences(member)

    # Generate a personalized message based on the member preferences
    personalized_message = generate_personalized_message(member_preferences, info_message)

    # Send the personalized message to the member
    send_personalized_message(member, personalized_message)
