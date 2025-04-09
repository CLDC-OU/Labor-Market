# ONET API Access

This ONET_report utilizes access to the BLS API in an easy-to-access format.

## Table of Contents
1. [Example Usage](#example-usage)
2. [Returns](#returns)

## Example Usage

```shell{example}
from ONET_API import ONET_report

codes = sys.stdin.read().split("\n")
ONET_report(codes).call()
```

## Returns
* A json string containing job information for every SOC Code given with format:

```shell{example}
   {
  "11-1011.00": {
    "results": {
      "abilities": {
        "group": [
          {
            "element": [
              {
                "id": "1.A.1.a.1",
                "name": "listen and understand what people say"
              },
              {
                "id": "1.A.1.a.3",
                "name": "communicate by speaking"
              }
            ],
            "title": {
              "id": "1.A.1.a",
              "name": "Verbal"
            }
          },
          {
            "element": [
              {
                "id": "1.A.1.b.4",
                "name": "use rules to solve problems"
              },
              {
                "id": "1.A.1.b.5",
                "name": "make general rules or come up with answers from lots of detailed information"
              }
            ],
            "title": {
              "id": "1.A.1.b",
              "name": "Ideas and Logic"
            }
          },
          {
            "element": [
              {
                "id": "1.A.1.c.1",
                "name": "choose the right type of math to solve a problem"
              },
              {
                "id": "1.A.1.c.2",
                "name": "add, subtract, multiply, or divide"
              }
            ],
            "title": {
              "id": "1.A.1.c",
              "name": "Math"
            }
          },
          {
            "element": [
              {
                "id": "1.A.1.e.2",
                "name": "see hidden patterns"
              }
            ],
            "title": {
              "id": "1.A.1.e",
              "name": "Visual Understanding"
            }
          }
        ]
      },
      "career": {
        "also_called": {
          "title": [
            "CEO (Chief Executive Officer)",
            "Chief Financial Officer (CFO)",
            "Chief Operating Officer (COO)",
            "President"
          ]
        },
        "career_video": true,
        "code": "11-1011.00",
        "on_the_job": {
          "task": [
            "Direct or coordinate an organization's financial or budget activities to fund operations, maximize investments, or increase efficiency.",
            "Confer with board members, organization officials, or staff members to discuss issues, coordinate activities, or resolve problems.",
            "Prepare budgets for approval, including those for funding or implementation of programs."
          ]
        },
        "resources": {
          "resource": [
            {
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-1011.00/knowledge",
              "title": "Knowledge"
            },
            {
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-1011.00/skills",
              "title": "Skills"
            },
            {
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-1011.00/abilities",
              "title": "Abilities"
            },
            {
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-1011.00/personality",
              "title": "Personality"
            },
            {
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-1011.00/technology",
              "title": "Technology"
            },
            {
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-1011.00/education",
              "title": "Education"
            },
            {
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-1011.00/job_outlook",
              "title": "Job Outlook"
            },
            {
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-1011.00/check_out_my_state",
              "title": "Check Out My State"
            },
            {
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-1011.00/explore_more",
              "title": "Explore More"
            }
          ]
        },
        "tags": {
          "apprenticeship": false,
          "bright_outlook": true,
          "green": false
        },
        "title": "Chief Executives",
        "what_they_do": "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan, direct, or coordinate operational activities at the highest level of management with the help of subordinate executives and staff managers."
      },
      "check_out_my_state": {
        "above_average": {
          "state": [
            {
              "location_quotient": 3.83,
              "name": "Guam",
              "postal_code": "GU"
            },
            {
              "location_quotient": 2.49,
              "name": "Virgin Islands",
              "postal_code": "VI"
            },
            {
              "location_quotient": 2.19,
              "name": "Puerto Rico",
              "postal_code": "PR"
            },
            {
              "location_quotient": 2.13,
              "name": "Alaska",
              "postal_code": "AK"
            },
            {
              "location_quotient": 2.07,
              "name": "Nebraska",
              "postal_code": "NE"
            },
            {
              "location_quotient": 1.79,
              "name": "Maine",
              "postal_code": "ME"
            },
            {
              "location_quotient": 1.69,
              "name": "Vermont",
              "postal_code": "VT"
            },
            {
              "location_quotient": 1.67,
              "name": "Minnesota",
              "postal_code": "MN"
            },
            {
              "location_quotient": 1.63,
              "name": "West Virginia",
              "postal_code": "WV"
            },
            {
              "location_quotient": 1.56,
              "name": "California",
              "postal_code": "CA"
            },
            {
              "location_quotient": 1.45,
              "name": "Iowa",
              "postal_code": "IA"
            },
            {
              "location_quotient": 1.44,
              "name": "Kansas",
              "postal_code": "KS"
            },
            {
              "location_quotient": 1.42,
              "name": "Florida",
              "postal_code": "FL"
            },
            {
              "location_quotient": 1.39,
              "name": "District of Columbia",
              "postal_code": "DC"
            },
            {
              "location_quotient": 1.38,
              "name": "Utah",
              "postal_code": "UT"
            },
            {
              "location_quotient": 1.37,
              "name": "Maryland",
              "postal_code": "MD"
            },
            {
              "location_quotient": 1.3,
              "name": "Tennessee",
              "postal_code": "TN"
            }
          ]
        },
        "average": {
          "state": [
            {
              "location_quotient": 1.24,
              "name": "Arkansas",
              "postal_code": "AR"
            },
            {
              "location_quotient": 1.18,
              "name": "Oklahoma",
              "postal_code": "OK"
            },
            {
              "location_quotient": 1.07,
              "name": "Virginia",
              "postal_code": "VA"
            },
            {
              "location_quotient": 1.05,
              "name": "Kentucky",
              "postal_code": "KY"
            },
            {
              "location_quotient": 1,
              "name": "Georgia",
              "postal_code": "GA"
            },
            {
              "location_quotient": 0.98,
              "name": "South Carolina",
              "postal_code": "SC"
            },
            {
              "location_quotient": 0.98,
              "name": "Wisconsin",
              "postal_code": "WI"
            },
            {
              "location_quotient": 0.88,
              "name": "South Dakota",
              "postal_code": "SD"
            },
            {
              "location_quotient": 0.83,
              "name": "Washington",
              "postal_code": "WA"
            }
          ]
        },
        "below_average": {
          "state": [
            {
              "location_quotient": 0.75,
              "name": "Arizona",
              "postal_code": "AZ"
            },
            {
              "location_quotient": 0.75,
              "name": "Illinois",
              "postal_code": "IL"
            },
            {
              "location_quotient": 0.7,
              "name": "Ohio",
              "postal_code": "OH"
            },
            {
              "location_quotient": 0.67,
              "name": "Montana",
              "postal_code": "MT"
            },
            {
              "location_quotient": 0.65,
              "name": "Hawaii",
              "postal_code": "HI"
            },
            {
              "location_quotient": 0.63,
              "name": "Michigan",
              "postal_code": "MI"
            },
            {
              "location_quotient": 0.59,
              "name": "New Hampshire",
              "postal_code": "NH"
            },
            {
              "location_quotient": 0.58,
              "name": "New York",
              "postal_code": "NY"
            },
            {
              "location_quotient": 0.54,
              "name": "Delaware",
              "postal_code": "DE"
            },
            {
              "location_quotient": 0.48,
              "name": "North Dakota",
              "postal_code": "ND"
            },
            {
              "location_quotient": 0.39,
              "name": "Connecticut",
              "postal_code": "CT"
            },
            {
              "location_quotient": 0.37,
              "name": "Texas",
              "postal_code": "TX"
            },
            {
              "location_quotient": 0.36,
              "name": "Mississippi",
              "postal_code": "MS"
            },
            {
              "location_quotient": 0.3,
              "name": "Oregon",
              "postal_code": "OR"
            },
            {
              "location_quotient": 0.29,
              "name": "Indiana",
              "postal_code": "IN"
            },
            {
              "location_quotient": 0.27,
              "name": "Wyoming",
              "postal_code": "WY"
            },
            {
              "location_quotient": 0.26,
              "name": "North Carolina",
              "postal_code": "NC"
            },
            {
              "location_quotient": 0.25,
              "name": "Alabama",
              "postal_code": "AL"
            },
            {
              "location_quotient": 0.19,
              "name": "New Jersey",
              "postal_code": "NJ"
            },
            {
              "location_quotient": 0.16,
              "name": "Colorado",
              "postal_code": "CO"
            },
            {
              "location_quotient": 0.15,
              "name": "Louisiana",
              "postal_code": "LA"
            }
          ]
        },
        "legend": {
          "height": 85,
          "href": "https://services.onetcenter.org/ws/mnm/state-maps/legend.gif",
          "width": 230
        },
        "map": {
          "height": 340,
          "href": "https://services.onetcenter.org/ws/mnm/state-maps/11-1011.gif",
          "width": 600
        }
      },
      "code": "11-1011.00",
      "education": {
        "education_usually_needed": {
          "category": [
            "master's degree",
            "bachelor's degree"
          ]
        },
        "job_zone": 5
      },
      "explore_more": {
        "careers": {
          "career": [
            {
              "code": "11-9199.02",
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-9199.02/",
              "tags": {
                "apprenticeship": true,
                "bright_outlook": true,
                "green": false
              },
              "title": "Compliance Managers"
            },
            {
              "code": "11-1021.00",
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-1021.00/",
              "tags": {
                "apprenticeship": true,
                "bright_outlook": true,
                "green": false
              },
              "title": "General & Operations Managers"
            },
            {
              "code": "11-2032.00",
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-2032.00/",
              "tags": {
                "apprenticeship": false,
                "bright_outlook": true,
                "green": false
              },
              "title": "Public Relations Managers"
            },
            {
              "code": "11-9151.00",
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-9151.00/",
              "tags": {
                "apprenticeship": false,
                "bright_outlook": true,
                "green": false
              },
              "title": "Social & Community Service Managers"
            },
            {
              "code": "11-3031.01",
              "href": "https://services.onetcenter.org/ws/mnm/careers/11-3031.01/",
              "tags": {
                "apprenticeship": false,
                "bright_outlook": true,
                "green": false
              },
              "title": "Treasurers & Controllers"
            }
          ]
        },
        "industries": {
          "industry": [
            {
              "code": 54,
              "href": "https://services.onetcenter.org/ws/mnm/browse/54",
              "percent_employed": 13,
              "title": "Professional, Science, & Technical"
            }
          ],
          "soc_code": "11-1011"
        }
      },
      "job_outlook": {
        "bright_outlook": {
          "category": [
            "Grow Rapidly"
          ],
          "description": "This career will grow rapidly in the next few years."
        },
        "outlook": {
          "category": "Bright",
          "description": "New job opportunities are very likely in the future."
        },
        "salary": {
          "annual_10th_percentile": 80000,
          "annual_90th_percentile_over": 239200,
          "annual_median": 206680,
          "hourly_10th_percentile": 38.46,
          "hourly_90th_percentile_over": 115,
          "hourly_median": 99.37,
          "soc_code": "11-1011"
        }
      },
      "knowledge": {
        "group": [
          {
            "element": [
              {
                "id": "2.C.1.a",
                "name": "management"
              },
              {
                "id": "2.C.1.f",
                "name": "human resources (HR)"
              }
            ],
            "title": {
              "id": "2.C.1",
              "name": "Business"
            }
          },
          {
            "element": [
              {
                "id": "2.C.7.a",
                "name": "English language"
              }
            ],
            "title": {
              "id": "2.C.7",
              "name": "Arts and Humanities"
            }
          },
          {
            "element": [
              {
                "id": "2.C.8.a",
                "name": "public safety and security"
              },
              {
                "id": "2.C.8.b",
                "name": "law and government"
              }
            ],
            "title": {
              "id": "2.C.8",
              "name": "Safety and Government"
            }
          },
          {
            "element": [
              {
                "id": "2.C.3.a",
                "name": "computers and electronics"
              }
            ],
            "title": {
              "id": "2.C.3",
              "name": "Engineering and Technology"
            }
          }
        ]
      },
      "personality": {
        "top_interest": {
          "description": "People interested in this work like activities that include leading, making decisions, and business.",
          "id": "1.B.1.e",
          "title": "Enterprising"
        },
        "work_styles": {
          "element": [
            {
              "id": "1.C.2.b",
              "name": "Leadership"
            },
            {
              "id": "1.C.1.c",
              "name": "Initiative"
            },
            {
              "id": "1.C.1.b",
              "name": "Persistence"
            },
            {
              "id": "1.C.7.b",
              "name": "Analytical Thinking"
            },
            {
              "id": "1.C.1.a",
              "name": "Achievement/Effort"
            },
            {
              "id": "1.C.5.c",
              "name": "Integrity"
            }
          ]
        }
      },
      "skills": {
        "group": [
          {
            "element": [
              {
                "id": "2.A.2.a",
                "name": "thinking about the pros and cons of different ways to solve a problem"
              },
              {
                "id": "2.A.1.d",
                "name": "talking to others"
              }
            ],
            "title": {
              "id": "2.A",
              "name": "Basic Skills"
            }
          },
          {
            "element": [
              {
                "id": "2.B.2.i",
                "name": "noticing a problem and figuring out the best way to solve it"
              }
            ],
            "title": {
              "id": "2.B.2",
              "name": "Problem Solving"
            }
          },
          {
            "element": [
              {
                "id": "2.B.4.e",
                "name": "thinking about the pros and cons of different options and picking the best one"
              },
              {
                "id": "2.B.4.h",
                "name": "measuring how well a system is working and how to improve it"
              }
            ],
            "title": {
              "id": "2.B.4",
              "name": "People and Technology Systems"
            }
          }
        ]
      },
      "technology": {
        "category": [
          {
            "example": [
              {
                "hot_technology": "Microsoft Dynamics",
                "name": "Microsoft Dynamics"
              },
              {
                "hot_technology": "Oracle PeopleSoft",
                "name": "Oracle PeopleSoft"
              }
            ],
            "title": {
              "name": "Enterprise resource planning ERP software"
            },
            "unspsc": 43231602
          },
          {
            "example": [
              {
                "name": "Mentimeter"
              },
              {
                "hot_technology": "Microsoft PowerPoint",
                "name": "Microsoft PowerPoint"
              }
            ],
            "title": {
              "name": "Presentation software"
            },
            "unspsc": 43232106
          },
          {
            "example": [
              {
                "hot_technology": "Intuit QuickBooks",
                "name": "Intuit QuickBooks"
              },
              {
                "name": "Sage 50 Accounting"
              }
            ],
            "title": {
              "name": "Accounting software"
            },
            "unspsc": 43231601
          }
        ]
      },
      "where_do_they_work": {
        "industry": [
          {
            "code": 54,
            "href": "https://services.onetcenter.org/ws/mnm/browse/54",
            "percent_employed": 13,
            "title": "Professional, Science, & Technical"
          }
        ]
      }
    }
  }
```












































The following is a set of instructions to utilize custom calls to the BLS API and output them as a json file of your choice.

## Usage
Please follow the instructions to make calls and deliver outputs for the ONET API:

1. Create a .txt file containing desired SOC codes:
    ```{python}
    # EX [Code Input.txt]:
    00-0001
    00-0002
    00-0003
    ```

2. Run the following from the command line:
    ```{CLI} 
    python [Path to SOC Codes Input.txt] < [Path to]ONET_API.py > [Path to Desired Output.json]
    ```
    Where
    * `[Path to SOC Codes Input.txt]` is the path to your text file containing desired SOC Codes.
    * `[Path to Desired Output.json]` is the path to and the name of your desired json return file.