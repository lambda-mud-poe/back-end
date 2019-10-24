# Lambda CS MUD Game Backend

## Endpoints

### Registration[POST]

curl -X POST -H "Content-Type: application/json" -d '{"username":"thunder", "password1":"testpassword", "password2":"testpassword"}' localhost:8000/api/registration/

#### Response

```json
    {"key":"abba6538c2ad559860ed87e5f6d6ed54ab5da56f"}
```

### Login[POST]

curl -X POST -H "Content-Type: application/json" -d '{"username":"thunder", "password":"testpassword"}' localhost:8000/api/login/

#### Response

```json
    {"key":"abba6538c2ad559860ed87e5f6d6ed54ab5da56f"}
```

### Initialize[GET]

curl -X GET -H 'Authorization: Token abba6538c2ad559860ed87e5f6d6ed54ab5da56f' localhost:8000/api/init/

#### Response

```json
    {"uuid": "2139cccb-1c90-4d96-9bfb-523c18ea77cc", "name": "thunder", "x": 0, "y": 0, "room_id": 1, "title": "Outside Cave Entrance", "description": "The quest for thy nobly ring burns true and bright. Search on thou famed voyager!", "players": ["oyekunle", "alum", "user", "testuser", "testuserXaa", "testuserXX"]}
```

### Move[POST]

curl -X POST -H 'Authorization: Token abba6538c2ad559860ed87e5f6d6ed54ab5da56f' -H "Content-Type: application/json" -d '{"direction":"e"}' localhost:8000/api/move/

#### Response

```json
    {"name": "thunder", "x": 1, "y": 0, "room_id": 2, "title": "Plain Garden Thicket", "description": "The quest for thy nobly ring burns true and bright. Search on thou famed voyager!", "players": [], "error_msg": ""}
```

    - Pusher broadcast (stretch):
        - Players in previous room receive a message: thunder has walked east.
        - Players in next room receive a message: thunder has entered from the west.
