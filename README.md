# Lambda CS MUD Game Backend

This is the backend of the Lambda MUD game. 🎮

It is built with Python 🐍, Django, a SQLite database in development and PostgreSQL database in production.

Multiple users can play the game simultaneously. Pusher is used to provide real-time communication 🔈 so players can communicate during the game and get information about the position of other players.

## Frontend 💻

The frontend is built with React and can be found [here](https://mud-mount-doom.herokuapp.com/)

## Endpoints

### Registration[POST]

#### Request

```
curl -X POST -H "Content-Type: application/json" -d '{"username":"thunder", "password1":"testpassword", "password2":"testpassword"}' https://mount-doom-mud.herokuapp.com/api/registration/
```

#### Response

```json
{"key":"abba6538c2ad559860ed87e5f6d6ed54ab5da56f"}
```

### Login[POST]

#### Request

```
curl -X POST -H "Content-Type: application/json" -d '{"username":"thunder", "password":"testpassword"}' https://mount-doom-mud.herokuapp.com/api/login/
```

#### Response

```json
{"key":"abba6538c2ad559860ed87e5f6d6ed54ab5da56f"}
```

### Initialize[GET]

#### Request

```
curl -X GET -H 'Authorization: Token abba6538c2ad559860ed87e5f6d6ed54ab5da56f' https://mount-doom-mud.herokuapp.com/api/init/
```

#### Response

```json
{"uuid": "2139cccb-1c90-4d96-9bfb-523c18ea77cc", "name": "thunder", "x": 0, "y": 0, "room_id": 1, "title": "Outside Cave Entrance", "description": "The quest for thy nobly ring burns true and bright. Search on thou famed voyager!", "players": ["oyekunle", "alum", "user", "testuser", "testuserXaa", "testuserXX"]}
```

### Move[POST]

#### Request

```
curl -X POST -H 'Authorization: Token abba6538c2ad559860ed87e5f6d6ed54ab5da56f' -H "Content-Type: application/json" -d '{"direction":"e"}' https://mount-doom-mud.herokuapp.com/api/move/
```

#### Response

```json
{"name": "thunder", "x": 1, "y": 0, "room_id": 2, "title": "Plain Garden Thicket", "description": "The quest for thy nobly ring burns true and bright. Search on thou famed voyager!", "players": [], "error_msg": ""}
```

##### Pusher broadcast

- Players in previous room receive a message: thunder has walked east.
- Players in next room receive a message: thunder has entered from the west.

### Say[POST]

#### Request

```
curl -X POST -H 'Authorization: Token abba6538c2ad559860ed87e5f6d6ed54ab5da56f' -H "Content-Type: application/json" -d '{"message":"Hello, world!"}' https://mount-doom-mud.herokuapp.com/api/say/
```

#### Response

```json
{"message": "Message: Hello, world! by player thunder has been broadcast successfully."}
```

##### Pusher broadcast

- Players in current room receive a message: thunder says "Hello, world!"

## Loading the server

### Set up a Pusher account

- Sign up for a free account on pusher.com
- Create a new app
- Take note of your credentials app_id, key, secret, cluster
- Look through the provided sample code and documentation

### Set up your local server

#### Set up your virtual environment

- pipenv --three
- pipenv install
- pipenv shell

#### Add your secret credentials

- Create .env in the root directory of your project
- Add your pusher credentials and secret key

```
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL="sqlite:///db.sqlite3"
SECRET_KEY='<your_secret_key>'
DEBUG=True
PUSHER_APP_ID=<your_app_id>
PUSHER_APP_KEY=<your_pusher_key>
PUSHER_APP_SECRET=<your_pusher_secret>
PUSHER_CLUSTER=<your_pusher_cluster>
```

### Run database migrations

- ./manage.py makemigrations
- ./manage.py migrate

### Add rooms to your database

- ./manage.py shell
- Copy/paste the contents of util/mount_doom_init.py into the Python interpreter
- Exit the interpreter

### Run the server

- ./manage.py runserver
