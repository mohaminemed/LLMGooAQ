# LLMGooAQ
**LLMGooAQ** is a comprehensive database encompassing diverse questions and answers across 20 domains and contexts. To prepare LLMQooAQ, we randomly sample 10K tuples from the GooAQ dataset and conduct inferences using seven LLMs ("Alpaca-13b", "Llama-2-13b", "Chatglm-6b", "Fastchat-t5-3b", "Koala-13b", "Vicuna-7b", "Vicuna-13b").


**Typical Usage Scenarios**
LLMGooAQ can be used to perform both human and automated evaluations by applying various methods such as pairwise comparison, single answer rating, or reference-guided rating to assess the credibility of LLMs. 


**LLMGooAq Data**
To obtain the data, consult the data/ directory. Note that the data is stored via git-lfs. If you clone the project (git clone git@github.com:allenai/gooaq.git), make sure you also run git lfs pull.

Each line of the data file should look like this:

- comment utiliser la dataset
- exemple de plusieurs questions
- Quelques statistiques
- Comment lire la base de données
- 
