import random

def d6(dice_number = 1):
    result = 0
    if dice_number >= 1:
        for x in range(dice_number):
            val = random.randrange(1, 7)
            result += val
        return result
    else:
        return False
def recurce_result_d6(dice_number, top_value, bot_value = 0):
    result = d6(dice_number)
    if top_value != 0 and result >= top_value:
        return recurce_result_d6(dice_number, top_value, bot_value)
    elif bot_value != 0 and result <= bot_value:
        return recurce_result_d6(dice_number, top_value, bot_value)
    else:
        return result

def d10(dice_number = 1):
    result = 0
    if dice_number >= 1:
        for x in range(dice_number):
            result += random.randrange(1, 11)

        return result
    else:
        return False
def recurce_result_d10(dice_number, top_value, bot_value = 0):
    result = d10(dice_number)
    if top_value != 0 and result > top_value:
        return recurce_result_d10(dice_number, top_value, bot_value)
    elif bot_value != 0 and result <= bot_value:
        return recurce_result_d10(dice_number, top_value, bot_value)
    else:
        return result

def characteristics():
    hability_scores = []

    for x in range(9):
        characteristics_score = int(recurce_result_d6(2, 11))
        hability_scores.append(x)
        hability_scores[x] = characteristics_score

    return hability_scores

# Returns text with Fixer habilities
def fixer_skils():
    array = []
    array.append(0)
    array.append(1)
    array[0] = "Moverse en la calle &"
    array[1] = "Advertir/Notar &, Abrir cerraduras &, Armas cortas &, Cuerpo a cuerpo &, Falsificacion &, Intimidar &, Pelea &, Persuacion &, Robar bolsillos &"
    return array
# Returns text with Executive habilities
def executive_skils():
    array = []
    array.append(0)
    array.append(1)
    array[0] = "Recursos &"
    array[1] = "Advertir/Notar &, Arreglo personal &, Buscar libros &, Cultura general &, Mercado de valores &, Percepcion humana &, Persuacion &, Vestuario y estilo &, Vida social &"
    return array
# Returns text with Solo habilities
def solo_skils():
    array = []
    array.append(0)
    array.append(1)
    array[0] = "Sentido del combate &"
    array[1] = "Advertir/Notar &, Armas cortas &, Armamento &, Atletismo &, Cuerpo a cuerpo &, Fusil &, Pelea o Art marcial  &, Sigilo &, Subfusil &"
    return array
# Returns text with Nomad habilities
def nomad_skils():
    array = []
    array.append(0)
    array.append(1)
    array[0] = "Familia &"
    array[1] = "Advertir/Notar &, Atletismo &, Conducir &, Cuerpo a cuerpo &, Fusil &, Mecanica basica &, Pelea &, Resistencia &, Supervivencia &"
    return array
# Returns text with Police habilities
def police_skils():
    array = []
    array.append(0)
    array.append(1)
    array[0] = "Autoridad &"
    array[1] = "Advertir/Notar &, Armas cortas &, Atletismo &, Conocimiento de la calle &, Cuerpo a cuerpo &, Cultura general &, Interrogatorio &, Pelea &, Percepcion humana &"
    return array
# Returns text with Rocker habilities
def rocker_skils():
    array = []
    array.append(0)
    array.append(1)
    array[0] = "Liderazgo carismatico &"
    array[1] = "Advertir/Notar &, Composicion &, Conocimiento de la calle &, Interpretar &, Pelea &, Persuacion &, Tocar instrumento &, Seduccion &, Vestuario y estilo &"
    return array
# Returns text with Tecnic habilities
def tecnic_skils():
    array = []
    array.append(0)
    array.append(1)
    array[0] = "Chapuza &"
    array[1] = "Advertir/Notar &, Cibertecnologia &, Cultura general &, Electronica &, Enseñar &, Mecanica basica &"
    return array
# Returns text with Tecno Medic habilities
def tocnomedic_skils():
    array = []
    array.append(0)
    array.append(1)
    array[0] = "Tecnica medica &"
    array[1] = "Advertir/Notar &, Buscar libros &, Cultura general &, Diagnostico &, Farmacia &, Man. tanque crio &, Mecanica basica &, Percepcion humana &, Zoologia &"
    return array

def main_habilities():
    array_char = characteristics()
    text = "INT[&] REF[&] TEC[&] FRI[&] ATR[&] SUE[&] MOV[&] TCO[&] EMP[&]"
    for x in array_char:
        text = text.replace("&", str(x), 1)

    print(text)

def cibernetics(rol):
    max_roll = 3
    rolls_made = 0
    # si es un mercenario
    if rol == 3:
        max_roll = 6

    array_ciber = []
    while max_roll > rolls_made:
        roll = d10(1)
        roll2 = 0
        complete_roll = roll
        if roll <= 3:
            roll2 = d6(1)
            complete_roll = complete_roll * 10 + roll2

        if complete_roll not in array_ciber:
            array_ciber.append(len(array_ciber))
            array_ciber[len(array_ciber)-1] = complete_roll
            rolls_made += 1

    for x in array_ciber:
        if x == 4:
            print("Nudillos de acero (1d6+2)")
        if x == 5:
            print("Destripadores (2d6)")
        if x == 6:
            print("Vampiros (1d6/3)")
        if x == 7:
            print("Troceadores (2d6)")
        if x == 8:
            print("Potenciador de REF Kerenzikov (+1 a la iniciativa)")
        if x == 9:
            print("Potenciador de REF Sandevistan (+3 a la iniciativa por 5 turnos)")
        if x == 11:
            print("Infrarojos (Permite ver en la oscuridad total, usando emiciones de calor)")
        if x == 12:
            print("Luz tenue (Permite ver en luz tenue, casi total oscuridad)")
        if x == 13:
            print("Camara (Captura hasta 20 imgs)")
        if x == 14:
            print("Lanzadardos (Arma de veneno, 1 dardo, -4REF o 4d6 (mitad con salvacion exitosa))")
        if x == 15:
            print("Antideslumbramiento (Inmune a la cegera por fog o laser)")
        if x == 16:
            print("Sist. de punteria (+1 ataque con arma int.)")
        if x == 21:
            print("Pistola media (2d6+1 [10)2])")
        if x == 22:
            print("Pistola ligera (1d6+1 [10)2])")
        if x == 23:
            print("Pistola media (2d6+1 [12)2])")
        if x == 24:
            print("Subfusil ligero (2d6+1 [30)15])")
        if x == 25:
            print("Pistola muy pesada (4d6+1 [8)1])")
        if x == 26:
            print("Pistola pesada (3d6+1 [8)2])")
        if x == 31:
            print("Wearman (Sistema de musica)")
        if x == 32:
            print("Radio (Comunicacion con radio 1,5km)")
        if x == 33:
            print("Dispositivo telefonico (celular completo, zonas urbanas)")
        if x == 34:
            print("Escucha amplificado (+1 advertir/notar con oido)")
        if x == 35:
            print("Editor de sonido (+2 adviertir/notar al oir una conversacion)")
        if x == 36:
            print("Conector de grabador digital (transmite sonido a un grab. digital)")

def habilities(rol):
    score = 40
    spetial = ""
    skills = ""

    if rol == 1:
        spetial = fixer_skils()[0]
        skills = fixer_skils()[1]
    if rol == 2:
        spetial = executive_skils()[0]
        skills = executive_skils()[1]
    if rol == 3:
        spetial = solo_skils()[0]
        skills = solo_skils()[1]
    if rol == 4:
        spetial = nomad_skils()[0]
        skills = nomad_skils()[1]
    if rol == 5:
        spetial = police_skils()[0]
        skills = police_skils()[1]
    if rol == 6:
        spetial = rocker_skils()[0]
        skills = rocker_skils()[1]
    if rol == 7:
        spetial = tecnic_skils()[0]
        skills = tecnic_skils()[1]
    if rol == 8:
        spetial = tocnomedic_skils()[0]
        skills = tocnomedic_skils()[1]

    spetial_score = recurce_result_d10(1, score, 0)
    spetial = spetial.replace("&", str(spetial_score), 1)
    score -= spetial_score
    for x in range(8):
        skills_score = recurce_result_d10(1, score, 0)
        if score <= 0 or skills_score <= 0: break

        skills = skills.replace("&", str(skills_score), 1)
        score -= int(skills_score)

        if score <= 0 or skills_score <= 0: break

    print(spetial)
    print(skills)
    print(f"Restan {score} puntos")

def armor_guns(rol):
    result = d10()
    if rol == 4 or rol == 5: result += 2
    if rol == 3: result += 3
    if result == 1:
        print("Cuero Pesado (CP 4*) /// Cuchillo (1d6)")
    if result == 2:
        print("Chaqueta Blindada (CP 10·) /// PL (1d6+1) [10)2]")
    if result == 3:
        print("Chaqueta Blindada L (CP 14··) /// PM (2d6+1) [12)2]")
    if result == 4:
        print("Chaqueta Blindada L (CP 14··) /// PP (3d6) [8)2]")
    if result == 5:
        print("Chaqueta Blindada M (CP 18··) (CE +1) /// PP (3d6) [8)2]")
    if result == 6:
        print("Chaqueta Blindada M (CP 18··) (CE +1) /// SUB L (2d6+1) [50)23]")
    if result == 7:
        print("Chaqueta Blindada M (CP 18··) (CE +1) /// FUS L (5d6) [35)25]")
    if result == 8:
        print("Chaqueta Blindada P (CP 20··) (CE +2) /// FUS M (5d6) [30)30]")
    if result == 9:
        print("Chaqueta Blindada P (CP 20··) (CE +2) /// FUS P (6d6+2) [35)25]")
    if result >= 10:
        print("Metal Gear (CP 25*) (CE+2) /// FUS P (6d6+2) [35)25]")



def display_character(rol):
    main_habilities()
    habilities(rol)
    cibernetics(rol)
    armor_guns(rol)

class main:
    last_command = ""

    while 1:
        command = input("> ").upper()

        if command == "HELP":
            print('FIX - generate fixer  EXE - generate executive  SOLO - generate mercenary \n'
                  'NOM - generate nomad  POL - generate police     ROC - generate reckerboy \n'
                  'TEC - generate tecy   MED - generate tecnomedic \n'
                  'STATS - random stats  \n'
                  'CIB3 - generate ciber                           CIB6 - generate ciber \n'
                  'EQUIP - generate armor/guns                     EQUIPSOLO - generate armor/guns for Solo \n'
                  'QUIT - to end program')
        elif command == "FIX":
            display_character(1)
        elif command == "EXE":
            display_character(2)
        elif command == "SOLO":
            display_character(3)
        elif command == "NOM":
            display_character(4)
        elif command == "POL":
            display_character(5)
        elif command == "ROC":
            display_character(6)
        elif command == "TEC":
            display_character(7)
        elif command == "MED":
            display_character(8)

        elif command == "STATS":
            main_habilities()
        elif command == "CIB3":
            cibernetics(1)
        elif command == "CIB6":
            cibernetics(3)
        elif command == "EQUIP":
            armor_guns(1)
        elif command == "EQUIPSOLO":
            armor_guns(3)
        elif command == "QUIT":
            print("the program has ended")
            break
        else:
            print("I don't undertand")


