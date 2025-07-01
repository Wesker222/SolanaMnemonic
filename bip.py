from mnemonic import Mnemonic

def generate_bulk_mnemonics(count, words=12):
    mnemo = Mnemonic("english")
    mnemonics_list = []

    for _ in range(count):
        # Generate mnemonic with the specified number of words (12, 15, 18, 21, 24)
        mnemonic = mnemo.generate(strength=words * 32 // 3)  # 128 bits for 12 words, 160 for 15, etc.
        mnemonics_list.append(mnemonic)

    return mnemonics_list

def save_mnemonics_to_file(mnemonics, filename="solana_mnemonics.txt"):
    with open(filename, "w") as f:
        for m in mnemonics:
            f.write(m + "\n")

if __name__ == "__main__":
    num_phrases = int(input("How many Solana mnemonics do you want to generate? "))
    mnemonics = generate_bulk_mnemonics(num_phrases, words=12)
    save_mnemonics_to_file(mnemonics)
    print(f"{num_phrases} mnemonics saved to solana_mnemonics.txt")
