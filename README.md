# FAQ Generator

## Overview

The FAQ Generator is a Python script that automatically generates Frequently Asked Questions (FAQs) based on information extracted from a given website. It scrapes the content, including paragraphs, lists, and tables, and uses an AI language model to formulate relevant FAQs and their corresponding answers. The generated FAQs are saved in a CSV file for easy access and distribution.


## Requirements

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `csv`
  - `langchain_openai`

## Example Usage

```bash
Give the site link: https://example.com/topic
What do you need FAQ on? Diabetes
FAQs saved to "Diabetes.csv".
```

## Limitations

- The quality of generated FAQs depends on the content available on the provided website and the capabilities of the AI model.
- The script assumes that the website is well-structured with relevant information in paragraphs, lists, or tables.

## License

This project is open-source and available under the [MIT License](LICENSE).


## Contact

For questions or feedback, please contact the author at [rohan.payyavula@outlook.com].
