# encounters-service

encounters-service — domain: ehr

- **Port:** 8301
- **Language:** Python 3.11 + Flask
- **Database:** `ehr` (Postgres, table `encounters`)
- **Event bus:** Kafka

## API

| Method    | Path                       |
|-----------|----------------------------|
| GET       | `/api/encounters/`          |
| POST      | `/api/encounters/`          |
| GET       | `/api/encounters/<id>`      |
| PUT/PATCH | `/api/encounters/<id>`      |
| DELETE    | `/api/encounters/<id>`      |
| GET       | `/health`                  |
| GET       | `/ready`                   |

## Events

**Publishes:** encounter.started, encounter.ended
**Subscribes:** appointment.booked

## HTTP peer dependencies

- `patients-service`
- `providers-service`
- `appointments-service`
- `audit-log-service`

## Local dev

```bash
pip install -e ../../libs/py-healthcare-common
pip install -r requirements.txt
cp .env.example .env
(cd ../../infra && docker compose up -d postgres kafka kafka-init)
python -m app.main
```

## Tests

```bash
pytest
```
