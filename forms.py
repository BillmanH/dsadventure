from django import forms

#https://docs.djangoproject.com/en/2.2/topics/forms/#rendering-fields-manually
class playerCharacterForm(forms.Form):
    name = forms.CharField(label='Your character\'s name', max_length=100)
    #background
    backgroundChoices = [('1', 'Noble family'), 
            ('2', 'Pesant family'),
            ('3', 'Temple orphan'),
            ('3','Nomad family')]
    background = forms.ChoiceField(widget=forms.RadioSelect, choices=backgroundChoices)
    #skills
    coreSkillsChoices = [('1','fencing'),
            ('2','archery'),
            ('3','spellcasting'),
            ('4','persuasion')]
    coreskills = forms.ChoiceField(widget=forms.RadioSelect, choices=coreSkillsChoices)
    #secondary skills
    secondarySkillsChoices = [('1','mountaneer'),
            ('2','desert survival'),
            ('3','hunting'),
            ('4','additional language')]
    secondaryskills = forms.ChoiceField(widget=forms.RadioSelect, choices=secondarySkillsChoices)

