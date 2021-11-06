class Junior:
    def __init__(self, language, soft_skills, laptop, salary):
        self.language = language
        self.soft = soft_skills
        self.laptop = laptop
        self.salary = salary

    def say_which_language(self):
        return f'Im using {self.language}'

    def __str__(self):
        return f'Language: {self.language}\n' \
               f'Soft_skills: {self.soft}\n' \
               f'Laptop: {self.laptop}\n' \
               f'Salary: {self.salary}'


junior_1 = Junior(language='Python',
                  soft_skills='Good Enoungh',
                  laptop='gaming laptop',
                  salary='300$')

# print(junior_1)

class Middle(Junior):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolving, reliable):
        super().__init__(language, soft_skills, laptop, salary)
        self.fast_resolving = fast_resolving
        self.reliable = reliable

    def __str__(self):
        return super(Middle, self).__str__() + f'\nResolving : {self.fast_resolving}\n' \
                                                f'Reliable : {self.reliable}'
middle_1 = Middle(language='Python',
                  soft_skills='Good Enoungh',
                  laptop='gaming laptop',
                  salary='300$',
                   fast_resolving='Often',
                   reliable=True)
# print(middle_1)
# print(middle_1.say_which_language())

class Senior(Middle):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolving, reliable, architecture, leading_skill):
        super().__init__(language, soft_skills, laptop, salary, fast_resolving, reliable)
        self.arch = architecture
        self.lead = leading_skill

    def __str__(self):
        return super(Senior, self).__str__() + f'\nArchitecture : {self.arch}\n' \
                                                f'Leading Skill : {self.lead}'

senior_1 = Senior(language='Python',
                  soft_skills='Good Enoungh',
                  laptop='gaming laptop',
                  salary='6000$',
                   fast_resolving='Often',
                    reliable=True,
                  architecture=True,
                  leading_skill=True)
print(senior_1)