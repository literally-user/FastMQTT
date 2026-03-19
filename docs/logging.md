# Logging

## Logger hierarchy

fastmqtt uses the standard `logging` module with the following logger names:

```
fastmqtt
  ├── fastmqtt.transport
  ├── fastmqtt.protocol
  └── fastmqtt.client
```

Configure any of these with the standard `logging` API.

## Enabling logging

The simplest way to see all library output:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

For production, configure only the loggers you care about:

```python
import logging
logging.getLogger("fastmqtt.client").setLevel(logging.WARNING)
logging.getLogger("fastmqtt.protocol").setLevel(logging.DEBUG)
```

## No-handlers policy

fastmqtt never installs handlers and never calls `logging.basicConfig()`. Your application controls all formatting, destinations, and log levels. The library only emits records — what happens to them is entirely up to you.

## What DEBUG output looks like

At `DEBUG` level, the protocol layer logs every packet sent and received:

```
DEBUG fastmqtt.protocol  → CONNECT client_id='' clean_session=True keepalive=60
DEBUG fastmqtt.protocol  ← CONNACK session_present=False return_code=0
DEBUG fastmqtt.protocol  → SUBSCRIBE filters=['sensors/#']
DEBUG fastmqtt.protocol  ← SUBACK return_codes=[0]
DEBUG fastmqtt.protocol  ← PUBLISH topic='sensors/temp' qos=0 retain=False
DEBUG fastmqtt.protocol  → PINGREQ
DEBUG fastmqtt.protocol  ← PINGRESP
DEBUG fastmqtt.protocol  → DISCONNECT
```

At `INFO` level the client layer logs reconnection events:

```
WARNING fastmqtt.client  Connection lost, reconnecting in 1.0s
INFO    fastmqtt.client  Successfully reconnected
```

Duplicate-filter warnings come from `fastmqtt.protocol` (see [Subscribing — Duplicate-filter guard](subscribing.md#duplicate-filter-guard)):

```
WARNING fastmqtt.protocol  Filter 'data/temp' already registered; skipping duplicate
```

---

**See also:** [Reconnection](advanced/reconnection.md) · [Error Handling](error-handling.md)
