import tkinter as tk
import unicodedata


def normalizar_texto(texto):
    
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_normalizado = ''.join([c for c in texto_normalizado if unicodedata.category(c) != 'Mn'])
    
    return texto_normalizado.lower()


paises_e_capitais = {
    "Afeganistão": "Cabul",
    "África do Sul": "Pretória",
    "Albânia": "Tirana",
    "Alemanha": "Berlim",
    "Andorra": "Andorra-a-Velha",
    "Angola": "Luanda",
    "Antígua e Barbuda": "Saint John's",
    "Arábia Saudita": "Riad",
    "Argélia": "Argel",
    "Argentina": "Buenos Aires",
    "Armênia": "Erevã",
    "Austrália": "Canberra",
    "Áustria": "Viena",
    "Azerbaijão": "Bacu",
    "Bahamas": "Nassau",
    "Bahrein": "Manama",
    "Bangladesh": "Daca",
    "Barbados": "Bridgetown",
    "Bélgica": "Bruxelas",
    "Belize": "Belmopan",
    "Benim": "Porto-Novo",
    "Bermudas": "Hamilton",
    "Bielorrússia": "Minsk",
    "Bolívia": "Sucre",
    "Bósnia e Herzegovina": "Sarajevo",
    "Botsuana": "Gaborone",
    "Brasil": "Brasília",
    "Brunei": "Bandar Seri Begawan",
    "Bulgária": "Sófia",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega",
    "Butão": "Thimphu",
    "Cabo Verde": "Praia",
    "Camarões": "Yaoundé",
    "Camboja": "Phnom Penh",
    "Canadá": "Ottawa",
    "Catar": "Doha",
    "Cazaquistão": "Astana",
    "Chade": "N'Djamena",
    "Chile": "Santiago",
    "China": "Pequim",
    "Chipre": "Nicósia",
    "Colômbia": "Bogotá",
    "Comores": "Moroni",
    "Congo (República do Congo)": "Brazzaville",
    "Congo (República Democrática do Congo)": "Kinshasa",
    "Coreia do Norte": "Pyongyang",
    "Coreia do Sul": "Seul",
    "Costa Rica": "San José",
    "Croácia": "Zagreb",
    "Cuba": "Havana",
    "Dinamarca": "Copenhague",
    "Djibuti": "Djibuti",
    "Dominica": "Roseau",
    "Egito": "Cairo",
    "El Salvador": "San Salvador",
    "Emirados Árabes Unidos": "Abu Dhabi",
    "Equador": "Quito",
    "Eritreia": "Asmara",
    "Eswatini": "Mbabane",
    "Eslováquia": "Bratislava",
    "Eslovênia": "Liubliana",
    "Espanha": "Madri",
    "Estados Unidos": "Washington, D.C.",
    "Estônia": "Tallinn",
    "Etiópia": "Adis Abeba",
    "Fiji": "Suva",
    "Filipinas": "Manila",
    "Finlândia": "Helsinque",
    "França": "Paris",
    "Gabão": "Libreville",
    "Gâmbia": "Banjul",
    "Gana": "Acra",
    "Geórgia": "Tbilisi",
    "Gibraltar": "Gibraltar",
    "Granada": "Saint George's",
    "Grécia": "Atenas",
    "Guatemala": "Cidade da Guatemala",
    "Guiana": "Georgetown",
    "Guiné": "Conakry",
    "Guiné Equatorial": "Malabo",
    "Guiné-Bissau": "Bissau",
    "Haiti": "Porto Príncipe",
    "Honduras": "Tegucigalpa",
    "Hungria": "Budapeste",
    "Iémen": "Sanaa",
    "Ilhas Cook": "Avarua",
    "Ilhas Faroe": "Tórshavn",
    "Ilhas Malvinas": "Stanley",
    "Ilhas Marshall": "Majuro",
    "Ilhas Salomão": "Honiara",
    "Índia": "Nova Délhi",
    "Indonésia": "Jacarta",
    "Irã": "Teerã",
    "Iraque": "Bagdá",
    "Irlanda": "Dublin",
    "Islândia": "Reiquiavique",
    "Israel": "Jerusalém",
    "Itália": "Roma",
    "Jamaica": "Kingston",
    "Japão": "Tóquio",
    "Jordânia": "Amã",
    "Kiribati": "Tarawa",
    "Kosovo": "Pristina",
    "Kuwait": "Kuwait City",
    "Laos": "Vientiã",
    "Lesoto": "Maseru",
    "Letônia": "Riga",
    "Libéria": "Monróvia",
    "Líbia": "Trípoli",
    "Liechtenstein": "Vaduz",
    "Lituânia": "Vílnius",
    "Luxemburgo": "Luxemburgo",
    "Madagáscar": "Antananarivo",
    "Malásia": "Kuala Lumpur",
    "Malawi": "Lilongwe",
    "Maldivas": "Malé",
    "Mali": "Bamaco",
    "Malta": "Valeta",
    "Marrocos": "Rabat",
    "Maurício": "Port Louis",
    "Mauritânia": "Nuakchott",
    "México": "Cidade do México",
    "Micronésia": "Palikir",
    "Moçambique": "Maputo",
    "Moldávia": "Chisináu",
    "Mônaco": "Mônaco",
    "Montenegro": "Podgorica",
    "Namíbia": "Windhoek",
    "Nauru": "Yaren",
    "Nepal": "Catmandu",
    "Nicarágua": "Manágua",
    "Níger": "Niamey",
    "Nigéria": "Abuja",
    "Noruega": "Oslo",
    "Nova Zelândia": "Wellington",
    "Omã": "Mascate",
    "Paquistão": "Islamabad",
    "Palau": "Ngerulmud",
    "Panamá": "Cidade do Panamá",
    "Papua-Nova Guiné": "Port Moresby",
    "Paraguai": "Assunção",
    "Peru": "Lima",
    "Polônia": "Varsóvia",
    "Portugal": "Lisboa",
    "Quênia": "Nairóbi",
    "Quirguistão": "Bishkek",
    "Reino Unido": "Londres",
    "República Centro-Africana": "Bangui",
    "República Dominicana": "Santo Domingo",
    "República Tcheca": "Praga",
    "Romênia": "Bucareste",
    "Ruanda": "Kigali",
    "Rússia": "Moscou",
    "Saara Ocidental": "Laayoune",
    "Samoa": "Apia",
    "Santa Lúcia": "Castries",
    "São Cristóvão e Nevis": "Basseterre",
    "São Tomé e Príncipe": "São Tomé",
    "Senegal": "Dacar",
    "Serra Leoa": "Freetown",
    "Sérvia": "Belgrado",
    "Singapura": "Cingapura",
    "Síria": "Damasco",
    "Somália": "Mogadíscio",
    "Sri Lanka": "Colombo",
    "Sudão": "Cartum",
    "Sudão do Sul": "Juba",
    "Suriname": "Paramaribo",
    "Suécia": "Estocolmo",
    "Suíça": "Berna",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Tailândia": "Bangcoc",
    "Tanzânia": "Dodoma",
    "Togo": "Lomé",
    "Tonga": "Nukualofa",
    "Trinidad e Tobago": "Porto da Espanha",
    "Tunísia": "Túnis",
    "Turcomenistão": "Asgabate",
    "Turquia": "Ancara",
    "Tuvalu": "Funafuti",
    "Uganda": "Campala",
    "Ucrânia": "Kiev",
    "Uruguai": "Montevidéu",
    "Vanuatu": "Port Vila",
    "Vaticano": "Cidade do Vaticano",
    "Venezuela": "Caracas",
    "Vietnã": "Hanói",
    "Zâmbia": "Lusaka",
    "Zimbábue": "Harare"
}

def buscar_capital():
    
    pais = entrada_pais.get()

    
    pais_normalizado = normalizar_texto(pais)

    
    for pais_nome in paises_e_capitais:
        if normalizar_texto(pais_nome) == pais_normalizado:
            capital = paises_e_capitais[pais_nome]
            resultado_label.config(text=f"A capital de {pais_nome} é {capital}.")
            return
    
    
    resultado_label.config(text="Desculpe, não temos informações sobre esse país.")


janela = tk.Tk()
janela.title("Consulta de Países e Capitais")
janela.geometry("400x300")  


instrucao_label = tk.Label(janela, text="Digite o nome de um país:")
instrucao_label.pack(pady=10)


entrada_pais = tk.Entry(janela, width=30)
entrada_pais.pack(pady=5)


buscar_button = tk.Button(janela, text="Buscar Capital", command=buscar_capital)
buscar_button.pack(pady=10)


resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.pack(pady=20)


janela.mainloop()
