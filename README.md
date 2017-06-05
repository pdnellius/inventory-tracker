# MHacks Inventory Tracker
Tracking system for hardware, food, and other things!

## Core Functionality
- [ ] Basic tracking indexed by barcode 
- [ ] Inventory search
- [ ] Add/remove items
- [ ] Item categories
- [ ] Notifications for custom events (e.g. quantity falls below threshold, etc.)
- [ ] Various data analyitcs for item consumption & distribution

## Building
Download and install `Python2.7` however you like.

Install the dependencies with pip: `pip install -r requirements.txt`

Run the server: `./manage.py runserver`

Additionaly, you may need to make and/or run migrations: `./manage.py makemigrations` and/or `./manage.py migrate`
