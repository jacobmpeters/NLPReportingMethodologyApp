# NLPReportingMethodologyApp
Development of a NLP Reporting Methodology App for the OHDSI Network.

## Meeting Notes:
Meeting notes can be kept in the _Wiki_ tab (for now).

## Issues
- Tasks can be managed as _Issues_
- Progress can be tracked in the _NLPReportingMethodologyApp_ project under the _Projects_ tab. 

## Scoring System and Reporting Methodology
- The scoring system and reporting methodology will be developed at the following source by Daniel Smith:

https://github.com/OHDSI/NLPTools/wiki/NLP-Validation-within-an-OHDSI-Framework

## Decision Tree
```mermaid
flowchart LR
    BMS{Background Measurement\n Study Completed?} -- Yes\n (BMS::1) --> SD{Study disseminated?};
    SD -- Yes\n (BMS::SD::1) --> REF{Reference Provided?};
    REF -- Yes --> AQ1[[Keyword output - BMS::SD::REF::1]]
    REF -- No --> EM{Evaluation &\n Methods Provided?};
    SD -- Yes\n (BMS::SD::1) --> EM
    EM -- Yes, via Description\n of Evaluation/Methods --> AQ2_A[[Keyword output - BMS::SD::EAMP::DESC::1]]
    EM -- Yes, via location\n of Evaluation/Methods\n (DOI or Equivalent) --> AQ2_B[[Keyword output - BMS::SD::EAMP::DOI::1]]
    SD -- No\n (BMS::SND::1) --> EM2{EAMP: Evaluation &\n Methods Provided?};
    EM2 -- Yes, via Description\n of Evaluation/Methods --> AQ3_A[[Keyword output - BMS::SND::EAMP::DESC::1]]
    EM2 -- Yes, via location\n of Evaluation/Methods\n (DOI or Equivalent) --> AQ3_B[[Keyword output - BMS::SND::EAMP::DOI::1]]
    EM2 -- No --> NLP2{NLP Summary?};
    NLP2 -- Yes, via Description\n of NLP pipeline --> AQ4_A[[Keyword output - BMS::SND::NLP::DESC::1]]
    NLP2 -- Yes, via location\n of NLP pipeline (DOI or Equivalent) --> AQ4_B[[Keyword output - BMS::SND::NLP::DOI::1]]
    BMS -- No --> BMS0[[Keyword output - BMS::0]]
```
