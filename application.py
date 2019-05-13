from flask import Flask
from flask import request
import csv

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hei vain'

def calculate_total_emissions():
    emissions = 0
    return emissions

def calculate_emissions_per_capita():
    emissions_per_capita = 0
    return emissions_per_capita

def get_population(country, year):
    return country

@app.route('/testi')
def main():
    with open ('./data/CSV/population-data.csv', 'r') as population_csv:
        readCSV = csv.reader(population_csv, delimiter=',')
        country = 'Austria'
        input_year = '1990'
        for row in readCSV:
                 numOfLines = readCSV.line_num
                 if numOfLines == 5:
                    headers = row
                    print(headers)
                    index_year = headers.index(input_year)
                 if numOfLines > 5:
                    # tarkistetaan, vastaako rivin maa kysyttyä maata
                    if row[0] == country:
                        # tulokseksi saadaan kysytyn vuoden väkiluku
                        result = row[index_year]
                        print(result)
                        print ('In ' + country + ' population in the year ' + input_year + ' was ' + result + '.')
    return 'tattadadaa' + result


if __name__ == '__main__':
    app.run()