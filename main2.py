#AnatolijXD@interia.pl
#ReaktorWytrzymaXD



def wczytanie_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as file:
        lines = file.readlines()

    studenci = {}

    for line in lines:
        data = line.strip().split(',')

        if len(data) >= 4:
            student = {
                'email': data[0],
                'imie': data[1],
                'nazwisko': data[2],
                'punkty': int(data[3])
            }

            if len(data) >= 6:
                student['ocena'] = float(data[4])
                student['status'] = data[5]

            studenci[data[0]] = student

    return studenci

def wstawienie_ocen(studenci):
    for studenci in studenci.values():
        if 'ocena' not in studenci.keys() and studenci['status'] not in ['GRADED', 'MAILED']:
            procent = studenci['punkty'] / 100.0 * 100.0

            if procent >= 91:
                studenci['ocena'] = 5
            elif procent >= 81:
                studenci['ocena'] = 4.5
            elif procent >= 71:
                studenci['ocena'] = 4
            elif procent >= 61:
                studenci['ocena'] = 3.5
            elif procent >= 51:
                studenci['ocena'] = 3
            else:
                studenci['ocena'] = 2

            studenci['status'] = 'GRADED'

def dodanie_studenta(studenci, email, imie, nazwisko, punkty, ocena=None, status=''):
    if email in studenci:
        print(f"Student o adresie email {email} już istnieje.")
        return

    student = {
        'email': email,
        'imie': imie,
        'nazwisko': nazwisko,
        'punkty': punkty,
        'ocena': ocena,
        'status': status
    }

    studenci[email] = student

    print(f"Student {imie} {nazwisko} dodany pomyślnie.")

def usuniecie_studenta(studenci, email):
    if email not in studenci:
        print(f"Nie ma studenta z takim adresem email {email}")
        return

    del studenci[email]

    print(f"Student o adresie: {email} zostal usuniety")

def wyslanie_maila

infoStudents = wczytanie_pliku('students.txt')
print(infoStudents)