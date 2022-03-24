# Executive Summary

A data dictionary and descriptive statistics were prepared based on the
Pesticide Labels Now (PLN) [analysis
plan](https://docs.google.com/document/d/1mUHPYdpWljCWroODGenUjYlyae2ZWwqN4MScBLXlr2U/edit).
For a better representation of users, we ignored a list of random
identifiers (‘aid’ in *ignores.csv*) associated with the project team
members and generated descriptive statistics for three subsets:

-   evDownload.01
-   evStart
-   evViewPage.01

# Data Dictionary

## evDownload.01 subset

Unique devices (aid)

    print(n_distinct(evDownload.01$aid), style="rmarkdown")

    ## [1] 93

<table>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>aid</td>
<td>Random device identifier</td>
</tr>
<tr class="even">
<td>epaReg</td>
<td>EPA regsistration number</td>
</tr>
<tr class="odd">
<td>prodName</td>
<td>Pesticide product name</td>
</tr>
<tr class="even">
<td>sourcePage</td>
<td>App page visited?</td>
</tr>
<tr class="odd">
<td>evType</td>
<td>Action taken on app (download)</td>
</tr>
<tr class="even">
<td>ts</td>
<td>Timestamp yyy:mm:dd:hh:mm:ss</td>
</tr>
</tbody>
</table>

## evStart subset

Unique users (aid)

    print(n_distinct(evStart$aid), style="rmarkdown")

    ## [1] 392

<table>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>aid</td>
<td>Random device identifier</td>
</tr>
<tr class="even">
<td>evDesc1</td>
<td>App version?</td>
</tr>
<tr class="odd">
<td>evDesc2</td>
<td>Device type</td>
</tr>
<tr class="even">
<td>evDesc3</td>
<td>GPS coordinates</td>
</tr>
<tr class="odd">
<td>evType</td>
<td>Action taken on app (start page)</td>
</tr>
<tr class="even">
<td>ts</td>
<td>Timestamp yyy:mm:dd:hh:mm:ss</td>
</tr>
</tbody>
</table>

## evViewPage.01 subset

Unique users (aid)

    print(n_distinct(evViewPage.01$aid), style="rmarkdown")

    ## [1] 358

<table>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>aid</td>
<td>Random device identifier</td>
</tr>
<tr class="even">
<td>evDesc1</td>
<td>First action on app</td>
</tr>
<tr class="odd">
<td>evDesc2</td>
<td>English or Spanish</td>
</tr>
<tr class="even">
<td>evDesc3</td>
<td>Pesticide label viewed</td>
</tr>
<tr class="odd">
<td>evType</td>
<td>Action taken on app (view page)</td>
</tr>
<tr class="even">
<td>ts</td>
<td>Timestamp yyy:mm:dd:hh:mm:ss</td>
</tr>
</tbody>
</table>

## Detailed variable descriptions

-   Device = identified by a randomly assigned identifier. = Person.
    Person = device. There is no way to distinguish individual users.
    One device can be used by ≥ 1 person and 1 person can use ≥ 1
    device.
-   Access = accessed app = put PLN on device and opened app (app opens
    to label List).
-   Session = time from when the app opened until just before next time
    it is opened.
-   PICOL Searches = PICOL results viewed.
-   Label searches = Label menu viewed.
-   View = accessed and viewed information (any combination of ≥ 1 of
    the following)
-   Label view = accessed + \[(opened ≥ 1 label) + (opened ≥ 1 menu
    bar)\] Label view + PDF = accessed + \[(opened ≥ 1 label) + (opened
    ≥ 1 menu bar)+ (downloaded label PDF)\]
-   PICOL view = accessed + \[(conducted ≥ 1 PICOL search) + (viewed ≥ 1
    PICOL result)\]
-   PICOL view + PDF = accessed app + \[(conducted ≥ 1 PICOL search) +
    (viewed ≥ 1 PICOL result) + (downloaded app)\]
-   General view = accessed +(viewed label search page + selected a
    label, but did not open menu bar) and/or ( viewed PICOL search page)
    and/or viewed more pages General view + links
-   Location = GPS coordinates. de-identified location in that it is
    somewhere within the ~ 500 ft radius. We will only report by broad
    areas. Agricultural regions if they are defined. Currently, many
    iPhone users are declining location as Apple is asking users if they
    want the location turned on/off with each update. We may only be
    able to evaluate this up to the April release date. App is only
    available to devices registered in the US, CA, and MX. However,
    phones registered in these countries can be used anywhere. For
    example, we had a user connect from S. America from a US registered
    phone.
-   Population A definition: anyone that has accessed the app. There is
    1 excluded population and 3 study subpopulations (based on gps
    location coordinates at time the app is opened.)
    -   Device used in WA state GPS data. (Not Seattle or King County)
    -   Device used outside of WA state
    -   No location (location services are off.)
    -   Exclude. King County or at least the Seattle metropolitan area
        locations. These are likely team and PNASH staff. Exclusion
        list. Selected random devices IDs are on an exclusion list.
        These are test devices.
-   Population B definition: (Only use if enough people respond to in
    app questions). Those users that respond to the location in-app
    question. (This response can be linked to app analytic data as it
    has the same random unique ID). This will be implemented very soon.
    -   Response I work in WA state (not quite the same as where they
        downloaded it)
    -   Response I work outside of Washington state
    -   Do not want to answer
    -   Skips answering the question. (will combine with c)

# Descriptive Statistics

## evDownload.01

## evStart

## evViewPage.01

# App use by location

<img src="Subquestions_files/figure-markdown_strict/user-map-us-1.png" width="100%" />

    ## 
    ## The downloaded binary packages are in
    ##  /var/folders/g8/z7k53ktx0pg62hb1c7cf4h1m0000gn/T//RtmpInwOCE/downloaded_packages

<img src="Subquestions_files/figure-markdown_strict/user-map-wa-1.png" width="100%" />

    ## 
    ## The downloaded binary packages are in
    ##  /var/folders/g8/z7k53ktx0pg62hb1c7cf4h1m0000gn/T//RtmpInwOCE/downloaded_packages

    ##   |                                                                              |                                                                      |   0%  |                                                                              |                                                                      |   1%  |                                                                              |=                                                                     |   1%  |                                                                              |=                                                                     |   2%  |                                                                              |==                                                                    |   3%  |                                                                              |===                                                                   |   4%  |                                                                              |===                                                                   |   5%  |                                                                              |====                                                                  |   5%  |                                                                              |====                                                                  |   6%  |                                                                              |=====                                                                 |   7%  |                                                                              |=====                                                                 |   8%  |                                                                              |======                                                                |   8%  |                                                                              |======                                                                |   9%  |                                                                              |=======                                                               |  10%  |                                                                              |=======                                                               |  11%  |                                                                              |========                                                              |  11%  |                                                                              |========                                                              |  12%  |                                                                              |=========                                                             |  13%  |                                                                              |==========                                                            |  14%  |                                                                              |==========                                                            |  15%  |                                                                              |===========                                                           |  15%  |                                                                              |===========                                                           |  16%  |                                                                              |============                                                          |  16%  |                                                                              |============                                                          |  17%  |                                                                              |============                                                          |  18%  |                                                                              |=============                                                         |  18%  |                                                                              |=============                                                         |  19%  |                                                                              |==============                                                        |  19%  |                                                                              |==============                                                        |  20%  |                                                                              |==============                                                        |  21%  |                                                                              |===============                                                       |  21%  |                                                                              |===============                                                       |  22%  |                                                                              |================                                                      |  22%  |                                                                              |================                                                      |  23%  |                                                                              |================                                                      |  24%  |                                                                              |=================                                                     |  24%  |                                                                              |=================                                                     |  25%  |                                                                              |==================                                                    |  25%  |                                                                              |==================                                                    |  26%  |                                                                              |===================                                                   |  27%  |                                                                              |====================                                                  |  28%  |                                                                              |====================                                                  |  29%  |                                                                              |=====================                                                 |  29%  |                                                                              |=====================                                                 |  30%  |                                                                              |======================                                                |  31%  |                                                                              |======================                                                |  32%  |                                                                              |=======================                                               |  32%  |                                                                              |=======================                                               |  33%  |                                                                              |========================                                              |  34%  |                                                                              |========================                                              |  35%  |                                                                              |=========================                                             |  35%  |                                                                              |=========================                                             |  36%  |                                                                              |==========================                                            |  37%  |                                                                              |==========================                                            |  38%  |                                                                              |===========================                                           |  38%  |                                                                              |===========================                                           |  39%  |                                                                              |============================                                          |  39%  |                                                                              |============================                                          |  40%  |                                                                              |=============================                                         |  41%  |                                                                              |=============================                                         |  42%  |                                                                              |==============================                                        |  43%  |                                                                              |===============================                                       |  44%  |                                                                              |===============================                                       |  45%  |                                                                              |================================                                      |  45%  |                                                                              |================================                                      |  46%  |                                                                              |=================================                                     |  47%  |                                                                              |=================================                                     |  48%  |                                                                              |==================================                                    |  48%  |                                                                              |==================================                                    |  49%  |                                                                              |===================================                                   |  49%  |                                                                              |===================================                                   |  50%  |                                                                              |===================================                                   |  51%  |                                                                              |====================================                                  |  51%  |                                                                              |====================================                                  |  52%  |                                                                              |=====================================                                 |  52%  |                                                                              |=====================================                                 |  53%  |                                                                              |======================================                                |  54%  |                                                                              |======================================                                |  55%  |                                                                              |=======================================                               |  55%  |                                                                              |=======================================                               |  56%  |                                                                              |========================================                              |  57%  |                                                                              |========================================                              |  58%  |                                                                              |=========================================                             |  58%  |                                                                              |=========================================                             |  59%  |                                                                              |==========================================                            |  60%  |                                                                              |===========================================                           |  61%  |                                                                              |===========================================                           |  62%  |                                                                              |============================================                          |  62%  |                                                                              |============================================                          |  63%  |                                                                              |=============================================                         |  64%  |                                                                              |=============================================                         |  65%  |                                                                              |==============================================                        |  65%  |                                                                              |==============================================                        |  66%  |                                                                              |===============================================                       |  66%  |                                                                              |===============================================                       |  67%  |                                                                              |===============================================                       |  68%  |                                                                              |================================================                      |  68%  |                                                                              |================================================                      |  69%  |                                                                              |=================================================                     |  69%  |                                                                              |=================================================                     |  70%  |                                                                              |=================================================                     |  71%  |                                                                              |==================================================                    |  71%  |                                                                              |==================================================                    |  72%  |                                                                              |===================================================                   |  72%  |                                                                              |===================================================                   |  73%  |                                                                              |====================================================                  |  74%  |                                                                              |====================================================                  |  75%  |                                                                              |=====================================================                 |  75%  |                                                                              |=====================================================                 |  76%  |                                                                              |======================================================                |  77%  |                                                                              |=======================================================               |  78%  |                                                                              |=======================================================               |  79%  |                                                                              |========================================================              |  79%  |                                                                              |========================================================              |  80%  |                                                                              |========================================================              |  81%  |                                                                              |=========================================================             |  81%  |                                                                              |=========================================================             |  82%  |                                                                              |==========================================================            |  82%  |                                                                              |==========================================================            |  83%  |                                                                              |===========================================================           |  84%  |                                                                              |===========================================================           |  85%  |                                                                              |============================================================          |  85%  |                                                                              |============================================================          |  86%  |                                                                              |=============================================================         |  87%  |                                                                              |=============================================================         |  88%  |                                                                              |==============================================================        |  88%  |                                                                              |==============================================================        |  89%  |                                                                              |===============================================================       |  90%  |                                                                              |================================================================      |  91%  |                                                                              |================================================================      |  92%  |                                                                              |=================================================================     |  92%  |                                                                              |=================================================================     |  93%  |                                                                              |=================================================================     |  94%  |                                                                              |==================================================================    |  94%  |                                                                              |==================================================================    |  95%  |                                                                              |===================================================================   |  95%  |                                                                              |===================================================================   |  96%  |                                                                              |====================================================================  |  97%  |                                                                              |====================================================================  |  98%  |                                                                              |===================================================================== |  98%  |                                                                              |===================================================================== |  99%  |                                                                              |======================================================================|  99%  |                                                                              |======================================================================| 100%

    ##   |                                                                              |                                                                      |   0%  |                                                                              |                                                                      |   1%  |                                                                              |=                                                                     |   1%  |                                                                              |=                                                                     |   2%  |                                                                              |==                                                                    |   2%  |                                                                              |==                                                                    |   3%  |                                                                              |==                                                                    |   4%  |                                                                              |===                                                                   |   4%  |                                                                              |===                                                                   |   5%  |                                                                              |====                                                                  |   5%  |                                                                              |====                                                                  |   6%  |                                                                              |=====                                                                 |   7%  |                                                                              |=====                                                                 |   8%  |                                                                              |======                                                                |   8%  |                                                                              |======                                                                |   9%  |                                                                              |=======                                                               |   9%  |                                                                              |=======                                                               |  10%  |                                                                              |=======                                                               |  11%  |                                                                              |========                                                              |  11%  |                                                                              |========                                                              |  12%  |                                                                              |=========                                                             |  12%  |                                                                              |=========                                                             |  13%  |                                                                              |=========                                                             |  14%  |                                                                              |==========                                                            |  14%  |                                                                              |==========                                                            |  15%  |                                                                              |===========                                                           |  15%  |                                                                              |===========                                                           |  16%  |                                                                              |============                                                          |  16%  |                                                                              |============                                                          |  17%  |                                                                              |============                                                          |  18%  |                                                                              |=============                                                         |  18%  |                                                                              |=============                                                         |  19%  |                                                                              |==============                                                        |  19%  |                                                                              |==============                                                        |  20%  |                                                                              |==============                                                        |  21%  |                                                                              |===============                                                       |  21%  |                                                                              |===============                                                       |  22%  |                                                                              |================                                                      |  22%  |                                                                              |================                                                      |  23%  |                                                                              |=================                                                     |  24%  |                                                                              |=================                                                     |  25%  |                                                                              |==================                                                    |  25%  |                                                                              |==================                                                    |  26%  |                                                                              |===================                                                   |  27%  |                                                                              |===================                                                   |  28%  |                                                                              |====================                                                  |  28%  |                                                                              |====================                                                  |  29%  |                                                                              |=====================                                                 |  29%  |                                                                              |=====================                                                 |  30%  |                                                                              |=====================                                                 |  31%  |                                                                              |======================                                                |  31%  |                                                                              |======================                                                |  32%  |                                                                              |=======================                                               |  32%  |                                                                              |=======================                                               |  33%  |                                                                              |=======================                                               |  34%  |                                                                              |========================                                              |  34%  |                                                                              |========================                                              |  35%  |                                                                              |=========================                                             |  35%  |                                                                              |=========================                                             |  36%  |                                                                              |==========================                                            |  36%  |                                                                              |==========================                                            |  37%  |                                                                              |==========================                                            |  38%  |                                                                              |===========================                                           |  38%  |                                                                              |===========================                                           |  39%  |                                                                              |============================                                          |  39%  |                                                                              |============================                                          |  40%  |                                                                              |============================                                          |  41%  |                                                                              |=============================                                         |  41%  |                                                                              |=============================                                         |  42%  |                                                                              |==============================                                        |  42%  |                                                                              |==============================                                        |  43%  |                                                                              |===============================                                       |  44%  |                                                                              |===============================                                       |  45%  |                                                                              |================================                                      |  45%  |                                                                              |================================                                      |  46%  |                                                                              |=================================                                     |  46%  |                                                                              |=================================                                     |  47%  |                                                                              |=================================                                     |  48%  |                                                                              |==================================                                    |  48%  |                                                                              |==================================                                    |  49%  |                                                                              |===================================                                   |  49%  |                                                                              |===================================                                   |  50%  |                                                                              |===================================                                   |  51%  |                                                                              |====================================                                  |  51%  |                                                                              |====================================                                  |  52%  |                                                                              |=====================================                                 |  52%  |                                                                              |=====================================                                 |  53%  |                                                                              |=====================================                                 |  54%  |                                                                              |======================================                                |  54%  |                                                                              |======================================                                |  55%  |                                                                              |=======================================                               |  55%  |                                                                              |=======================================                               |  56%  |                                                                              |========================================                              |  57%  |                                                                              |========================================                              |  58%  |                                                                              |=========================================                             |  58%  |                                                                              |=========================================                             |  59%  |                                                                              |==========================================                            |  59%  |                                                                              |==========================================                            |  60%  |                                                                              |==========================================                            |  61%  |                                                                              |===========================================                           |  61%  |                                                                              |===========================================                           |  62%  |                                                                              |============================================                          |  62%  |                                                                              |============================================                          |  63%  |                                                                              |=============================================                         |  64%  |                                                                              |=============================================                         |  65%  |                                                                              |==============================================                        |  65%  |                                                                              |==============================================                        |  66%  |                                                                              |===============================================                       |  67%  |                                                                              |===============================================                       |  68%  |                                                                              |================================================                      |  68%  |                                                                              |================================================                      |  69%  |                                                                              |=================================================                     |  69%  |                                                                              |=================================================                     |  70%  |                                                                              |=================================================                     |  71%  |                                                                              |==================================================                    |  71%  |                                                                              |==================================================                    |  72%  |                                                                              |===================================================                   |  72%  |                                                                              |===================================================                   |  73%  |                                                                              |===================================================                   |  74%  |                                                                              |====================================================                  |  74%  |                                                                              |====================================================                  |  75%  |                                                                              |=====================================================                 |  75%  |                                                                              |=====================================================                 |  76%  |                                                                              |======================================================                |  76%  |                                                                              |======================================================                |  77%  |                                                                              |======================================================                |  78%  |                                                                              |=======================================================               |  78%  |                                                                              |=======================================================               |  79%  |                                                                              |========================================================              |  79%  |                                                                              |========================================================              |  80%  |                                                                              |========================================================              |  81%  |                                                                              |=========================================================             |  81%  |                                                                              |=========================================================             |  82%  |                                                                              |==========================================================            |  82%  |                                                                              |==========================================================            |  83%  |                                                                              |==========================================================            |  84%  |                                                                              |===========================================================           |  84%  |                                                                              |===========================================================           |  85%  |                                                                              |============================================================          |  85%  |                                                                              |============================================================          |  86%  |                                                                              |=============================================================         |  86%  |                                                                              |=============================================================         |  87%  |                                                                              |=============================================================         |  88%  |                                                                              |==============================================================        |  88%  |                                                                              |==============================================================        |  89%  |                                                                              |===============================================================       |  89%  |                                                                              |===============================================================       |  90%  |                                                                              |===============================================================       |  91%  |                                                                              |================================================================      |  91%  |                                                                              |================================================================      |  92%  |                                                                              |=================================================================     |  92%  |                                                                              |=================================================================     |  93%  |                                                                              |==================================================================    |  94%  |                                                                              |==================================================================    |  95%  |                                                                              |===================================================================   |  95%  |                                                                              |===================================================================   |  96%  |                                                                              |====================================================================  |  97%  |                                                                              |====================================================================  |  98%  |                                                                              |===================================================================== |  98%  |                                                                              |===================================================================== |  99%  |                                                                              |======================================================================|  99%  |                                                                              |======================================================================| 100%

<img src="Subquestions_files/figure-markdown_strict/user-map-wa-2.png" width="100%" /><img src="Subquestions_files/figure-markdown_strict/user-map-wa-3.png" width="100%" /><img src="Subquestions_files/figure-markdown_strict/user-map-wa-4.png" width="100%" />

# Device time use patterns

# Dataframe summaries


    ```r
    # creating sessions 
    # Goal: 1327 total sessions from 2020-08-26 through 2021-08-31. This doesn't include any sessions initiated by one of the 'ignored' aids.

    install.packages("dplyr")

    ## 
    ## The downloaded binary packages are in
    ##  /var/folders/g8/z7k53ktx0pg62hb1c7cf4h1m0000gn/T//RtmpInwOCE/downloaded_packages

    library("dplyr")
    install.packages("lubridate")

    ## 
    ## The downloaded binary packages are in
    ##  /var/folders/g8/z7k53ktx0pg62hb1c7cf4h1m0000gn/T//RtmpInwOCE/downloaded_packages

    library("lubridate")

    #filter merged.csv from aid's first "evStart" to the next "evStart"
    merged.csv.dedup <- unique(merged.csv)

    x <- merged.csv.dedup %>% 
      group_by(sessionid = cumsum(evType == 'evStart')) %>% 
      mutate(sessioneventno = row_number())
    # Problem with the code... look at line 1451, 1663 or 4052 (happens VERY rarely)
    # the code restarts the counter every time there is an evStart, however, if there are multiple users utilizing the app at the same time, the session ids and their actions are not distinguished 
    # Solution: remove evType of statechange? I believe active-->nonactive & nonactive-->active is ruining results... actually maybe not 

    x$ts <- ymd_hms(x$ts)

    # Objective: To understand the 'Pesticide Labels Now' movile application user audience and their preferences for app utility. 

    # Primary Research Question: How do user characteristics inform or explain their interaction with the 'Pesticides Labels Now' application? 

    # SubQuestion #1: Which operating systems are utilized to access the application? 

    str(evStart)
    per_data <- evStart %>%
      count(device_cat) %>% 
      mutate(per = n / sum(n),
             per_label = paste0(round(per*100), "%"))

    ggplot(per_data, aes(x = reorder(n, -per), y=per)) + 
      geom_bar(stat = "identity", fill = "darkseagreen1", color = "black") + 
      geom_text(aes(label=per_label), vjust=-0.25) + 
      labs(x = "Devices", y = "Count",  
           title = "Operating Systems Utilized to Access the Application") + 
      theme_bw() + 
      scale_x_discrete(labels = c("iPhone", "Android", "iPad", "Pixel 3a: Android 10"))

    # SubQuestion #2: Which language is more frequently utilized with the 'Pesticide Labels Now' application? 

    library("dplyr")
    count_Language <- evViewPage.01 %>%
      count(evDesc2)

    library(tidyverse)

    str(evViewPage.01)
    #per_data(2) <- evViewPage.01 %>%
      #count(evDesc2) %>% 
      #mutate(per = n / sum(n),
             #per_label = paste0(round(per*100), "%"))

    str(evStart)
    per_data <- evStart %>%
      count(device_cat) %>% 
      mutate(per = n / sum(n),
             per_label = paste0(round(per*100), "%"))

    ggplot(per_data, aes(x = reorder(n, -per), y=per)) + 
      geom_bar(stat = "identity", fill = "lightblue", color = "black") + 
      geom_text(aes(label=per_label), vjust=-0.25) + 
      labs(x = "Language", y = "Count",  
           title = "Frequency of Each Language Accessed on the Application") + 
      theme_bw() + 
      scale_x_discrete(labels = c("English", "Spanish"))

    # Subquestion 1 + 2 Combined 

    install.packages("tidyr")
    library(tidyr)

    device_cat_aid <- unique(evStart[ , c("aid", "device_cat")])
    aid_device_language <- left_join(evViewPage.01, device_cat_aid, by="aid") 

    table(aid_device_language$evDesc2, aid_device_language$device_cat) 

    #With percentage labels 
    #https://stackoverflow.com/questions/68848650/create-percentage-labels-for-two-discrete-variables-in-ggplot-2
    ggplot(aid_device_language, aes(x=evDesc2)) + 
      geom_bar(aes(y = 2*(..count..)/sum(..count..), fill = device_cat, group=device_cat), stat="count") +
      geom_label(aes(label = scales::percent(2*(..count..)/sum(..count..)),
                      group = device_cat), position = "fill", stat= "count", vjust = 0) +
      labs(y = "Percent", fill="device_cat") +
      scale_y_continuous(labels = scales::percent)
      
    #------------------------------------------------------------------------------------------------

    #Attempt 2: with percentage labels 
    ggplot(data = aid_device_language2, na.rm = TRUE, aes(x = evDesc2, fill = device_cat)) + 
      geom_bar(position = "fill") + 
      scale_y_continuous(labels = function(x) paste0(x*100, "%")) + 
       labs(title = "Frequency of Different Languages by Device", 
           x = "Language", 
           y = "Percentage") +
          scale_x_discrete(labels = c("English", "Spanish")) + 
          scale_fill_discrete(name = "Devices", labels = c("Android", "iPad", "iPhone","Pixel:Android 10")) +     
            geom_text(data = aid_device_language %>% 
                  group_by(evDesc2, device_cat) %>%
                  tally() %>%
                  mutate(p = n / sum(n)) %>%
                  ungroup(),
                aes(y = p, label = scales::percent(p)),
                position = position_stack(vjust = 0.5),
                show.legend = FALSE)
                
    #Option 1: figure how to add 'Pixel 3a: Android 10' to android category 
    # -- create a new variable
    # -- ggplot(ignore NA)

    #Option 2: Remove 'Pixel 3a: Android 10' from dataset 
    # Where is 'NA' coming from? 

    #------------------------------------------------------------------------------------------------

    #Without percentage labels 
    install.packages("car")
    library(car)
    aid_device_language2 <- aid_device_language
    aid_device_language2$device_cat <- recode(aid_device_language2$device_cat,"c('iphone') = 'iOS'")
    aid_device_language2$device_cat <- recode(aid_device_language2$device_cat,"c('ipad') = 'iOS'")
    aid_device_language2$device_cat <- recode(aid_device_language2$device_cat,"c('android') = 'Android'")
    aid_device_language2$device_cat <- recode(aid_device_language2$device_cat,"c('Pixel 3a: Android 10') = 'android'")
    #aid_device_language2$device_cat <- case_when(aid_device_language2$device_cat == "Pixel 3a: Android 10" ~ "android", TRUE ~ NA)

    aid_device_language2 <- filter(aid_device_language2, !is.na(device_cat))

    aid_device_language2 <- filter(aid_device_language2, !is.na(evDesc2))

    which(is.na(aid_device_language2), arr.ind=TRUE)


    ggplot(data = aid_device_language2, aes(x = evDesc2, fill = device_cat)) + 
      geom_bar(position = "fill") + 
      scale_y_continuous(labels = function(x) paste0(x*100, "%")) + 
       labs(title = "Frequency of Different Languages by Device", 
           x = "Language", 
           y = "Percentage") +
          scale_x_discrete(labels = c("English", "Spanish")) +
          scale_fill_discrete(name = "Operating System", labels = c("Android", "iOS"))  
    #-------------------------------------------------------------------------------------------------------      
    ggplot(data = aid_device_language2, aes(x = evDesc2, fill = device_cat)) + 
      geom_bar(position = "fill") + 
      scale_y_continuous(labels = function(x) paste0(x*100, "%")) + 
       labs(title = "Frequency of Different Languages by Device", 
           x = "Language", 
           y = "Percentage") +
          scale_x_discrete(labels = c("English", "Spanish")) +
          scale_fill_discrete(name = "Operating System", labels = c("Android", "iOS")) 

    #-------------------------------------------------------------------------------------------------------
    #Original 
    ggplot(data = aid_device_language, aes(x = evDesc2, fill = device_cat)) + 
      geom_bar(position = "fill") + 
      scale_y_continuous(labels = function(x) paste0(x*100, "%")) + 
       labs(title = "Frequency of Different Languages by Device", 
           x = "Language", 
           y = "Percentage") +
          scale_x_discrete(labels = c("English", "Spanish")) + 
          scale_fill_discrete(name = "Devices", labels = c("Android", "iPad", "iPhone", "Pixel 3a: Android 10")) 

    #Subquestion #3: What is the relationship between location and utilization of the application? 

    install.packages("usmap")
    install.packages("ggplot2")

    #evStart provides latitude and longitude of MOST USERS 
    #1. remove variables that have "NA" for their latitude and longitude 
    evStart.location <- evStart[!(evStart$lat=="n/a" | evStart$lat=="NaN"),]
    evStart.location.1 <- subset(evStart.location, select = -c(aid, evDesc1, evDesc2, evDesc3, evType, ts, device_cat))


    #interactive map? 
    install.packages("leaflet")
    install.packages("dplyr")

    leaflet()%>%addTiles()
    leaflet()%>%addTiles()%>%addCircleMarkers(data=evStart.location.1, lat= ~lat, lng = ~lon)


    # ERROR: "addCirclMarkers requires numeric longitude/latitude values" 

    #-------------------------------------------------------------------------------------------------------

    #united states map 
    install.packages("usmap")
    install.packages("maptools")
    install.packages("rgdal")
    library(maptools)
    library("rgdal")

    transformed_data <-  usmap_transform(evStart.location.1)

    library(usmap)
    plot_usmap("states") + 
      geom_point(data = transformed_data, 
      aes(x=lon.1, y=lat.1),
      color="red",
      size=3)
    # ERROR: "addCircleMarkers requires numeric longitude/latitude values" 

    # Subquestion #4: What is the average number of labels looked at per session? 

    #Notes from Dennis on ‘How to find Number of Labels Search Per User in a Session’:
    # 1. Sort the list by aid 
    # 2. Sort by time stamp (not that it matters)
    # 3. Iterate through the list from (1) evStart 
    # 4. Set up a counter - evViewHS , from one evStart to the next evStart 

    # Heatmap
    install.packages("data.table")

    ## 
    ## The downloaded binary packages are in
    ##  /var/folders/g8/z7k53ktx0pg62hb1c7cf4h1m0000gn/T//RtmpInwOCE/downloaded_packages

    library(data.table)

    ## 
    ## Attaching package: 'data.table'

    ## The following objects are masked from 'package:lubridate':
    ## 
    ##     hour, isoweek, mday, minute, month, quarter, second, wday, week,
    ##     yday, year

    ## The following objects are masked from 'package:dplyr':
    ## 
    ##     between, first, last

    ## The following object is masked from 'package:purrr':
    ## 
    ##     transpose

    install.packages("dplyr")

    ## 
    ## The downloaded binary packages are in
    ##  /var/folders/g8/z7k53ktx0pg62hb1c7cf4h1m0000gn/T//RtmpInwOCE/downloaded_packages

    library(dplyr)
    install.packages("ggplot2")

    ## 
    ## The downloaded binary packages are in
    ##  /var/folders/g8/z7k53ktx0pg62hb1c7cf4h1m0000gn/T//RtmpInwOCE/downloaded_packages

    library(ggplot2)
    install.packages("lubridate")

    ## 
    ## The downloaded binary packages are in
    ##  /var/folders/g8/z7k53ktx0pg62hb1c7cf4h1m0000gn/T//RtmpInwOCE/downloaded_packages

    library(lubridate)

    setDT(x)
    y <- x[ , .(session_start = min(ts), session_end = max(ts), num_occurance = .N), by = sessionid]

    #'session time' column is added 
    y$sessiontime <- ymd_hms(y$session_end) - ymd_hms(y$session_start)
    y$sessiontime2 <- as.double(y$sessiontime)
    y$sessiontimemin <- y$sessiontime2/60

Time-Series Calendar HeatMap
![](Subquestions_files/figure-markdown_strict/unnamed-chunk-9-1.png)

    # heatmap attempt 4 (WORKS!)
    # x=hour of the day, y=day of the month, fill="activity"/number of occurances
    ggplot(y, aes(x=hour, y=day)) + geom_tile(aes(fill=num_occurance)) +
      labs(x="Hour of The Day",
           y="Day of the Month",
           title = "Time-Series Calendar Heatmap", 
           fill="Activity of the User")

![](Subquestions_files/figure-markdown_strict/unnamed-chunk-10-1.png)

    # heatmap attempt 6 (this is the one included in the poster)
    # sessiontime is done in seconds here 

    ggplot(y, aes(x=day, y=month)) + geom_tile(aes(fill=sessiontimemin)) + 
    scale_y_discrete(limits = month.abb) + 
     labs(x="Day of the Month",
           y="Month",
           title = "2020-2021 Calendar Heatmap", 
           fill="Session Time (minutes)")

![](Subquestions_files/figure-markdown_strict/unnamed-chunk-11-1.png)

    #heatmap attempt 7 (WORKS!)
    # (https://www.r-graph-gallery.com/283-the-hourly-heatmap.html)
    # Analyzes all 503 sessions... what day, time, and month 

    install.packages("ggplot2")
    library(ggplot2)
    install.packages("dplyr")
    library(dplyr) #easier data wrangling 
    install.packages("viridis")
    library(viridis) #colour blind friendly palette, works in B&W also
    install.packages("Interpol.T")
    library(Interpol.T) # will generate a large dataset on initial load
    install.packages("lubridate")
    library(lubridate) #for easy date manipulation
    install.packages("ggExtra")
    library(ggExtra) #because remembering ggplot theme options is beyond me
    install.packages("tidyr")
    library(tidyr) 

    df <-y %>% select(sessionid,day,hour,month,year)
    p <-ggplot(df,aes(day,hour))+
      geom_tile(color= "white",size=0.1) + 
      scale_fill_viridis(name="Hrly Temps C",option ="C")
    p <-p + facet_grid(year~month)
    p <-p + scale_y_continuous(trans = "reverse", breaks = unique(df$hour))
    p <-p + scale_x_continuous(breaks =c(1,10,20,31))
    p <-p + theme_minimal(base_size = 8)
    p <-p + labs(title= paste("Session Analytics"), x="Day of the Month", y="Hour Commencing")
    p <-p + theme(legend.position = "bottom")+
      theme(plot.title=element_text(size = 14))+
      theme(axis.text.y=element_text(size=6)) +
      theme(strip.background = element_rect(colour="white"))+
      theme(plot.title=element_text(hjust=0))+
      theme(axis.ticks=element_blank())+
      theme(axis.text=element_text(size=7))+
      theme(legend.title=element_text(size=8))+
      theme(legend.text=element_text(size=6))
    p

    # heatmap attempt 
    install.packages("ggplot2")
    library(ggplot2)
    install.packages("dplyr")
    library(dplyr) #easier data wrangling 
    install.packages("viridis")
    library(viridis) #colour blind friendly palette, works in B&W also
    install.packages("Interpol.T")
    library(Interpol.T) # will generate a large dataset on initial load
    install.packages("lubridate")
    library(lubridate) #for easy date manipulation
    install.packages("ggExtra")
    library(ggExtra) #because remembering ggplot theme options is beyond me
    install.packages("tidyr")
    library(tidyr) 

    df <-y %>% select(sessionid,day,hour,month,year) %>% fill(sessiontime2)
    p <-ggplot(df,aes(day,hour, fill=sessiontime2))+
      geom_tile(color= "white",size=0.1) + 
      scale_fill_viridis(name="Hrly Temps C",option ="C")
    p <-p + facet_grid(year~month)
    p <-p + scale_y_continuous(trans = "reverse", breaks = unique(df$hour))
    p <-p + scale_x_continuous(breaks =c(1,10,20,31))
    p <-p + theme_minimal(base_size = 8)
    p <-p + labs(title= paste("Session Analytics"), x="Day of the Month", y="Hour Commencing")
    p <-p + theme(legend.position = "bottom")+
      theme(plot.title=element_text(size = 14))+
      theme(axis.text.y=element_text(size=6)) +
      theme(strip.background = element_rect(colour="white"))+
      theme(plot.title=element_text(hjust=0))+
      theme(axis.ticks=element_blank())+
      theme(axis.text=element_text(size=7))+
      theme(legend.title=element_text(size=8))+
      theme(legend.text=element_text(size=6))
    p

    # cumulative distribution plot
    # https://rpubs.com/tgjohnst/cumulative_plotting
    # https://stackoverflow.com/questions/66471218/plotting-a-cumulative-frequency-curve-on-a-histogram-in-r

    # Average session duration 
    sum(y$sessiontime)

    ## Time difference of 7179658 secs

    (7179658/60)

    ## [1] 119661

    119661/1328

    ## [1] 90.10617

    #90.11

<img src="Subquestions_files/figure-markdown_strict/user-map-wa-2-1.png" width="100%" />
