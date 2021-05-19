net stop odoo-server-12.0
net start odoo-server-12.0
pytest -v -s testCases/test_automate_upgrade.py --browser chrome