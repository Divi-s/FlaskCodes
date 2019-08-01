# FlaskCodes
This folder contains scripts for computing Spearman coefficient to determine similarity for Wordsim353 dataset.
It contains three scripts which should be run in the following order:

1) saveESAConceptVectors.py
    This file takes the word pairs, gets their concept vectors from ESA service and saves the following:
    w1_concepts, w1_relevance, w1_dict, w2_concepts, w2_relevance, w2_dict, uniqueConceptsTfidfDict and humanScore for this wordpair

    Run the script using:
    python3 saveESAConceptVectors.py 
    
    Parameters while running:
    a) --rawDataPath : Path to csv file containing word pairs and human scores.
    b) --conceptVecPath : Path to the folder where the concept vectors will be saved
    c) --conceptVecLength : Maximum length of the concept vector
    
2) saveVandUvectors.py
    This file first loads the saved concept vectors and their tf-idf for a given word. Then for each word pair, arranges the common concepts at front in decreasing order of relevance for low entropy word.
    It then performs gsnorm on the concept vectors and saves the resulting vectors.
    
    Run the script using:
    python3 saveVandUvectors.py 
    
    Parameters while running:
    a) --rawDataPath : Path to csv file containing word pairs and human scores.
    b) --conceptVecPath : Path to the folder where the concept vectors were saved
    c) --VandUvecPath : Path to the folder where the vectors after gsnorm will be saved
    
3) findCoeff.py
    This file first loads the saved concept vectors and their tf-idf for a given word. Then for each word pair, arranges the common concepts at front in decreasing order of relevance for low entropy word.
    It then performs gsnorm on the concept vectors and saves the resulting vectors.
    
    Run the script using:
    python3 findCoeff.py
    
    Parameters while running:
    a) --rawDataPath : Path to csv file containing word pairs and human scores.
    b) --savedVecPath : Path to the folder where the concept vectors were saved
    c) --newRelPath : Path to save the new relevance scores after gsnorm
    d) --coeffSavePath : Path to save the coefficients

   
