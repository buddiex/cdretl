import app
from flask.ext.script import Manager, Server, Shell
from flask.ext.script.commands import ShowUrls,  Clean
from datetime import datetime

manager = Manager(app.app)

@manager.command
def run(in_date,stream_name):
    app.hello_world(in_date,stream_name)
    ref_date = datetime.strptime(in_date, '%Y%m%d')

    # app.main_generate(stream_name, ref_date)
    # app.main_generate_parallel(stream_name, ref_date)

@manager.option('-sn', '--surname', help='Your surname should be entered here', required=False)
@manager.option('-n', '--name', help='Your name should be entered here')
@manager.command
def hello(name, surname):
    app.hello_world()
    print "hello", name, surname


manager.add_command("runservernoreload", Server(use_reloader=False))
manager.add_command("shell", Shell())
manager.add_command("urls", ShowUrls())
manager.add_command("clean", Clean())

if __name__ == "__main__":
    manager.run()