class Patient(object):
    def __init__(self, Id=0,name="Matt",allergies="none",bed=0):
        self.Id = Id
        self.name = name
        self.allergies = allergies
        self.bed = bed

class Hospital(object):
    def __init__(self, name="General Hospital",capacity=2):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit(self,patient=Patient()):
        # If the length of the list is >= the capacity do not admit the patient. 
        if len(self.patients) >= self.capacity:
            print "The Hospital is full!"
        else:
            if type(patient) is Patient:
                patient.bed = len(self.patients)# Assign the patient a bed number.
                self.patients.append(patient)# add a patient to the list of patients.
                print "Added Patient"# Return a message either confirming that admission is complete
            else:
                print "Attempted admission is not a Patient class"
        return self
    def discharge(self,nameOrBed):
        if type(nameOrBed) is str:
            for patient in self.patients:
                if nameOrBed == patient.name:
                    self.patients.remove(patient)
                    print "Patient Removed"
                    return self
        elif type(nameOrBed) is int:
            del self.patients[nameOrBed]
            print "Patient Removed"
            return self
        #look up and remove a patient from the list of patients. Change bed number for that patient back to none.
    def patientList(self):
        for patient in self.patients:
            print "Patient: {}; Bed#: {}".format(patient.name,patient.bed)

pat0 = Patient(1,"Mo",10)
genHos = Hospital()
genHos.admit(pat0).admit().patientList()
genHos.discharge(1).patientList()
