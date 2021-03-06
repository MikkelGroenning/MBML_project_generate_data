# 42186 MODEL-BASED MACHINE LEARNING PROJECT
This Github Repo contains two python scripts used to download, make, and preprocess the The Danish Parliament Corpus 2009 - 2017 dataset.
Use the following command in the following order.

1. Build environment
<pre><code>
conda env create -f environment.yml
conda env update
</code></pre>

2. Download and make the data set
<pre><code>
python3 src/data/make_dataset.py
</code></pre>

3. Preprocess the data set
<pre><code>
python3 src/features/build_features.py
</code></pre>

This will generate
- vocabulary: a dictionary of all the words and corrosponding number
- X: a bag of words representation of the data
- X_tfidf: a bag of words representation of the data where the words of been weighted accordingly to TFIDF measure
- corpus: A list of tuples for each speech that contains the word and number of times the word were used.
- corpus_tfidf: A list of tuples for each speech that contains the word and TFIDF weight of times the word were used.


After running the command the folder structure should look like the following:
<pre><code>
├── README.md       
├── data
│   ├── external       <- Intermediate data that has been transformed. (contains the stop words)
│   ├── interim        <- The original, immutable data dump. (created from make_dataset)
│   ├── processed      <- Intermediate data that has been transformed. ( vocabulary, X, X_tfidf, corpus, corpus_tfidf)
│   └── raw            <- The original, immutable data dump. (contain the raw unzipped xml files)
│
├── scr
│   ├── data 
│   │    ├── make_dataset
│   │
│   ├── features
│   │    ├── build_features 
│
├── notebook
│   ├── project.ipynb
│
├── setup.py
├── Enviroment.yml
├── stopord.txt
</code></pre>
