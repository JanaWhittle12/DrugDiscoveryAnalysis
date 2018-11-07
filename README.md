# DrugDiscoveryAnalysis

This project is to analyze the results of molecular dynamic(MD) simulations of four G protein-coupled receptors. 
During the MD simulations of each protein, a snapshot of it's conformation was taken every 200 ps. Then further 
MD simulations were performed to determine which conformations showed binding affinity for an extensive library of 
well-known ligands. Finally descriptive properties of each of the time-stamped conformations was obtained.

The analysis portion of the project will determine data-analysis methods applied to these protein
conformation properties can be used to determine optimal binding conformations. First data reduction
methods is performed including, PCA, LDA and random sampling. Then several 
clustering techniques; logistic regression, SVM, Naive-Bayes and neural networks,
are used to distinguish binding conformations. Finally, agnostic methods of clustering 
are used to find similarities between confomations, such as k-means, or PCM.