# food-nutrition

> A simple command-line-based program (food nutrition optimization) implemented using branch and bound algorithm.

- [General Info](#General-Info)
- [Technologies](#Technologies)
- [Install](#Install)
- [Run](#Run)
- [Versioning](#Versioning)
- [Roadmap](#Roadmap)
- [Author](#Author)
- [Reference](#Reference)

## General Info

This project is one of tasks in IF2211 Strategi Algoritma. The goal of this project is to create a program which can optimize food consumption by budget and energy need. This project is implemented using branch and bound algorithm.

## Technologies

- Python 3 (minimum)

## Install

- clone this repository

```
git clone https://github.com/mgstabrani/food-nutrition.git
```

## Run

- Follow this instruction to run in your local command line.

```
python main.py
```

## Versioning

This project follows Semantic Versioning with staged modernization:

- `MAJOR`: breaking public interface changes (CLI, SDK, REST API contracts).
- `MINOR`: backward-compatible features and improvements.
- `PATCH`: backward-compatible bug fixes.

Current version is stored in `VERSION` and release notes are tracked in `CHANGELOG.md`.

## Roadmap

- Step 1: Semantic versioning baseline (`0.1.0`).
- Step 2: Core engine refactor (separate algorithm from input/output).
- Step 3: CLI adapter on top of shared core.
- Step 4: Python SDK adapter.
- Step 5: REST API adapter with versioned endpoints.

## Author

[Mgs. Tabrani (13519122)](https://github.com/mgstabrani)

## Reference

- [Angka Kecukupan Gizi (AKG)](http://hukor.kemkes.go.id/uploads/produk_hukum/PMK_No__28_Th_2019_ttg_Angka_Kecukupan_Gizi_Yang_Dianjurkan_Untuk_Masyarakat_Indonesia.pdf)
- [Food nutrition search engine](https://nilaigizi.com/)
