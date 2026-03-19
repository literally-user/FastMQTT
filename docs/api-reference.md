# API Reference

## Factory

::: fastmqtt.client.create_client
    options:
      show_source: false

## Client protocols

::: fastmqtt.client.MQTTClientV311
    options:
      show_source: false

::: fastmqtt.client.MQTTClientV5
    options:
      show_source: false

## Core classes

::: fastmqtt.client.MQTTClient
    options:
      show_source: false

::: fastmqtt.client.Subscription
    options:
      show_source: false
      members:
        - get_message
        - __aenter__
        - __aexit__
        - __aiter__
        - __anext__

::: fastmqtt.types.Message
    options:
      show_source: false
      members:
        - topic
        - payload
        - qos
        - retain
        - properties
        - ack

## Configuration

::: fastmqtt.client.ReconnectConfig
    options:
      show_source: false

## Enumerations

::: fastmqtt.types.QoS
    options:
      show_source: false

::: fastmqtt.types.RetainHandling
    options:
      show_source: false

## Properties (MQTT 5.0)

::: fastmqtt.packets.properties.PublishProperties
    options:
      show_source: false

::: fastmqtt.packets.properties.ConnectProperties
    options:
      show_source: false

::: fastmqtt.packets.properties.AuthProperties
    options:
      show_source: false

## Exceptions

::: fastmqtt.errors.MQTTError
    options:
      show_source: false

::: fastmqtt.errors.MQTTConnectError
    options:
      show_source: false

::: fastmqtt.errors.MQTTProtocolError
    options:
      show_source: false

::: fastmqtt.errors.MQTTDisconnectedError
    options:
      show_source: false

::: fastmqtt.errors.MQTTTimeoutError
    options:
      show_source: false
