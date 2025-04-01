import json
from commands import get_status, send_data

COMMANDS = {
    "get_status": get_status,
    "send_data": send_data
}

def handle_request(data):
    try:
        request = json.loads(data)
        command = request.get("command")

        if command in COMMANDS:
            response = COMMANDS[command](request.get("data"))
            return json.dumps({"status": "ok", "response": response})
        
        return json.dumps({"status": "error", "message": "Unknown command"})
    
    except json.JSONDecodeError:
        return json.dumps({"status": "error", "message": "Invalid JSON"})
