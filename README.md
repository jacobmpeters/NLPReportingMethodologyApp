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
    BMS{Background Measurement\n Study Completed?} -- Yes --> SD;
    SD{SD: Study disseminated?} -- Yes --> REF{REF: Reference?};
    REF -- Yes --> AQ1[[AQ1, BMS::SD::REF::INHERIT::1]]
    REF -- No --> EM{EAMP: Evaluation &\n Methods Provided?}
    EM -- DESC: Description of Evaluation and Methods --> AQ2_A[[AQ2, BMS::SD::EAMP::DESC::1]]
    EM -- DOI: Location (DOI or Equivalent) provided --> AQ2_B[[AQ2, BMS::SD::EAMP::DOI::1]]
    SD -- No --> EM2{EAMP: Evaluation &\n Methods Provided?}
    EM2 -- DESC: Description of Evaluation and Methods --> AQ3_A[[AQ3, BMS::SND::EAMP::DESC::1]]
    EM2 -- DOI: Location (DOI or Equivalent) provided --> AQ3_B[[AQ3, BMS::SND::EAMP::DOI::1]]
    EM2 -- None --> NLPS{NLP: NLP Summary?}
    NLPS -- DESC: Description of Evaluation and Methods --> AQ4_A[[AQ4, BMS::SND::NLP::DESC::1]]
    NLPS -- DOI: Location (DOI or Equivalent) provided --> AQ4[[AQ4, BMS::SND::NLP::DOI::1]]
    BMS -- No --> BMS0[[BMS::0]]
```
