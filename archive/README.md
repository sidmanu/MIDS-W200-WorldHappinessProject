# 200 Project Proposal
### Team Members
[Aaron Lin](https://github.com/linaaron88), [Siddharth Manu](https://github.com/sidmanu), [Stephanie Andrews](https://github.com/jellomoat)
### Repo
Current: [Project2_Andrews_Lin_Manu](https://github.com/UC-Berkeley-I-School/Project2_Andrews_Lin_Manu)

Will later be renamed: sf-emergency-response-times

### Primary Dataset
[Law Enforcement Dispatched Calls for Service: Closed](https://data.sfgov.org/Public-Safety/Law-Enforcement-Dispatched-Calls-for-Service-Close/2zdj-bwza/) ([Documentation](https://sfgov.org/scorecards/public-safety/police-response-serious-incidents))
### Secondary Datasets
* [Police Department Incident Reports: 2018 to Present](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783) ([Documentation](https://datasf.gitbook.io/datasf-dataset-explainers/sfpd-incident-report-2018-to-present))
* [Census Data](https://data.census.gov/table?t=Income%20and%20Poverty&g=050XX00US06075,06075$8600000_860XX00US94102,94103,94104,94105,94107,94108,94109,94110,94111,94112,94114,94115,94116,94117,94118,94121,94122,94123,94124,94127,94129,94130,94131,94132,94133,94134,94158,94188,941HH,941XX,94501,94920)
* [SF Map Geojson](https://data.sfgov.org/Geographic-Locations-and-Boundaries/SF-Find-Neighborhoods/pty2-tcw4)
* [SF Redlining Map Geojson](https://dsl.richmond.edu/panorama/redlining/#loc=5/39.1/-94.58&text=downloads)
### Goals
* Analyze incident/crime rates by location and severity
* Characterize current DEM response times and internal (intrinsic) factors that may impact them; eg personnel capacity, proximity
* Identify external factors that may influence response times; eg demographics, wealth
### Research Questions and EDA Plan
| Priority | Topics/Variables                                             | Questions                                                    | Viz Types                                  |
|----------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------|
| 1        | - `response_time`<br>vs<br>- `incident_severity`<br>- `incident_type`<br><br>* split by department, fire/ems/police | How does emergency response time relate to incident type/severity? | line<br>bar chart                          |
| 1        | - `response_time`<br>vs<br>- `incident_zipcode`              | How does response time relate to location?<br><br>Are there parts of the city that have better emergency response times? | map<br>bar chart<br>box plot               |
| 1        | - `response_time`<br>vs<br>- `incident_month`<br>- `incident_year` | How has emergency response times changed over the years?<br><br>How does response time vary by month?  What are possible factors for variance? | heat map<br>trend line                     |
| 1        | - `response_time`<br>vs<br>- `day`<br>- `time`               | What are patterns of emergency response with regards to day of the week and to time? | heat map<br>bar chart                      |
| 1        | - `response_time`<br>vs<br>- `police_district`<br>- `police_analysis_neighborhood`<br> | Do certain areas have better emergency response coverage, eg related to police?<br><br>How might that impact response time?<br><br>How does that relate to departmental budgets? | bar chart<br>map                           |
| 2        | - `response_time`<br>vs<br>- `population_size`               | How might population size/density impact response time?      | map<br>scatter plot                        |
| 2        | - `response_time`<br>vs<br>- `race_area_demo` (TBD)<br>- `percent_minority`(?) | How do race and ethnicity relate to response time?<br><br>Is there a correlation between emergency response times and a greater concentration of minority residents in an area? | scatter plot<br>line                       |
| 2        | - `response_time`<br>vs<br>- `median_household_income`<br>- `mean_household_income`<br>- `income_per_capita`(?) | Do wealthier areas have better police response times?        | map w/ layers<br>bar chart                 |
| 2        | - `response_time`<br>vs<br>-`redlined_district`              | Do areas that have been historically redlined(have higher HOLC grades) have higher response times? | GeoJSON map                                |
| 3        | Analysis of high-risk areas and call volume/times<br><br>Crimes grouped by `incident_category`, `analysis_neighborhood`, `zipcode` | When and where are communities most at risk/most likely to be in need of emergency response?<br><br>Reference violent vs nonviolent crimes | heat map<br>bar chart<br>map<br>others tbd |
| 3        | - `response_time`<br>vs<br>- `police_capacity`<br>- `budget_dem`<br>- `budget_police`<br>- `budget_fire`<br>- `total_budget`<br> | How does police capacity and budget allocated play a role in response times? | Line graph                                 |

### Report Structure
* Background and Context
  * Related news articles
  * State response time requirements
  * Audience: policy makers, public, businesses
  * Defining data sources, schemas
  * Response times: time between call received and time on scene
* Summary of research questions and sub-questions
* Crime rates and risk
  * Analysis of high-risk areas and call volume/times
  * Crimes grouped by `incident_category`, `analysis_neighborhood`, `zipcode`
  * Visualization ideas: heat map, bar chart
* Average response times:
  * `call_received_dt`, `call_dispatched_dt`, `call_onscene_dt`
  * `number_minutes` (bucket), `incident_count` - trend lines, bar chart
  * `call_type`, `call_priority` - trend lines, bar chart
* Current response times in relation to internal factors:
  * `incident_severity`, `incident_type` - line, bar chart
  * `incident_zipcode` - map, bar chart, box plot
  * `month`, `year`- heat map, trend line
  * `day`, `time` - heat map, bar chart
  * `police_district`, `police_analysis_neighborhood`; `police_capacity_by_district` if available - bar chart, map
  * `budget_dem`, `budget_police`, `budget_fire`, `total_budget`
* Current response times in relation to external factors:
  * `redlined_district`, GeoJSON - map
  * `population_size` - map, scatter plot
  * `race_area_demo` (TBD), `percent_minority`(?) - scatter plot, line
  * `median_household_income`, `mean_household_income`, `income_per_capita`(?) - map w/ layers, bar chart
* Implications and Further Analysis
  * Impact on businesses, loss of life, etc.
  * Additional factors - traffic, cell signal
  * Actionable insights