#' NLP Reporting App
#' 
#' Author: Jake Peters
#' Date: April 9, 2024
#' Description: This Shiny app loads a questionnaire configuration from a CSV 
#' file, displays it using the shinySurveys package, and saves the responses to 
#' a CSV file.

# Load necessary libraries
library(shinysurveys)
library(readr)

# Read questionnaire configuration from CSV file
questionnaire_df <- readr::read_csv("questionnaire_config.csv")

# Define the UI components
ui <- shiny::fluidPage(
  shinysurveys::surveyOutput(
    questionnaire_df,
    survey_title = "Clever Name:",
    survey_description = "An NLP Reporting Methodology Questionnaire"
  ),
  card(
    card_title(markdown("\n\n## Results: ")),
    card_body(
      tableOutput("response_data")
    )
  )
)

# Define the server logic
server <- function(input, output, session) {
  # Render the survey
  renderSurvey()
  
  # Define observer for submit button
  observeEvent(input$submit, {
    # Store rendered data table as an output variable
    output$response_data <- renderTable({
      # Get the survey data
      df_responses <- getSurveyData()
      # Write responses to CSV file
      readr::write_csv2(df_responses, 'questionnaire_responses.csv')
      df_responses
    })
  })
}

# Run the application
shiny::shinyApp(ui = ui, server = server)
