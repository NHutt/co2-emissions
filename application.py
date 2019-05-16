from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import jsonify
from flask import json
import jsonpickle
import csv

app = Flask(__name__)


# metodit, joilla saadaan koko maailman kokonaismäärä populaation ja saasteiden osalta
# tietylle vuodelle
# tai saataisiin jos data olisi vähän vähemmän ihmeellisesti rakennettu

def calculate_total_emissions_for_year(): #parametri year
    with open ('./data/CSV/co2-emissions-data.csv', 'r') as emissions_csv:
        csv_reader = csv.reader(emissions_csv, delimiter=',')
        year = '2005'
        total_emissions = 0.0
        for line in csv_reader:
            line_number = csv_reader.line_num
            # hankitaan headerit ja etsitään niiden joukosta kysytyn vuoden indeksi
            if line_number == 5:
                headers = line
                print(headers)
                index_year = headers.index(year)
            if line_number > 5:
                # otetaan kunkin maan kohdalla kysytyn vuoden päästöarvo
                emissions = (line[index_year])
                if len(emissions) > 0:
                    total_emissions += float(emissions)
                
        formatted_total_emissions = format(total_emissions, ".2f")
        print(formatted_total_emissions)
        print('Total worldwide amount of emissions for the year ' + year + ' was at least ' + formatted_total_emissions + ' kilotonnes.')

        # datassa on erillisenä koko maailma + useita eri alueita, joten tulokset ovat hyvin harhaanjohtavia
        # siispä tämä metodi ei ole käytössä
    return formatted_total_emissions

def calculate_total_population_for_year(): # parametri year
    with open ('./data/CSV/population-data.csv', 'r') as population_csv:
        csv_reader = csv.reader(population_csv, delimiter=',')
        year = '2005'
        total_population = 0
        for line in csv_reader:
            line_number = csv_reader.line_num
            # hankitaan headerit ja etsitään niiden joukosta kysytyn vuoden indeksi
            if line_number == 5:
                headers = line
                print(headers)
                index_year = headers.index(year)
            if line_number > 5:
                # otetaan kunkin maan kohdalla kysytyn vuoden väkiluku
                population = (line[index_year])
                if len(population) > 0:
                    total_population += int(population)
                
        print(total_population)
        print('Total world population in the year ' + year + ' was at least ' + str(total_population) + ' people.')

        # palauttaa aivan väärän arvon, koska aineistossa maat erillisinä + maanosat, joten
        # väkiluvusta tulee noin kymmenen kertaa isompi kuin kuuluisi

    return str(total_population)
    

# metodit, joilla listataan maat järjestykseen joko saastemäärän tai saastemäärä
# per henkilö perusteella
# ei tällä hetkellä käytössä

def generate_emissions_by_country_list(year):
    emissions_per_country_list = []
    # for-looppi, joka käy koko emissions-tiedoston läpi
    # ja poimii oikean vuosi-indeksin arvon
    # ja tallentaa arvot dictionaryyn, key: maan nimi, value: saatu emissions-arvo
    # sen jälkeen ordered dict, niin että dictionary järjestyy niin, että
    # emissions-arvoltaan suurin maa tulee ensin

    return emissions_per_country_list

def generate_emissions_per_capita_list(year):
    emissions_per_capita_list = []
    # tähän joku for-looppi, joka alkaa käydä emissions csv-tiedostoa läpi
    # ja luo dictionaryn niin, että key: maan nimi, value: get_emissions jaettuna get_population
    # sen jälkeen järjestää listan ordered dict niin, että per capita-arvoltaan
    # suurin maa tulee ensin ja palauttaa dictionaryn

    return emissions_per_capita_list


# metodit, joilla haetaan yksittäisten maiden arvoja
# väkiluku, päästöt, ja päästöt suhteutettuna väkilukuun

def get_population(year, country):
    with open ('./data/CSV/population-data.csv', 'r') as population_csv:
        csv_reader = csv.reader(population_csv, delimiter=',')
        country = 'Finland'
        year = '2000'
        for line in csv_reader:
            line_number = csv_reader.line_num
            if line_number == 5:
                headers = line
                print(headers)
                index_year = headers.index(year)
            if line_number > 5:
                # tarkistetaan, vastaako rivin maa kysyttyä maata
                if line[0] == country:
                    if len(line[index_year]) > 0:
                        # tulokseksi saadaan kysytyn vuoden väkiluku
                        population = int(line[index_year])
                        #print(population)
                        #print('In ' + country + ' population in the year ' + year + ' was ' + population + '.')
                    else:
                        population = 0

    return population


def get_emissions(): #parametrit year ja country
    with open ('./data/CSV/co2-emissions-data.csv', 'r') as emissions_csv:
        csv_reader = csv.reader(emissions_csv, delimiter=',')
        country = 'Finland'
        year = '2000'
        for line in csv_reader:
            line_number = csv_reader.line_num
            if line_number == 5:
                headers = line
                print(headers)
                index_year = headers.index(year)
            if line_number > 5:
                # tarkistetaan, vastaako rivin maa kysyttyä maata
                if line[0] == country:
                    # tulokseksi saadaan kysytyn vuoden päästöt
                    emissions = line[index_year]
                    print(emissions)
                    #print('In ' + country + ' the emissions of the year ' + year + ' were ' + emissions + ' kilotonnes.')

    return emissions


def get_year_list():
    with open ('./data/CSV/co2-emissions-data.csv', 'r') as emissions_csv:
        csv_reader = csv.reader(emissions_csv, delimiter=',')
        for line in csv_reader:
            line_number = csv_reader.line_num
            # luodaan headereiden vuosista lista
            if line_number == 5:
                headers = line
                indexes = len(headers)
                years = []
                # hmm mitähän tässä tapahtuu
                for i in range(4, indexes-1):
                    if len(line[i]) > 0:
                        years.append(int(line[i]))
                    else:
                        years.append(0)

                print(years)
                print(len(years))

    return years


def get_all_emissions_for_country(country):
    with open ('./data/CSV/co2-emissions-data.csv', 'r') as emissions_csv:
        csv_reader = csv.reader(emissions_csv, delimiter=',')
        for line in csv_reader:
            line_number = csv_reader.line_num
            # luodaan headereiden vuosista lista
            if line_number == 5:
                headers = line
                indexes = len(headers)
                years = []
                for i in range(4, indexes-1):
                    years.append(line[i])

            if line_number > 5:
                # tarkistetaan, vastaako rivin maa kysyttyä maata
                if line[0] == country:
                    emissions = []
                    # tulokseksi saadaan kysytyn vuoden päästöt
                    for i in range(4, indexes-1):
                        if len(line[i]) > 0:
                            emissions.append(float(line[i]))
                        else:
                            emissions.append(0)
                    print(emissions)
                    print(len(emissions))

    return emissions


# ei käytössä, vaikka varmaan ois hyvä olla
def calculate_emissions_per_capita(country, year):
    # tähän joku metodi, joka hakee ensin oikean väkiluvun
    # get_population
    # ja sitten hakee päästöt
    # get_emissions
    # ja sitten laskee emissions jaettuna väkiluvulla
    # ja palauttaa arvon
    emissions_per_capita = 0
    return emissions_per_capita


def get_country_list():
    with open ('./data/CSV/co2-emissions-data.csv', 'r') as emissions_csv:
        csv_reader = csv.reader(emissions_csv, delimiter=',')
        countries = []
        for line in csv_reader:
            line_number = csv_reader.line_num
            # lisätään kunkin rivin ensimmäinen arvo eli maan nimi listalle
            if line_number > 5:
                countries.append(line[0])
        print(countries)
    return countries


# en ole ihan varma, miksi kehitin tähän oman metodin
def check_data_values(list):
    values_amount = 0
    for i in range(0, (len(list))-1):
        if (list[i] > 0):
            values_amount += 1
    print(values_amount)
    return values_amount


# piti kehittää data-objekteja
class Data(object):
    x = ''
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return self.x + ':' + str(self.y)

    def __str__(self):
        return self.x + ':' + str(self.y)

def make_data(x, y):
    data = Data(x, y)

    return data


@app.route('/co2-emissions/browse', methods=["GET", "POST"])
def browse():
    if request.method == "GET":
        years = get_year_list()
        return render_template('browse.html', data_years=years)
    
    elif request.method == "POST":
        with open ('./data/CSV/co2-emissions-data.csv', 'r') as emissions_csv:
            csv_reader = csv.reader(emissions_csv, delimiter=',')
            years = get_year_list()
            data_list = []
            # otetaan vuosi requestista
            year = request.form['year']
            exclusions = ['World', 'IDA', 'income', 'IBRD', 'dividend', 'Asia', 'OECD', 'Euro', 'America', 'Asia', 'Middle East', 'Africa', 'Heavily', 'Other', 'countries', 'Fragile', 'states']
            for line in csv_reader:
                line_number = csv_reader.line_num
                if line_number == 5:
                    headers = line
                    index_year = headers.index(year)
                    print(headers)
                    print(index_year)
                if line_number > 5:    
                    if len(line[index_year]) > 0:
                        # karsitaan listalta pois isot alueet, että data piirtyy edes jotenkin
                        if any(x in line[0] for x in exclusions):
                            continue

                        country = line[0]
                        # lasketaan päästöt per henkilö -indeksi
                        population = get_population(year, country)
                        emissions = float(line[index_year])
                        emissions_percapita = emissions / population
                        #data = make_data(line[0], float(line[index_year]))
                        data = make_data(line[0], emissions_percapita)
                        data_list.append(data)
                    else:
                        continue
            
            # lajitellaan maiden lista niin, että suurimmat päästöt ovat ensimmäisinä
            sorted_data_list = sorted(data_list, key=lambda Data: Data.y, reverse=True)

            print(sorted_data_list) 

            # tarkistetaan, tuliko listalle edes mitään, arvo välitetään fronttiin, jotta tiedetään, näytetäänkö virheilmoitus
            values_amount = len(sorted_data_list) 

            print(values_amount)
        
        return render_template('browse.html', data_years=years, data_year=year, all_data=sorted_data_list, data_values=values_amount)


@app.route('/co2-emissions/search', methods=["GET", "POST"])
def search():
    if request.method == "GET":
        #country = countryname.capitalize()
        countries = get_country_list()
        countries.sort()
        return render_template('search.html', country_list=countries)

    elif request.method == "POST":
        print(request)
        country = request.form['country']
        print(country)
        countries = get_country_list()
        countries.sort()
        years = get_year_list()
        emissions = get_all_emissions_for_country(country)
        # tarkistetaan, tuliko listalle edes mitään, arvo välitetään fronttiin, jotta tiedetään, näytetäänkö virheilmoitus
        values_amount = check_data_values(emissions)
        return render_template('search.html', emissions_for_country=emissions, data_years=years, country_list=countries, country_name=country, data_values=values_amount)


@app.route('/co2-emissions')
def main():

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)