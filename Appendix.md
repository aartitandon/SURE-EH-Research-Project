# APPENDIX

<br>

# Data Dictionary 

## evDownload.01 subset

Unique devices (aid)

```{r unique-evDownload-users, echo=F, warning=F, message=F}

print(n_distinct(evDownload.01$aid), style="rmarkdown")


| Variable      | Description                    |
|---------------|--------------------------------|
| aid           | Random device identifier       |
| epaReg        | EPA regsistration number       |
| prodName      | Pesticide product name         |
| sourcePage    | App page visited?              |
| evType        | Action taken on app (download) |
| ts            | Timestamp yyy:mm:dd:hh:mm:ss   |


## evStart subset

Unique users (aid)

```{r unique-evStart-users, echo=F, warning=F, message=F}
print(n_distinct(evStart$aid), style="rmarkdown")
```

```{r evStart-dictionary, echo=F, message=F, warnings=F, results='asis'}
tabl <- "
| Variable      | Description                     |
|---------------|---------------------------------|
| aid           | Random device identifier        |
| evDesc1       | App version?                    |
| evDesc2       | Device type                     |
| evDesc3       | GPS coordinates                 |
| evType        | Action taken on app (start page) |
| ts            | Timestamp yyy:mm:dd:hh:mm:ss    |
"
cat(tabl)
```

## evViewPage.01 subset

Unique users (aid)

```{r unique-evViewpage-users, echo=F, warning=F, message=F}
print(n_distinct(evViewPage.01$aid), style="rmarkdown")
```

```{r evViewPage.01-dictionary, echo=F, message=F, warnings=F, results='asis'}
tabl <- "
| Variable      | Description                     |
|---------------|---------------------------------|
| aid           | Random device identifier        |
| evDesc1       | First action on app             |
| evDesc2       | English or Spanish              |
| evDesc3       | Pesticide label viewed          |
| evType        | Action taken on app (view page) |
| ts            | Timestamp yyy:mm:dd:hh:mm:ss    |
"
cat(tabl)
```

## Detailed variable descriptions

- Device = identified by a randomly assigned identifier. = Person. Person = device. There is no way to distinguish individual users. One device can be used by ≥ 1 person and 1 person can use ≥ 1 device.
- Access = accessed app = put PLN on device and opened app (app opens to label List).
- Session = time from when the app opened until just before next time it is opened.
- PICOL Searches = PICOL results viewed.
- Label searches = Label menu viewed.
- View = accessed and viewed information (any combination of ≥ 1 of the following)
- Label view = accessed + [(opened ≥ 1 label) + (opened ≥ 1 menu bar)] 
Label view + PDF = accessed + [(opened ≥ 1 label) + (opened ≥ 1 menu bar)+ (downloaded label PDF)] 
- PICOL view = accessed + [(conducted ≥ 1 PICOL search) + (viewed ≥ 1 PICOL result)]
- PICOL view + PDF  = accessed app + [(conducted ≥ 1 PICOL search) + (viewed ≥ 1 PICOL result) + (downloaded app)]
- General  view = accessed +(viewed label search page + selected a label, but did not open menu bar) and/or ( viewed PICOL search page) and/or viewed more pages
General  view + links
- Location = GPS coordinates. de-identified location in that it is somewhere within the ~ 500 ft radius. We will only report by broad areas. Agricultural regions if they are defined. Currently, many iPhone users are declining location as Apple is asking users if they want the location turned on/off with each update.  We may only be able to evaluate this up to the April release date.
 App is only available to devices registered in the US, CA, and MX. However, phones registered in these countries can be used anywhere. For example, we had a user connect from S. America from a US registered phone. 
- Population A definition: anyone that has accessed the app.  There is 1 excluded population and 3 study subpopulations (based on gps location coordinates at time the app is opened.)
    - Device used in WA state GPS data. (Not Seattle or King County)
    - Device used outside of WA state
    - No location (location services are off.)
    - Exclude. King County or at least the Seattle metropolitan area locations.  These are likely team and PNASH staff. Exclusion list. Selected random devices IDs are on an exclusion list. These are test devices. 

- Population B definition: (Only use if enough people respond to in app questions). Those users that respond to the location in-app question. (This response can be linked to app analytic data as it has the same random unique ID). This will be implemented very soon.
    - Response I work in WA state (not quite the same as where they downloaded it)
    - Response I work outside of Washington state
    - Do not want to answer
    - Skips answering the question.  (will combine with c)
