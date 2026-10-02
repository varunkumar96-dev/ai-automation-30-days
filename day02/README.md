# Day 02 - Validation, Duplicate Handling & REST APIs

## Goal

Build a duplicate-safe lead processing automation and understand how
external systems communicate with automation through REST APIs.

---

## Part 1 - Lead Processing Automation

### Flow

JSON

↓

Validation

↓

Duplicate Check

↓

Insert or Skip

↓

PostgreSQL

### Concepts Learned

- Data validation
- Required fields
- SQL SELECT
- SQL WHERE
- Duplicate detection
- Conditional processing
- PostgreSQL from Python

### Test Cases

1. Existing lead → skipped
2. Missing field → rejected
3. New lead → inserted

---

## Part 2 - REST APIs

### HTTP Methods

| Method | Purpose |
|---|---|
| GET | Read/retrieve data |
| POST | Create new data |
| PUT | Replace/update a resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

### Python

Used the `requests` library:

```python
requests.get()
requests.post()
requests.put()
requests.patch()
requests.delete()