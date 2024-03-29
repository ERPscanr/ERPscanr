---
layout: default
---

# Methods

In order to collect the literature data, search terms for ERP components and association terms were curated, and then used to identify relevant articles in the literature. Information and text from these articles was then collected, and used to analyze patterns and properties of ERP-related articles, and how terms of interest co-occur in the literature.

The main methods for this project are briefly summarized in the following graphic:

![methods]({{ site.baseurl }}/assets/FIGS/overview.png){: width="500" }

Code for this project is written in Python, and primarily uses the
[LISC](https://github.com/lisc-tools/lisc) module for data collection and analysis.
All the code to run this project is openly available in the
[project repository](https://github.com/ERPscanr/ERPscanr).

## Search Terms

To collect information on ERP-related articles, lists of search terms were manually curated. These lists include the names of included ERP components, as well as potential associations, including cognitive and disorder-related terms. The full set of search terms used is available in the
[terms folder](https://github.com/ERPscanr/ERPscanr/tree/main/terms).

In order to ensure the searches found articles specific to ERPs, rather than potential homophones, search terms were manually checked and ERP-specific exclusion words were curated to tune the search results. These exclusion terms restrict search results to the relevant literature, (for example, for some components, we use an exclusion word of 'protein' to avoid articles examining proteins that happen to have the same label as an ERP component).

## Literature Collection

Using these terms, the PubMed E-Utilities were used to return data on relevant articles, and to search for term co-occurrences. Specifically, E-Search was used to identify IDs for relevant articles, and to extract the number of relevant articles, and E-Fetch was used to retrieve data regarding these articles.

Data collection was done in two ways. In the "words" collection, search terms were used to collect available meta-data for all articles mentioning a particular ERP, including title, journal, author, publication date, keywords, and abstract text. In addition, in the co-occurrence analysis we collected data on the number of articles returned by a combination of search terms (for example, counting the number of IDs returned by the search for "N400"AND"language").

The code used to run the literature collections is available in the
[scripts folder](https://github.com/ERPscanr/ERPscanr/tree/main/scripts).

## Data-Driven Profiles

For each ERP, we create a data-driven profile, based on the collected text, using simple text analyses to find the most common words that are used to describe each component, as well as some historical context regarding when, where, and by whom this component has been investigated in the literature.

The full set of data-driven profiles for each component is available
[here](https://erpscanr.github.io/ERPscanr/words.html).

## Group Analysis

We also examined similarities between different ERP components, computing similarity and clustering metrics on the collected data.

The results of these group level analyses are available on the
[network](https://erpscanr.github.io/ERPscanr/network.html),
[cognition](https://erpscanr.github.io/ERPscanr/cognitive.html)
[disorders](https://erpscanr.github.io/ERPscanr/disorders.html)
pages.

The code that performs these analyses is available in the
[project notebooks](https://github.com/ERPscanr/ERPscanr/tree/main/notebooks).

## Limitations

Note that this project is explicitly a summary of the literature, and will share any limitations of the underlying literature.
Limitations include that articles are identified by terms of interest, which can include primary research and review articles,
and no weighting is done for sample size, experiment design, or research quality. We also note that this analysis only reflects
a subset of the literature, in particular articles that reference terms of interest in their titles and/or abstracts.

In the text analyses, we only access limited information including only words which occur in the title, keywords and abstract,
as well as certain meta-data such as journal, authors, and publication date. The current collection and analysis does not include
full-text analysis, and so is only getting a limited insight into the collected articles. In the co-occurrence analyses,
we note that while co-occurrence can be useful to identify which topics are discussed together (or at least nearby),
this approach does not reflect if or how such terms are actually associated.

Due to these limitations, this project should perhaps best be thought of as a high-level overview of the literature,
rather than as a detailed summary of the topics under question. This analysis will share the biases of the literature,
including being susceptible to trends and popularity in research, as well as publication bias. While this kind of "birds eye view"
may be useful to identify general patterns in the literature, we note that detailed conclusions should be further explored for verification.
