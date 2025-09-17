
# SolanaMnemonic

Simple utility for generating and working with **BIP39 mnemonics** for Solana wallets.
Useful for creating and storing Solana wallets on any device.

## Overview

This project provides tools to generate BIP39 mnemonic seed phrases compatible with Solana keypair derivation. Mnemonics make it easier for users to securely back up and restore their wallet keys using a list of human-readable words instead of raw private keys.

## Features

- Generate random BIP39 mnemonic phrases (12, 15, 18, 21, or 24 words)
- Compatible with Solana wallet key derivation standards
- Lightweight and easy to integrate into Solana wallet projects
- MIT licensed

## Installation

Clone the repository or download the source code:

```bash
git clone https://github.com/Wesker222/SolanaMnemonic.git
cd SolanaMnemonic
```

Install dependencies (if any, depending on implementation language):

```bash
# Example for Node.js (if applicable)
npm install
```

## Usage

### Generate a new mnemonic phrase

Example (TypeScript/JavaScript):

```typescript
import * as bip39 from "bip39";

const mnemonic = bip39.generateMnemonic();
console.log("Generated mnemonic:", mnemonic);
```

### Derive Solana keypair from mnemonic

You can use standard Solana libraries (e.g., `@solana/web3.js` or `bip_utils` in Python) to derive keys from the mnemonic.

## License

This project is licensed under the **MIT License**.

```
