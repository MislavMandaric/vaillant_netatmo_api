"""Module HTTP communication with the Netatmo API."""

from .auth import AuthClient, auth_client
from .errors import (
    ApiException,
    NonOkResponseException,
    NetworkException,
    NetworkTimeoutException,
    NonRetryableException,
    RequestBackoffException,
    RequestClientException,
    RequestException,
    RequestServerException,
    RequestUnauthorizedException,
    RetryableException,
    UnsuportedArgumentsException,
)
from .thermostat import (
    Device,
    Measured,
    EnergyUsage,
    MeasurementItem,
    MeasurementScale,
    MeasurementType,
    Module,
    Program,
    Setpoint,
    SetpointMode,
    SystemMode,
    ThermostatClient,
    TimeSlot,
    Zone,
    thermostat_client,
)
from .token import Token, TokenStore

__all__ = [
    "AuthClient",
    "ThermostatClient",
    "ApiException",
    "NonOkResponseException",
    "NetworkException",
    "NetworkTimeoutException",
    "NonRetryableException",
    "RequestBackoffException",
    "RequestClientException",
    "RequestException",
    "RequestServerException",
    "RequestUnauthorizedException",
    "RetryableException",
    "UnsuportedArgumentsException",
    "Device",
    "Module",
    "Program",
    "Zone",
    "TimeSlot",
    "Setpoint",
    "EnergyUsage",
    "Measured",
    "MeasurementItem",
    "MeasurementType",
    "MeasurementScale",
    "SystemMode",
    "SetpointMode",
    "Token",
    "TokenStore",
    "auth_client",
    "thermostat_client",
]
