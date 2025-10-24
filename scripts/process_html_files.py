import re

file_18S = "../data/raw_data/18S_V5.html"
file_28S = "../data/raw_data/28S_V5.html"


def extract_fasta(file, rRNA):
    sequence_dict = {}
    with open(file, "r") as f:
        content = f.read().splitlines()
        for line in content:
            # Remove all the span tags
            line = re.sub(r"<span.*?>|</span>", "", line)
            line = line.replace("<br>", "")
            line = line.replace("<pre>", "")
            line = line.replace("</pre>", "")
            # Change multiple spaces to a single space
            line = re.sub(r" +", " ", line)

            if (
                len(line.strip()) > 0
                and not line.startswith(" ")
                and not line.startswith("<")
            ):
                name, seq, num = line.split(" ")
                if name not in sequence_dict:
                    sequence_dict[name] = seq
                else:
                    sequence_dict[name] += seq

    with open(f"../data/raw_data_processed/{rRNA}_V5.fasta", "w") as out:
        for name, seq in sequence_dict.items():
            seq = seq.replace("-", "")
            out.write(f">{name}\n{seq}\n")


def main():
    extract_fasta(file_18S, "18S")
    extract_fasta(file_28S, "28S")


if __name__ == "__main__":
    main()
