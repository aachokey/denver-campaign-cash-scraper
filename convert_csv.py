import csv
import json


def main():
    
    DATA_FILE = "denver-contributions.json"
    OUTPUT_FILE = "denver-contributions.csv"
    
    contribution_data = None
    with open(DATA_FILE, "r") as df:
        contribution_data = json.load(df)
    
    
    contribution_data = contribution_data["searchContributionTransactions"]
    
    with open(OUTPUT_FILE, "w") as outfile:
        fieldnames = contribution_data[0].keys()
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contribution_data)
            

if __name__ == "__main__":
    main()