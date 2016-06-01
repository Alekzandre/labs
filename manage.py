#! /usr/bin/python
import os
from flask import redirect, url_for, render_template
from app import create_app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app.auth.models import User, Role
from app.firm.models import Firm
from app.formation.models import Project
from app.contrat.models import Contrat

app = create_app(os.getenv('42LABSCONF') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


@app.route('/')
def base_url():
    user_count = User.query.count()
    firm_count = Firm.query.count()
    project_count = Project.query.count()
    contrat_count = Contrat.query.count()
    return (render_template('index.html', user_c=user_count, firm_c=firm_count, project_c=project_count, contrat_c=contrat_count))


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
