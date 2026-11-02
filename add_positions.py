############################
# Homework 5
# Add Chromosome and Position
############################

unique_file = "unique_snps.txt"
ucsc_file = "uscs_results.txt"
output_file = "final_snplist.txt"

# Dictionary to store SNP positions
positions = {}

# Read UCSC results
with open(ucsc_file, "r") as file:
    for line in file:

        # Skip header lines
        if line.startswith("#"):
            continue

        columns = line.strip().split("\t")

        if len(columns) >= 4:
            chrom = columns[0]
            chrom_start = columns[1]
            snp = columns[3]

            # Use regular chromosomes only
            if chrom in [f"chr{i}" for i in range(1, 23)] + ["chrX", "chrY"]:

                # Convert 0-based UCSC position to 1-based
                position = int(chrom_start) + 1

                # Remove "chr" from chromosome name
                chromosome = chrom.replace("chr", "")

                positions[snp] = (chromosome, position)


# Read unique SNP list and create final output
with open(unique_file, "r") as infile, open(output_file, "w") as outfile:

    # Header
    outfile.write("Chr\tpos(1-based)\tsnp\n")

    for line in infile:
        snp = line.strip()

        if not snp:
            continue

        if snp in positions:
            chromosome, position = positions[snp]
            outfile.write(f"{chromosome}\t{position}\t{snp}\n")

        else:
            outfile.write(f"NA\tNA\t{snp}\n")


print("Finished!")
print("SNP positions found:", len(positions))
print("Final file saved to:", output_file)