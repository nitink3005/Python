class Dept:
    def __init__(self):
        self.depts = {
            'hr': 'Human Resource',
            'acc': 'Accounts & Finance',
            'sd' : 'Sales & Distribution',
            'mkt': 'Marketing'
        }
    
    ## call is an override method
    def __call__(self, dept):
        return self.depts[dept]

d = Dept()
result = d('hr')
print(result)