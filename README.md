# 42186 MODEL-BASED MACHINE LEARNING PROJECT
This Github Repo contains two python scripts used to download, make, and preprocess the The Danish Parliament Corpus 2009 - 2017 dataset.
       


Build environment

<pre><code>
conda env create -f environment.yml
conda env update
</code></pre>

Download and make the data set
<pre><code>
python make_dataset
</code></pre>

Preprocess the data set
<pre><code>
python build_features
</code></pre>