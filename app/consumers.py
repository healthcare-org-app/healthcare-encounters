"""Kafka consumers for encounters-service.

One handler per subscribed topic. Real handlers write to this service's own
database and/or publish follow-up events; stub handlers just log + audit.
"""
from __future__ import annotations

import logging

from psycopg.types.json import Json

from healthcare_common.audit import emit_audit

log = logging.getLogger("encounters-service.consumers")

TABLE = "encounters"


def register(svc) -> None:
    bus = svc.bus
    db = svc.db
    clients = svc.clients

    @bus.on("appointment.booked")
    def _on_appointment_booked(envelope: dict) -> None:
        log.info("encounters-service: received appointment.booked id=%s", envelope.get("id"))
        emit_audit(bus, action="consume.appointment.booked", actor="system:encounters-service",
                   target=None, details={"envelope_id": envelope.get("id")})

