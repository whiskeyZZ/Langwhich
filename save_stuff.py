class Prop:
    level_counter = 0
    button_one_lang = ""
    button_two_lang = ""
    button_three_lang = ""

    def get_counter(self):
        return self.level_counter

    def add_to_counter(self):
        self.level_counter += 1

    def set_one_lang(self, lang):
        self.button_one_lang = lang
    
    def set_two_lang(self, lang):
        self.button_two_lang = lang

    def set_three_lang(self, lang):
        self.button_three_lang = lang

    def get_one_lang(self):
        return self.button_one_lang

    def get_two_lang(self):
        return self.button_two_lang

    def get_three_lang(self):
        return self.button_three_lang

