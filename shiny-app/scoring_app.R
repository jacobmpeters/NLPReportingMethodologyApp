#' NLP Reporting App
#'
#' Author: Jake Peters
#' Date: April 9, 2024
#' Description: This Shiny app loads a questionnaire configuration from a CSV
#' file, displays it using the shinysurveys package, and saves the responses to
#' a CSV file.


## Load necessary libraries ---------------------------------------------------
required_packages <- c("shiny", "shinysurveys", "readr", "dplyr")
missing_packages  <- setdiff(required_packages, installed.packages()[, "Package"])

# Install missing packages if needed
if (length(missing_packages) > 0) { install.packages(missing_packages)}

# Load required packages
invisible(sapply(required_packages, library, character.only = TRUE))


## Read questionnaire configuration from CSV file ------------------------------
df_questionnaire <- readr::read_csv("questionnaire_config.csv")


## Helper Functions ------------------------------------------------------------

# Function to map responses to keyword values and return specific columns
map_responses_to_keyword <- function(config_data, response_data) {
  # Merge configuration with responses
  merged_data <- merge(config_data, response_data, by.x = "input_id", by.y = "question_id")
  
  # Map responses to keyword values and filter for the selected response
  # Assume response_data has columns 'question_id' and 'response'
  # and config_data has 'input_id', 'option', and 'keyword'
  result_data <- merged_data %>%
    filter(option == response) %>%
    distinct(question, input_id, response, keyword, .keep_all = TRUE) %>%
    select(question, input_id, response, keyword)
  
  return(result_data)
}


## Define the UI components ----------------------------------------------------
ui <- shiny::fluidPage(
  shinysurveys::surveyOutput(
    df_questionnaire,
    survey_title = "Clever Name:",
    survey_description = "An NLP Reporting Methodology Questionnaire"
  ),
  shiny::tableOutput("response_data")
)


## Define the server logic -----------------------------------------------------
server <- function(input, output, session) {
  shinysurveys::renderSurvey()

  # Define observer for submit button
  shiny::observeEvent(input$submit, {
    # Store rendered data table as an output variable
    output$response_data <- shiny::renderTable({
      df_responses <- shinysurveys::getSurveyData()
      result_df <- map_responses_to_keyword(df_questionnaire, df_responses)
      readr::write_csv2(result_df, "questionnaire_responses.csv")
      print(result_df)
      result_df
    })
  })
}


## Run the application ---------------------------------------------------------
shiny::shinyApp(ui = ui, server = server)



