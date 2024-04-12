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
map_response_to_keyword <- function(config_data, response_data) {
  # Merge configuration with responses, keeping the order of response_data
  merged_data <- merge(response_data, config_data, 
                       by.x = "question_id", 
                       by.y = "input_id", 
                       sort = FALSE)
  
  # Map responses to keyword values and filter for the selected response
  # We will use 'merged_data' directly to ensure column references are correct
  result_data <- merged_data %>%
    filter(option == response) %>%
    select(question, input_id = question_id, response, keyword) %>%
    distinct()  # Ensure we have unique rows for each question-response pair
  
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
      result_df <- map_response_to_keyword(df_questionnaire, df_responses)
      readr::write_csv2(result_df, "questionnaire_responses.csv")
      print(result_df)
      result_df
    })
  })
}


## Run the application ---------------------------------------------------------
shiny::shinyApp(ui = ui, server = server)



