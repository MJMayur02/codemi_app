# Implementation Plan: EPMCDMETST-71078 — Add GET /items endpoint to retrieve paginated list of items

-**Jira**: EPMCDMETST-71078
-**Story Title**: Add GET /items endpoint to retrieve paginated list of items
-**Repo**: `MJMayur02/codemi_app`
-**Plan Path**: `docs/plans/EPMODMETST-71078-get-items.md`

> Note: The plan path in this header keeps the repo's file path convention (`docs/plans/<jira-key>-...`).


---


## 1) Overview / Context

The current FastAPI application (`main.py`) supports four CRUD endpoints:

- `POST /items` – create an item
- `GET /items/{item_id}` — get one item
- `PUT /items/{item_id}` — replace an item
- `DELETE /items/{item_id}` — delete an item

The Jira story requires an additional endpoint `GET /items` to list items, with simple pagination via `limit` and `offset`, plus a consistent response schema including `items`, `limit`, `offset`, and `total`.

The app currently stores items in-memory in a module-level dictionary (`items: Dict[int, Item]`) and generates IDs using `itertools.count(1)`. This plan assumes the list endpoint will operate on that in-memory store.

---


## 2) Goal (succinct restatement)

Implement `GET /items` that returns a deterministic, paginated view of all items in memory, validating pagination inputs and returning a stable response contract.

---

## 3) Goals and Non-Goals

### Goals
- Add a new `GET /items` endpoint that returns a paginated list of items.