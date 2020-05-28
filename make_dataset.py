
import pandas as pd
import sys 
import xml.etree.ElementTree as ET
from pathlib import Path
import requests, zipfile, io, os, zipfile


data_path = Path(__file__).parent / "data/interim/data.pickle"

def tale_iterator( et, verbose = False ):
    current_agenda_id = None
    missing_observations = 0
    found_observations = 0

    for element in et.iter():
        if element.tag == 'Tale':
            observation = {x.tag : x.text for x in element}
            observation.update( { 'Dagsordenpunkt' : current_agenda_id } )

            if not 'Tekst' in  observation or observation['Tekst'] is None:
                missing_observations += 1
            else:
                found_observations += 1
                yield observation

        elif element.tag == 'Dagsordenpunkt':
            current_agenda_id = element.text

    if verbose:
        print('Successfully read %d speeches, found %d to be missing.' % \
            (found_observations, missing_observations))


if __name__ == '__main__':
    print('Creating data folder structure')
    os.mkdir('data/')
    os.mkdir('data/external')
    os.mkdir('data/interim')
    os.mkdir('data/processed')
    os.mkdir('data/raw')

    print('Downloading zip online... ', end=' ')
    zip_file_url = "https://repository.clarin.dk/repository/xmlui/bitstream/handle/20.500.12115/8/FT-data-DSpace.zip?sequence=1&isAllowed=y"
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    print('Dowloading finished!')

    print('unzipping downloaded data ... ', end=' ')
    for file in os.listdir('FT-data-DSpace/'):
        with zipfile.ZipFile('FT-data-DSpace/' + file, 'r') as zip_ref:
            zip_ref.extractall('data/raw/')

    for file in os.listdir('FT-data-DSpace/'):
        os.remove('FT-data-DSpace/' + file)
    os.rmdir('FT-data-DSpace/') 
    print('Unzipping done! ')


    df = pd.DataFrame()
    
    #%% Reading data from each file, appending each 'Tale' entry to dataframe
    for file in os.scandir(Path.cwd() / Path(r'data/raw')):
        if file.path.endswith('.xml'):
            print(f"Processing file: {file.name}")
            et = ET.parse(file)
            df = df.append( list( tale_iterator(et, verbose=True) ) )
    
    #%% Proper datatypes, sorting

    print('Sorting data according to time...', end=' ')
    df['Starttid'] = pd.to_datetime(df['Starttid']).apply(lambda x: x.date())
    df['Sluttid'] = pd.to_datetime(df['Sluttid']).apply(lambda x: x.date())
    print('Done!')

    df.sort_values('Starttid', inplace=True)
    df.reset_index(inplace=True, drop=True)

    #%% Pickling
    print("Saving to pickle...", end=' ')
    df.to_pickle( data_path )
    print("Done!")

else:

    df = pd.read_pickle( data_path )
    