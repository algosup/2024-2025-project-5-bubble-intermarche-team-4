# Wine & Cheese Data

## Repository structure

```
├── data/
    ├── images-meals/                   # Made by us
    └── cheeses.json                    # Made by us
    └── meal.json                       # Made by us
    └── wines.json                      # Made by us
    └── Data - Wine and Cheese.xlsx     # Provided by Intermarché Saint-Rémy-de-Provence
```

## Overview

* **Raw Source**: Data originally sourced from the Intermarché Saint-Rémy-de-Provence.
* **Unique JSON Format**: We've independently structured and enriched the raw datasets into a comprehensive JSON schema—no one else has published it this way.
* **Fields Included**:

  * `id`, `ITM8`, `EAN` — unique identifiers
  * `name`, `region`, `country`, `year`, `type`, `grape`/`milk`
  * `price`, `rating`, `description`, `description_en`, `image`, `bestseller`

## Usage

1. Clone or download this repository.
2. Load the JSON files into your application or database.
3. Build your UI or API on top of this data to showcase products and pairings.

## Attribution

All data in this repository is original and proprietary to the Intermarché Saint-Rémy-de-Provence.

> **Please credit our work**
>
> If you use or display this data in any form (publications, websites, applications), kindly acknowledge:
>
> *"Data provided by Team 4, curated in-house."*

## Contributing

For corrections, improvements, or feedback, please open an issue or contact the team directly.

---

*Thank you for respecting our work!*