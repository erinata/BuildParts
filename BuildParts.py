import sublime
import sublime_plugin
#import time
import tempfile
import os

current_new_path = None

#TODO: Make this work for multiple selections.
#TODO: option to "remove indentation" so that it works better for python
#TODO: another command (so that it doesn't use ctrl+b) to build the parts selected and put the console output to the document
class BuildPartsCommand(sublime_plugin.WindowCommand):
    def run(self):
        global current_new_path

        current_new_path = ""
        view = self.window.active_view()
        reg = view.sel()[0]
        if not reg.empty():
            selection = view.substr(reg)

            name = view.file_name()
            fileName, fileExtension = os.path.splitext(name)

            output = tempfile.NamedTemporaryFile(delete=False, suffix=fileExtension)
            output.write(selection.encode('UTF-8'))
            output.close()
    
            current_new_path = output.name
    
            new_view = self.window.open_file(current_new_path)
    
            if not new_view.is_loading():
                self.window.focus_view(new_view)
                self.window.run_command("build")
                self.window.run_command("close")
        else:
            self.window.run_command("build")


#        view = self.window.active_view()S
#        reg = view.sel()[0]
#        selection = view.substr(reg)
#        print selection
#
#        reg_all = sublime.Region(0,view.size())
#        selection_all = view.substr(reg_all)
#
#        edit = view.begin_edit()
#        view.erase(edit,reg_all)
#        view.insert(edit,0,selection)
#
#        time.sleep(0.1)
#
#        self.window.run_command("build")
#
#        view.erase(edit,reg_all)
#        view.insert(edit,0,selection_all)
#        view.end_edit(edit)
#
#        self.window.run_command("undo")

        

class BuildPartsEvent(sublime_plugin.EventListener):
    def on_load(self, view):

        global current_new_path
        if current_new_path != None and view.file_name() == current_new_path:
            view.window().run_command("build")
            view.window().run_command("close")
