from flask import Flask
from flask import request
from flask import render_template
import csv

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hei vain'


# metodit, joilla saadaan koko maailman kokonaismäärä populaation ja saasteiden osalta
# tietylle vuodelle

@app.route('/totalemissions')
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

        # tähän joku metodi, joka ottaa annetun vuoden,
        # ja etsii emissions-tiedostosta kyseisellä indeksillä
        # jokaisen maan arvon ja yhdistää ne kokonaismääräksi
        # jonkinlainen for-looppi joka kasvattaa arvoa kunkin rivin jälkeen
    return formatted_total_emissions

@app.route('/totalpopulation')
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
        6,542,159,383

    return str(total_population)
    
    # tähän joku metodi, joka ottaa annetun vuoden,
    # ja etsii population-tiedostosta kyseisellä indeksillä
    # jokaisen maan arvon ja yhdistää ne kokonaismääräksi
    # jonkinlainen for-looppi, joka kasvattaa arvoa kunkin rivin jälkeen
    



# metodit, joilla listataan maat järjestykseen joko saastemäärän tai saastemäärä
# per henkilö perusteella

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

@app.route('/getpopulation')
def get_population(): #parametrit year ja country
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
                    # tulokseksi saadaan kysytyn vuoden väkiluku
                    population = line[index_year]
                    print(population)
                    print('In ' + country + ' population in the year ' + year + ' was ' + population + '.')

    return population

@app.route('/getemissions')
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
                    print('In ' + country + ' the emissions of the year ' + year + ' were ' + emissions + ' kilotonnes.')

    return emissions

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
    with open ('./data/CSV/population-data.csv', 'r') as population_csv:
        csv_reader = csv.reader(population_csv, delimiter=',')
        countries = []
        for line in csv_reader:
            line_number = csv_reader.line_num
            if line_number > 5:
                countries.append(line[0])
        print(countries)
    return countries


@app.route('/co2-emissions')
def main():
    countries = get_country_list()
    print(countries)
    return render_template('index.html', country_list=countries)



if __name__ == '__main__':
    app.run(debug=True)