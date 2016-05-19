#! /usr/bin/python
import os
from app import create_app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app.auth.models import User, Role
from app.firm.models import Firm

app = create_app(os.getenv('42LABSCONF') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return {
        'app': app,
        'db': db,
        'User': User,
        'Firm': Firm,
        'Role': Role
    }

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


@manager.command
def test():

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
