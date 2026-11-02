############################
# Homework 5
# Clean SNP List
############################

import re

input_file = "snplist.txt"
output_file = "clean_snplist.txt"

clean_snps = []

# Open original SNP list
with open(input_file, "r") as file:
    for line in file:

        # Remove extra spaces/newlines
        line = line.strip()

        # Skip header and empty lines
        if not line or line.upper() == "SNP":
            continue

        # Find every rs number in the line
        snps = re.findall(r"rs\d+", line)

        # Add each SNP separately
        clean_snps.extend(snps)


# Write cleaned SNPs to a new file
with open(output_file, "w") as file:
    for snp in clean_snps:
        file.write(snp + "\n")############################
# Homework 5
# Clean SNP List
############################

import re

input_file = "snplist.txt"
output_file = "clean_snplist.txt"

clean_snps = []

# Open original SNP list
with open(input_file, "r") as file:
    for line in file:

        # Remove extra spaces/newlines
        line = line.strip()

        # Skip header and empty lines
        if not line or line.upper() == "SNP":
            continue

        # Find every rs number in the line
        snps = re.findall(r"rs\d+", line)

        # Add each SNP separately
        clean_snps.extend(snps)


# Write cleaned SNPs to a new file
with open(output_file, "w") as file:
    for snp in clean_snps:
        file.write(snp + "\n")


print("Cleaning complete!")
print("Total SNPs:", len(clean_snps))
print("Saved to:", output_file)


print("Cleaning complete!")
print("Total SNPs:", len(clean_snps))
print("Saved to:", output_file)