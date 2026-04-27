class ScriptWriter:
    def __init__(self, type_of_script):
        self.type_of_script = type_of_script

    def generate_script(self):
        if self.type_of_script == 'tutorial':
            return self.generate_tutorial_script()
        elif self.type_of_script == 'news/commentary':
            return self.generate_news_commentary_script()
        elif self.type_of_script == 'motivational':
            return self.generate_motivational_script()
        elif self.type_of_script == 'compilation':
            return self.generate_compilation_script()
        else:
            return "Unknown script type."

    def generate_tutorial_script(self):
        return "Tutorial script content..."

    def generate_news_commentary_script(self):
        return "News/Commentary script content..."

    def generate_motivational_script(self):
        return "Motivational script content..."

    def generate_compilation_script(self):
        return "Compilation script content..."

# Example Usage:
# writer = ScriptWriter('tutorial')
# print(writer.generate_script())