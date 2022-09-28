# Raidbots-Sheets-Python-Script
<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This Project exists to save time on loot decisions. In the past I had to open every droptimizer link provided individually and compare numbers. This Python project aggregates the links and creates a spreadsheet in which you can easily compare DPS per item per character.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Follow the instructions listed here to set up your authentication:
https://docs.gspread.org/en/latest/oauth2.html
https://gspread-pandas.readthedocs.io/en/latest/configuration.html#alternate-workflows

On line 34 fill in your local key's file name within the ""

On line 37 fill in your spreadsheet url within the ""

On line 133 fill in the spreadsheet key within the ''
This is part of the spreadsheet URL, everything that comes after d/ and before the next /

### Prerequisites

* gspread
  ```sh
  pip install gspread
  ```

* pandas
  ```sh
  pip install pandas
  ```

* gspread-pandas
  ```sh
  pip install gspread-pandas
  ```

* oauth2client
  ```sh
  pip install oauth2client
  ```

Old version of script (Deprecated)
* df2gspread
  ```sh
  pip install df2gspread
  ``` 
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
<!-- USAGE EXAMPLES -->
## Usage

Create a Spreadsheet on the account you authenticated.

After filling out all the information from the Getting Started section, create a second worksheet and keep its name as Sheet2.

In Sheet 1 format your Columns so that A1 is Raid Character and B1 is Droptimizer Links.

For your sanity you can name each link in the A column but it is not necessary.

In the B column for every character you want to add copy the droptimizer URL in B2 to BN.

Now you can run the script and the information will populate in worksheet Sheet2.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Add Sheet settings to the Script (automatic filter, automatic resizing, etc)
- [ ] Pull droptimizer links from other worksheets

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>