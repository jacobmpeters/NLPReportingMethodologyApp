# Instructions for Implementing the NLP Reporting Shiny App

## Overview
This Shiny app allows users to load a questionnaire configuration from a CSV file, display the survey using the `shinysurveys` package, and save the responses to a CSV file. Follow the steps below to set up, run, and customize the app.

---

## Prerequisites

1. **R Installation**:
   - Ensure R is installed on your system. Download it from [CRAN](https://cran.r-project.org/).

2. **Required R Packages**:
   - The app uses the following packages:
     - `shiny`
     - `shinysurveys`
     - `readr`
     - `dplyr`
   - Missing packages will be installed automatically when the script is run.

3. **Input File**:
   - There is a questionnaire configuration CSV file named `questionnaire_config.csv` in the same directory as the script. If modified, the file must still include the following columns:
     - `section`, `question`, `option`, `input_type`, `input_id`, `dependence`, `dependence_value`, `required`, `keyword`

---

## Steps to Implement

### 1. **File Preparation**
   - Place the `questionnaire_config.csv` file in the same directory as `scoring_app.R`.

### 2. **Running the Application**
   - Open RStudio or an R terminal.
   - Navigate to the directory containing `scoring_app.R` and `questionnaire_config.csv`.
   - Execute the command: `shiny::runApp('scoring_app.R')` (Ensure the working directory is correctly set).

### 3. **Interacting with the App**
   - The app will display a survey based on the configuration provided in `questionnaire_config.csv`.
   - After filling out the survey, click the **Submit** button to save responses.

### 4. **Output**
   - Responses are saved in a file named `questionnaire_responses.csv` in the same directory.
   - The output includes the following columns:
     - `question`, `input_id`, `response`, `keyword`

---

## Troubleshooting

1. **Missing or Incorrect Questionnaire File**:
   - Ensure the `questionnaire_config.csv` file is present and includes all required columns.
   - If you're customizing, use the provided sample configuration to verify your customized format.

2. **Error in Package Installation**:
   - If the automated installation does not work, manually install missing packages by running:
     ```R
     install.packages(c("shiny", "shinysurveys", "readr", "dplyr"))
     ```

3. **File Permission Issues**:
   - Ensure the directory has write permissions for the app to save `questionnaire_responses.csv`.

4. **Survey Submission Errors**:
   - Confirm that all required fields in the survey are filled before submitting.
   - Check the console for detailed error messages.
