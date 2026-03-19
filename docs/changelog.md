# Changelog

## Unreleased

### Added

- MQTT 5.0 support: `PublishProperties`, `AuthProperties`, `ConnectProperties`, session expiry interval, `no_local`, `retain_as_published`
- `create_client()` factory with version-typed return (`MQTTClientV311` / `MQTTClientV5`)
- Enhanced authentication: `client.auth()` for MQTT 5.0 AUTH packets
- Manual acknowledgement: `auto_ack=False` on `subscribe()`, `Message.ack()` (idempotent)
- Manual ping: `client.ping()` returns RTT in seconds; `timeout` parameter
- Wildcard filter priority routing: most-specific filter wins, no duplicate delivery
- Duplicate-filter guard: `WARNING` log when same filter registered twice
- Backpressure: `receive_buffer_size` on `subscribe()`
- Automatic reconnection with exponential backoff (`ReconnectConfig`)
- Subscriptions survive reconnect transparently
- TLS support: `tls=True` (system CA) or `tls=ssl.SSLContext`
- `@pytest.mark.broker` tests against a real Artemis broker (`docker compose up -d artemis`)

### Architecture

- Pure asyncio — no threads, no callbacks
- I/O-free codec layer: `encode(packet, version=...)` / `decode(buf, version=...)` — no asyncio in `packets/`
- All packet types are frozen dataclasses (`frozen=True, slots=True, kw_only=True`)
- `TaskGroup` for internal `_read_loop` + `_ping_loop`
- Strict mypy + ruff
