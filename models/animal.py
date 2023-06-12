class Animal:

    def __init__(self, name, type, contact_details, date_of_birth, treatment_notes, check_in_date, check_out_date, vet, id = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.type = type
        self.contact_details = contact_details
        self.treatment_notes = treatment_notes
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.vet = vet
        self.id = id