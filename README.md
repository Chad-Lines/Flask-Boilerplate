# Flask Boilerplate v0.01

This is a simple boilerplate for small flask projects that requires user login. This is primarily for personal use, but if someone else wants to use it, that's fine too.

## Assumptions

The following assumptions are made:
- Login is controlled via flask and not a third-party like OAuth
- SQLite is the database; this is easy to modify

## Other Peculiarities

This has two tables (models.py) User and Customer. Only User is really in use. 
