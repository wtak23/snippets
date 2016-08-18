import datetime, getpass
import sublime, sublime_plugin
class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.date.today().strftime("%d %B %Y (%A)") } )

# class AddTimeCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%H:%M") } )

#https://docs.python.org/2/library/time.html#time.strftime
class AddTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        str_ = "%s" %  datetime.date.today().strftime("%m-%d-%Y ")
        str_ += "%s" %  datetime.datetime.now().strftime("(%H:%M)")
        self.view.run_command("insert_snippet", { "contents": str_ } )