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
    BMS{Background Measurement\n Study Completed?} -- Yes --> BMS_T[[Keyword output - BMS::1]] --> SD{Study disseminated?};
        SD -- Yes --> SD_T[[BMS-SD::1]] --> REF{Reference Provided?};
            REF -- Yes --> AQ1_T[[BMS-REF::1]] --> EM{Evaluation &\n Methods Provided?};
                EM -- Yes --> EM_T[[BMS-EM::1]]
                    EM_T -- ...via Description --> EM_DESC[[BMS-EM-DESC::1]]
                    EM_T -- ...via Location\n (DOI or Equivalent) --> EM_DOI[[BMS-EM-DOI::1]]
                    EM_T --> NLP1{NLP Pipeline\n Summary Provided?};
                        NLP1 -- Yes --> NLP1_T[[BMS-NLP::1]]
                        NLP1_T -- ...via Description --> AQ3_A[[BMS-NLP-DESC::1]]
                        NLP1_T -- ...via Location\n (DOI or Equivalent) --> AQ3_B[[BMS-NLP-DOI::1]]
                        NLP1 -- No --> NLP1_F[[BMS-NLP::0]]
                EM -- No --> EM_F[[BMS-EM::0]] --> NLP1
            REF -- No --> AQ1_F[[BMS-REF::0]] --> EM
        SD -- No --> SD_F[[BMS-SD::0]] --> EM
    BMS -- No --> BMS_F[[Keyword output - BMS::0]]
```
