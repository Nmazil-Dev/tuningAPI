class Bass():
    def __init__(self, tuning, s1, s2, s3, s4):
        self.tuning = tuning
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
    def get_dict(self):
        return {self.tuning: {'s1': self.s1,'s2': self.s2,'s3': self.s3,'s4': self.s4}}

class Guitar(Bass):
    def __init__(self, tuning, s1, s2, s3, s4, s5, s6):
        Bass.__init__(self, tuning, s1, s2, s3, s4)
        self.tuning = tuning
        self.s5 = s5
        self.s6 = s6
    def get_dict(self):
        return {self.tuning: { 's1': self.s1,'s2': self.s2,'s3': self.s3,'s4': self.s4, 's5': self.s5, 's6': self.s6}}


def get_json(instrument, tuning_names, tunings):
    output = []
    i = 0
    while i < len(tuning_names):
        tuning = (tunings[i].split('-'))
        s1 = tuning[0]
        s2 = tuning[1]
        s3 = tuning[2]
        s4 = tuning[3]
        if instrument == "bass" or instrument == 'ukulele':
            output.append(Bass(tuning_names[i], s1, s2, s3, s4).get_dict())
            i += 1
        else:
            s5 = tuning[4]
            s6 = tuning[5]
            output.append((Guitar(tuning_names[i], s1, s2, s3, s4, s5, s6).get_dict()))
            i += 1
    return output

guitar_names = ["Standard", "Drop D", "Open G", "Open D", "Open E", "Open A"]
guitar_tunings = ["E-A-D-G-B-E", "D-A-D-G-B-E", "D-G-D-G-B-D", "D-A-D-F#-A-D", "E-B-E-G-B-E", "E-A-E-A-C#-E"]

bass_names = ["Standard", "Drop D", "Drop C", "Half Step", "Full Step", "5 String-ish"]
bass_tunings = ["E-A-D-G", "D-A-D-G", "C-A-D-G", "Eb-Ab-Db-Gb", "D-G-C-F", "B-E-A-D"]

ukulele_names = ["Standard", "1/2 Step Down", "Full Step Down", "1/2 Step Up", "Full Step Up"]
ukulele_tunings = ["g-C-E-A", "F#-B-D#-G#", "f-A#-D-G", "g#-C#-F-A#", "a-D-F#-B"]

get_json('guitar', guitar_names, guitar_tunings)
get_json('bass', bass_names, bass_tunings)
get_json('ukulele', ukulele_names, ukulele_tunings)