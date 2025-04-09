# Labor Market Reporting

This collection of scripts takes inputs from scraped Hot 50 MI jobs information, Lightcast Occupation Reports, CIP to SOC conversions, and University majors and delivers
tabular data breaking down all of the professions associated with university degrees, statistics of demographics, information of the positions, hiring data for the state of Michigan,
and growth projections.

Used at the CLDC to Create a Yearly Labor Market Dashboard.

[![Watch the video](demo.mp4)]()

***

> [!WARNING]
> Ensure that Input files are up to date and named properly in the [configuration](#configuring-files).

> [!IMPORTANT]
> Google configuration includes a folder for the desired year with documents titled after each SOC code containing companies hiring and the count of positions they've hired.


## Setup
1. Clone this repository.
2. Ensure all [dependencies](#dependencies) are configured and running properly
3. [Update and Configure](#configuring-files)
4. Run 
```{jupyter}
jupyter nbconvert --to notebook --inplace --execute match_codes.ipynb
```
5. (Optional) Replace connections/files in the OneDrive to update the Labor Market Dashboard annually.

## Features
- [x] Scrapes Hot 50 Michigan Jobs Report 
- [x] Delivers statistics for all jobs provided by OU degrees to `/Outputs` folder
- [x] Used to power Labor Market Dashboard in PowerBI.

## Dependencies
See `requirements.txt` for a list of required packages.
``` {CLI}
pip install -r requirements.txt
```

## Configuring Files
> [!IMPORTANT]
> These Files Should Exist and Be Updated Annually: 
> * CIP_TO_SOC_CROSSWALK: File from NCES that gives CIP to SOC conversion. [Link](https://nces.ed.gov/ipeds/cipcode/post3.aspx?y=56)
> * MAJORS: File from OU that lists all majors and associated CIP codes at Oakland University
> * LIGHTCAST_OCCUPATION_REPORT: Occupation Table report from Lightcast (**SET YEARS TO INCLUDE NEXT SUBSET IN SPAN -- EX: if 2023-2033 change to 2024-2034). [Link](https://analyst.lightcast.io/analyst/?t=4ntrw#h=QDCXTPV.5CE7KuiyBpH9GyNG_J&page=occupation_table&vertical=standard&nation=us)
> * MISMATCHED_LIGHTCAST_CODES: Custom text file that includes conversions of codes that are incorrectly listed on Lightcast.
> * HOT_50_INPUT: The Michigan Center for Data and Analytics Hot Jobs Report. [Link](https://www.michigan.gov/mcda/reports/michigan-hot-50)

> [!IMPORTANT]
> Ensure that file paths are configured properly in `config.json`.


