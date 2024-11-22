from .models import LineGroup
from app.events.models import Event
from app.members.models import Member

def add_all_line_users_in_line_group_to_event(line_group: LineGroup, event: Event) -> None:
    line_users_in_group = line_group.line_users_in_group
    for line_user in line_users_in_group:
        member = Member(line_user.line_user_name, event.event_id)
        event.add_member(member)