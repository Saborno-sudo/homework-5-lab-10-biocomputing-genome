############################
# Homework 5
# Create Unique SNP List
############################

input_file = "clean_snplist.txt"
output_file = "unique_snps.txt"

snps = []

# Read cleaned SNP list
with open(input_file, "r") as file:
    for line in file:
        snp = line.strip()

        if snp:
            snps.append(snp)


# Remove duplicates
unique_snps = sorted(set(snps))


# Write unique SNPs to a new file
with open(output_file, "w") as file:
    for snp in unique_snps:
        file.write(snp + "\n")


print("Duplicate removal complete!")
print("Total SNPs before removing duplicates:", len(snps))
print("Unique SNPs:", len(unique_snps))
print("Saved to:", output_file)