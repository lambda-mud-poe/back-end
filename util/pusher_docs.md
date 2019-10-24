# The Pusher Implementation Suggestion from the Dashboard

## Frontend

```javascript
    <!DOCTYPE html>
    <head>
    <title>Pusher Test</title>
    <script src="https://js.pusher.com/5.0/pusher.min.js"></script>
    <script>

        // Enable pusher logging - don't include this in production
        Pusher.logToConsole = true;

        var pusher = new Pusher('a251c78f5cdcaf3a85d8', {
        cluster: 'eu',
        forceTLS: true
        });

        var channel = pusher.subscribe('my-channel');
        channel.bind('my-event', function(data) {
        alert(JSON.stringify(data));
        });
    </script>
    </head>
    <body>
    <h1>Pusher Test</h1>
    <p>
        Try publishing an event to channel <code>my-channel</code>
        with event name <code>my-event</code>.
    </p>
    </body>

```

## Backend

```python
    import pusher

    channels_client = pusher.Pusher(
    app_id='886664',
    key='a251c78f5cdcaf3a85d8',
    secret='61033f17623a7fe9080d',
    cluster='eu',
    ssl=True
    )

    channels_client.trigger('my-channel', 'my-event', {'message': 'hello world'})

```
