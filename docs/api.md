# Lead API

## Lead Object

| Field | Type | Description |
|-------|------|-------------|
| id | integer | Identifier |
| name | string | Name of the lead |
| phone | string | Phone number |
| email | string | Email address |
| event_date | date | Date of the event (YYYY-MM-DD) |
| guests_count | integer | Number of guests |
| source | string | Source of the lead |
| status | string | Current status |

## Endpoints

### GET /leads

Returns list of leads.

**Response 200**
```
[
  {
    "id": 1,
    "name": "John Doe",
    "phone": "+123456789",
    "email": "john@example.com",
    "event_date": "2024-08-15",
    "guests_count": 100,
    "source": "website",
    "status": "new"
  }
]
```

### POST /leads

Creates a new lead.

**Request body**
```
{
  "name": "John Doe",
  "phone": "+123456789",
  "email": "john@example.com",
  "event_date": "2024-08-15",
  "guests_count": 100,
  "source": "website",
  "status": "new"
}
```

**Response 201**

Returns the created lead object.

### PATCH /leads/{id}

Updates an existing lead. Only provided fields will be updated.

**Request body**
```
{
  "status": "contacted"
}
```

**Response 200**

Returns the updated lead.
