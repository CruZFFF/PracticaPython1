import requests

TOKEN = 'M2NhNzFiYmUtMWVkYy00MzZhLWI4OWUtZWIwYTZmYzAyNzNhMGMwY2Y4ZDgtYjAx_P0A1_e5840657-a59b-4c71-a507-6ac685cd8fcf'
ROOM = 'Programación de redes 2023'
HEADERS = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}

def get_room_id(name):
    r = requests.get('https://webexapis.com/v1/rooms', headers=HEADERS)
    return next((room['id'] for room in r.json()['items'] if room['title'] == name), None)

def send_message(room_id, text):
    r = requests.post('https://webexapis.com/v1/messages', headers=HEADERS, json={'roomId': room_id, 'text': text})
    print(" Mensaje enviado." if r.status_code == 200 else f"Error: {r.text}")

def get_messages(room_id, max=5):
    r = requests.get(f'https://webexapis.com/v1/messages?roomId={room_id}&max={max}', headers=HEADERS)
    for m in r.json().get('items', []): print(f"- {m['personEmail']}: {m.get('text', '[sin texto]')}")

if __name__ == '__main__':
    room_id = get_room_id(ROOM)
    if room_id:
        send_message(room_id, input("Escribe tu mensaje: "))
        get_messages(room_id)
    else:
        print("Room no encontrado.")
