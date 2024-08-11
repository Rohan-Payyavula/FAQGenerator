from langchain_openai import ChatOpenAI
import csv
import requests
from bs4 import BeautifulSoup


class FAQGenerator:
    def __init__(self, api_key):
        self.llm = ChatOpenAI(api_key=api_key)

    def get_information_from_website(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                paragraphs = " ".join([p.text for p in soup.find_all('p')])

                lists = " ".join([li.text for ul in soup.find_all('ul') for li in ul.find_all('li')])

                # Extract tables
                tables = []
                for table in soup.find_all('table'):
                    rows = table.find_all('tr')
                    for row in rows:
                        cells = row.find_all(['th', 'td'])
                        table_row = " | ".join([cell.text.strip() for cell in cells])
                        tables.append(table_row)
                tables = " ".join(tables)

                info = f"{paragraphs} {lists} {tables}"
                return info
            else:
                print(f"Failed to fetch data from the website. Status code: {response.status_code}")
                return ""
        except Exception as e:
            print(f"An error occurred while fetching data from the website: {e}")
            return ""

    def getFAQ(self, url, topic, num_faqs=10):
        website_info = self.get_information_from_website(url)
        prompt = f"Based on the information from the website: {website_info}, give me {num_faqs} FAQs on the topic {topic}."
        output = self.llm.invoke(prompt)
        output_list = output.content.split('\n')
        return output_list

    def getAns(self, questions):
        answer_list = []
        for question in questions:
            answer = self.llm.invoke(question).content
            answer_list.append(answer)
        return answer_list

    def makeCSV(self, filename, questions, answers):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            for question, answer in zip(questions, answers):
                writer.writerow([question, answer])


def main():
    #Main method
    pass


if __name__ == "__main__":
    main()

